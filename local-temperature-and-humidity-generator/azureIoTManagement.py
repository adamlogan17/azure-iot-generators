import time
import threading
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import ExportImportDevice
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
import json
from random import uniform

global exit_event # thread event used to kill a thread
exit_event = threading.Event() 

def retrieveHubName(connStr):
    """
    Gets the hub/device name from the connection string of the hub/device
    
    Parameters
    ----------
    connStr : str
        A connection string for an IoT Hub.

    Returns
    -------
    str
        The name of the IoT hub.
    """
    hubName = ""
    tempConnStr = connStr[9:]
    for c in tempConnStr:
        if c == ".":
            break
        hubName += c
    return hubName

def stop_sending():
    """Sets the thread event and allows the threads to be killed mid processing"""
    exit_event.set()

async def send_telemetry(conn_str, data="", numOfMessage=0, timeBetweenMssgs=1, tempRng=[20,30], humRng=[60.0,80.0]):
    """Sends Telemetry data to an individual device

    Parameters
    ----------
    connStr : str
        A connection string for an IoT Hub.
    data : str
        This is the payload of the message.
        If this is not given then temperature and humidity data will be sent.
    numOfMessage : int
        The number of messages to send.
        If this value is 0 then messages will continuously be sent until the program is killed.
    timeBetweenMssgs : float
        The time between each message to send, in seconds.
    tempRange : [float, float]
        A range of the values to be created for the temperature.
        The first element is the minimum value and the second element is the maximum value.
        This is not required if custom data is being used.
    humRange : [float, float]
        A range of the values to be created for the humidity.
        The first element is the minimum value and the second element is the maximum value.
        This is not required if custom data is being used.
    """
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    await device_client.connect()
    origData = data # used to store the first data being transmitted
    count = 1 # keeps track of how many messages are being sent

    # the 'not exit_event.is_set()' allows the messages to stop being sent at anytime
    while (count <= numOfMessage or numOfMessage==0) and (not exit_event.is_set()):
        # when 'origData' this is empty it means that the user wishes to use the default humidity and temperature data
        if origData == "": 
            data = {"messageId":count, "temperature":uniform(tempRng[0], tempRng[1]),"humidity":uniform(humRng[0], humRng[1])}
        await device_client.send_message(json.dumps(data)) # sends the message in JSON format
        count += 1 
        time.sleep(timeBetweenMssgs) # allows for a break between messages

    await device_client.disconnect() # disconnects the device when data has stopped sending

def send_telemetry_for_all_devices(iothub_connection_str, data="", numOfMessage=10, timeBetweenMssgs=1, tempRng=[], humRng=[]):
    """
    Creates threads for each device in an IoT Hub and sends telemetry data to each device

    Parameters
    ----------
    iothub_connection_str : str
        A connection string for an IoT Hub.
    data : str
        This is the payload of the message.
        If this is not given then temperature and humidity data will be sent.
    numOfMessage : int
        The number of messages to send.
        If this value is 0 then messages will continuously be sent until the program is killed.
    timeBetweenMssgs : float
        The time between each message to send, in seconds.
    tempRng : [float, float]
        A range of the values to be created for the temperature.
        The first element is the minimum value and the second element is the maximum value.
        This, along with humRng, must be included if the user would like to use temperature and humidity data.
        This is not required if custom data is being used.
    humRng : [float, float]
        A range of the values to be created for the humidity.
        The first element is the minimum value and the second element is the maximum value.
        This, along with tempRng, must be included if the user would like to use temperature and humidity data.
        This is not required if custom data is being used.

    Returns
    -------
    Thread[]
        A list of the Threads that was created.
    """
    iothub_registry_manager = IoTHubRegistryManager.from_connection_string(iothub_connection_str)
    max_number_of_devices = 1000 # sets the maximum devices that can be created
    devices = iothub_registry_manager.get_devices(max_number_of_devices)
    threads = []
    iotHubName = retrieveHubName(iothub_connection_str)
    if devices:
        for device in devices:
            deviceid = device.device_id # gets the device ID of a particular device
            primaryKey = device.authentication.symmetric_key.primary_key # gets the primary key of the device
            # the below line creates the connection string for the specific device
            connStr = "HostName={0}.azure-devices.net;DeviceId={1};SharedAccessKey={2}".format(iotHubName, deviceid, primaryKey)
            exit_event.clear() # clears the 
            # the below if statement checks if the user wishes to use the default data or if they would like to use their own data
            if len(tempRng) == 0 and len(humRng) == 0:
                startThread = threading.Thread(target=asyncio.run, args = (send_telemetry(connStr,data=data,numOfMessage=numOfMessage,timeBetweenMssgs=timeBetweenMssgs),), daemon=True) # creates a thread for each device that is created
            else:
                startThread = threading.Thread(target=asyncio.run, args = (send_telemetry(connStr,data=data,numOfMessage=numOfMessage,timeBetweenMssgs=timeBetweenMssgs,tempRng=tempRng, humRng=humRng),), daemon=True) # creates a thread for each device that is created
            startThread.start()
            threads.append(startThread)
               
        # waits for the threads to finish before continuing with the main program, this is needed as the devices will be deleted during the threads
        for thread in threads:
            thread.join()
    iothub_registry_manager = None # Set registry manager object to `None` so all open files get closed
    return threads

def create_devices(numDevices, iothub_connection_str):
    """
    Creates devices for a particular IoT Hub

    Parameters
    ----------
    numDevices : int
        The number of devices to be created.
    iothub_connection_str : str
        A connection string for an IoT Hub.

    Returns
    -------
    ExportImportDevice[]
        A list of the devices created
    """
    iothub_registry_manager = IoTHubRegistryManager.from_connection_string(iothub_connection_str)
    devices = []

    for i in range(numDevices):
        device = ExportImportDevice(id="createdDevice{0}".format(i+1), status="enabled")
        device.import_mode = "create"
        devices.append(device)
    iothub_registry_manager.bulk_create_or_update_devices(devices)

    iothub_registry_manager = None # Set registry manager object to `None` so all open files get closed
    return devices

def delete_devices(devices, iothub_connection_str):
    """
    Deletes devices for a particular IoT Hub

    Parameters
    ----------
    devices : ExportImportDevice[]
        The devices to be deleted.
    iothub_connection_str : str
        A connection string for an IoT Hub.
    """
    iothub_registry_manager = IoTHubRegistryManager.from_connection_string(iothub_connection_str)
    # below iterates through all the 'devices' that has chosen to be deleted
    for device in devices:
        device.import_mode = "delete"
    iothub_registry_manager.bulk_create_or_update_devices(devices)
    iothub_registry_manager = None # Set registry manager object to `None` so all open files get closed