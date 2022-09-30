import tkinter as tk
import azureIoTManagement
import iotGeneratorGUI

def begin_sending(win):
    numOfDevices = int(win.NumDevicesIn.get())
    conStr = win.ConnStrIn.get()
    minTemp = float(win.MinTempIn.get())
    maxTemp= float(win.MaxTempIn.get())
    minHum = float(win.MinHumIn.get())
    maxHum = float(win.MaxHumIn.get())
    numMssgs = int(win.NumMssgsIn.get())
    timeMssg = float(win.TimeMssgIn.get())

    tmpRng = [minTemp,maxTemp]
    hmRng = [minHum, maxHum]
    devices = azureIoTManagement.create_devices(numOfDevices, conStr)
    threads = azureIoTManagement.send_telemetry_for_all_devices(conStr,numOfMessage=numMssgs, timeBetweenMssgs=timeMssg,tempRng=tmpRng, humRng=hmRng)
    """
    for thread in threads:
        thread.join()
    """
    azureIoTManagement.delete_devices(devices, conStr)

"""
The stop button rarely works, as the program is still loading
when data is being sent. But because it works some of the tmie
I have decided to leave the code here and if you would like to
try, simply uncomment the code (except for this text) and find
the relevent code within the 'iotGeneratorGUI.py' file, and
uncomment it. You will also need to uncomment the line
'window.StopButton.configure(command=stop_sending_data)'
within this file.
        
def stop_sending_data():
    azureIoTManagement.stop_sending()
"""

if __name__ == '__main__':
    root = tk.Tk()
    window = iotGeneratorGUI.create_Toplevel1(root)
    window.StartButton.configure(command=lambda: begin_sending(window))
    #window.StopButton.configure(command=stop_sending_data)
    connStr = "HostName=hubToConnect.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=lw8fXkx+rk8t2S/SmEPizVwmeUkI3SbQUZx1B9xAuJY="
    window.ConnStrIn.insert(0, connStr)
    root.mainloop()
