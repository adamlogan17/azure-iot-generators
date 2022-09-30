from flask import Flask, redirect, url_for, render_template, request, flash
from azureIoTManagement import *

# can add template_folder='folderName' to this to use a specific folder to hold the templates
app = Flask(__name__)

@app.route("/",methods = ['GET'])
def index():
    """This function is ran when the web app is loaded"""
    try:
        connStr = request.args.get("connStr", "")
        numDevices = int(request.args.get("numDevices",""))
        tempRange = [float(request.args.get("minTemp","")), float(request.args.get("maxTemp",""))]
        humRange = [float(request.args.get("minHum","")), float(request.args.get("maxHum",""))]
        timeMssgs = float(request.args.get("timeMssgs", ""))
        numMssgs = int(request.args.get("numMssgs", ""))
    except ValueError:
        pass # this is required to 'pass' as the above code will produce an error when the page is first loaded
             # as the arguments are empty strings and can't be converted to their respective types

    # if the connection string is empty, this means that the page has just loaded and therefore the default values should be loaded in
    if connStr:
        errOccr = setUp(connStr, numDevices, tempRange, humRange, timeMssgs, numMssgs)
        # The below if statement is used to produce the correct message when the execution has finished 
        if errOccr:
            return "You have entered a incorrect connection string or you have no connection to Azure!"
        return "Messages Have Stopped Sending!"

    DEFAULTNUM = "1"
    connStr = "HostName=hubToConnect.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=lw8fXkx+rk8t2S/SmEPizVwmeUkI3SbQUZx1B9xAuJY="
    return render_template('index.html', prevConnStr=connStr, prevNumDevices=DEFAULTNUM, 
        prevMinTemp=DEFAULTNUM, prevMaxTemp="60", 
        prevMinHum=DEFAULTNUM, prevMaxHum="100", 
        prevTimeMssgs=DEFAULTNUM, prevNumMssgs=DEFAULTNUM)

def setUp(connStr, numDevices, tempRange, humRange, timeMssgs, numMssgs):
    """
    This method is used for the main logic of the program
    
    Parameters
    ----------
    connStr : str
        A connection string for an IoT Hub.
    numDevices : int
        The number of devices to be created.
    tempRange : [float, float]
        A range of the values to be created for the temperature.
        The first element is the minimum value and the second element is the maximum value.
    humRange : [float, float]
        A range of the values to be created for the humidity.
        The first element is the minimum value and the second element is the maximum value.
    timeMssgs : float
        The time between each message to send, in seconds.
    numMssgs : int
        The number of messages to send.

    Returns
    -------
    boolean
        If there are no errors False is returned but if there is an error True is returned
    """
    try:
        devices = create_devices(numDevices, connStr)
        send_telemetry_for_all_devices(connStr,numOfMessage=numMssgs, timeBetweenMssgs=timeMssgs,tempRng=tempRange, humRng=humRange)
        delete_devices(devices, connStr)
    except Exception:
        return True
    return False


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
