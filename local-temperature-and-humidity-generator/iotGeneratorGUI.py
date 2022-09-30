import tkinter as tk

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    print("hello")
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    rt = root
    top = Toplevel1 (root)
    return top

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        default = "-family {Segoe UI} -size 8 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("426x423+748+176")
        top.title("Azure Device and Data Generator")
        top.configure(background="#d9d9d9")

        """
        The stop button rarely works, as the program is still loading
        when data is being sent. But because it works some of the tmie
        I have decided to leave the code here and if you would like to
        try, simply uncomment the code (except for this text) and find
        the relevent code within the 'main.py' file, and uncomment it.
        
        self.StopButton = tk.Button(top)
        self.StopButton.place(relx=0.845, rely=0.922, height=24, width=47)
        self.StopButton.configure(activebackground="#ececec")
        self.StopButton.configure(activeforeground="#000000")
        self.StopButton.configure(background="#d9d9d9")
        self.StopButton.configure(disabledforeground="#a3a3a3")
        self.StopButton.configure(foreground="#000000")
        self.StopButton.configure(highlightbackground="#d9d9d9")
        self.StopButton.configure(highlightcolor="black")
        self.StopButton.configure(pady="0")
        self.StopButton.configure(text='''Stop''')
        """

        self.StartButton = tk.Button(top)
        self.StartButton.place(relx=0.423, rely=0.922, height=24, width=47)
        self.StartButton.configure(activebackground="#ececec")
        self.StartButton.configure(activeforeground="#000000")
        self.StartButton.configure(background="#d9d9d9")
        self.StartButton.configure(disabledforeground="#a3a3a3")
        self.StartButton.configure(foreground="#000000")
        self.StartButton.configure(highlightbackground="#d9d9d9")
        self.StartButton.configure(highlightcolor="black")
        self.StartButton.configure(pady="0")
        self.StartButton.configure(text='''Start''')

        self.EnteredData = tk.Frame(top)
        self.EnteredData.place(relx=0.0, rely=0.142, relheight=0.768
                , relwidth=0.998)
        self.EnteredData.configure(relief='groove')
        self.EnteredData.configure(borderwidth="0")
        self.EnteredData.configure(relief="groove")
        self.EnteredData.configure(background="#d9d9d9")

        self.NumDevicesIn = tk.Spinbox(self.EnteredData, from_=1.0, to=100.0)
        self.NumDevicesIn.place(relx=0.471, rely=0.138, relheight=0.065
                , relwidth=0.504)
        self.NumDevicesIn.configure(activebackground="#f9f9f9")
        self.NumDevicesIn.configure(background="white")
        self.NumDevicesIn.configure(buttonbackground="#d9d9d9")
        self.NumDevicesIn.configure(disabledforeground="#a3a3a3")
        self.NumDevicesIn.configure(font="TkDefaultFont")
        self.NumDevicesIn.configure(foreground="black")
        self.NumDevicesIn.configure(highlightbackground="black")
        self.NumDevicesIn.configure(highlightcolor="black")
        self.NumDevicesIn.configure(insertbackground="black")
        self.NumDevicesIn.configure(selectbackground="#c4c4c4")
        self.NumDevicesIn.configure(selectforeground="black")

        self.DeviceLabel = tk.Label(self.EnteredData)
        self.DeviceLabel.place(relx=0.024, rely=0.138, height=21, width=134)
        self.DeviceLabel.configure(background="#d9d9d9")
        self.DeviceLabel.configure(disabledforeground="#a3a3a3")
        self.DeviceLabel.configure(foreground="#000000")
        self.DeviceLabel.configure(font=default)
        self.DeviceLabel.configure(text='''Devices to be Created:''')

        self.MssgLabel = tk.Label(self.EnteredData)
        self.MssgLabel.place(relx=0.024, rely=0.708, height=21, width=144)
        self.MssgLabel.configure(background="#d9d9d9")
        self.MssgLabel.configure(disabledforeground="#a3a3a3")
        self.MssgLabel.configure(foreground="#000000")
        self.MssgLabel.configure(font=default)
        self.MssgLabel.configure(text='''Time Between Messages:''')

        self.NumOfMssgLabel = tk.Label(self.EnteredData)
        self.NumOfMssgLabel.place(relx=0.024, rely=0.862, height=21, width=187)
        self.NumOfMssgLabel.configure(background="#d9d9d9")
        self.NumOfMssgLabel.configure(disabledforeground="#a3a3a3")
        self.NumOfMssgLabel.configure(foreground="#000000")
        self.NumOfMssgLabel.configure(font=default)
        self.NumOfMssgLabel.configure(text='''Number of Messages to be Sent:''')

        self.ConnStrLabel = tk.Label(self.EnteredData)
        self.ConnStrLabel.place(relx=0.035, rely=0.046, height=21, width=164)
        self.ConnStrLabel.configure(background="#d9d9d9")
        self.ConnStrLabel.configure(disabledforeground="#a3a3a3")
        self.ConnStrLabel.configure(foreground="#000000")
        self.ConnStrLabel.configure(font=default)
        self.ConnStrLabel.configure(text='''Connection String for IoT Hub:''')

        self.ConnStrIn = tk.Entry(self.EnteredData)
        self.ConnStrIn.place(relx=0.471, rely=0.046,height=21, relwidth=0.504)
        self.ConnStrIn.configure(background="white")
        self.ConnStrIn.configure(disabledforeground="#a3a3a3")
        self.ConnStrIn.configure(font="TkFixedFont")
        self.ConnStrIn.configure(foreground="#000000")
        self.ConnStrIn.configure(insertbackground="black")

        self.TempFrame = tk.Frame(self.EnteredData)
        self.TempFrame.place(relx=0.0, rely=0.215, relheight=0.231
                , relwidth=0.976)
        self.TempFrame.configure(relief='groove')
        self.TempFrame.configure(borderwidth="0")
        self.TempFrame.configure(relief="groove")
        self.TempFrame.configure(background="#d9d9d9")

        self.TempLabel = tk.Label(self.TempFrame)
        self.TempLabel.place(relx=0.024, rely=0.133, height=21, width=112)
        self.TempLabel.configure(background="#d9d9d9")
        self.TempLabel.configure(disabledforeground="#a3a3a3")
        self.TempLabel.configure(foreground="#000000")
        self.TempLabel.configure(font=default)
        self.TempLabel.configure(text='''Temperature Range:''')

        self.MinTempLabel = tk.Label(self.TempFrame)
        self.MinTempLabel.place(relx=0.048, rely=0.533, height=21, width=114)
        self.MinTempLabel.configure(background="#d9d9d9")
        self.MinTempLabel.configure(disabledforeground="#a3a3a3")
        self.MinTempLabel.configure(foreground="#000000")
        self.MinTempLabel.configure(font=default)
        self.MinTempLabel.configure(text='''Minimum Value:''')

        self.MinTempIn = tk.Spinbox(self.TempFrame, from_=1.0, to=100.0)
        self.MinTempIn.place(relx=0.313, rely=0.533, relheight=0.28
                , relwidth=0.181)
        self.MinTempIn.configure(activebackground="#f9f9f9")
        self.MinTempIn.configure(background="white")
        self.MinTempIn.configure(buttonbackground="#d9d9d9")
        self.MinTempIn.configure(disabledforeground="#a3a3a3")
        self.MinTempIn.configure(font="TkDefaultFont")
        self.MinTempIn.configure(foreground="black")
        self.MinTempIn.configure(highlightbackground="black")
        self.MinTempIn.configure(highlightcolor="black")
        self.MinTempIn.configure(insertbackground="black")
        self.MinTempIn.configure(selectbackground="#c4c4c4")
        self.MinTempIn.configure(selectforeground="black")

        self.MaxTempLabel = tk.Label(self.TempFrame)
        self.MaxTempLabel.place(relx=0.53, rely=0.533, height=21, width=96)
        self.MaxTempLabel.configure(background="#d9d9d9")
        self.MaxTempLabel.configure(disabledforeground="#a3a3a3")
        self.MaxTempLabel.configure(foreground="#000000")
        self.MaxTempLabel.configure(font=default)
        self.MaxTempLabel.configure(text='''Maximum Value:''')

        self.MaxTempIn = tk.Spinbox(self.TempFrame, from_=1.0, to=100.0)
        self.MaxTempIn.place(relx=0.783, rely=0.533, relheight=0.28
                , relwidth=0.181)
        self.MaxTempIn.configure(activebackground="#f9f9f9")
        self.MaxTempIn.configure(background="white")
        self.MaxTempIn.configure(buttonbackground="#d9d9d9")
        self.MaxTempIn.configure(disabledforeground="#a3a3a3")
        self.MaxTempIn.configure(font="TkDefaultFont")
        self.MaxTempIn.configure(foreground="black")
        self.MaxTempIn.configure(highlightbackground="black")
        self.MaxTempIn.configure(highlightcolor="black")
        self.MaxTempIn.configure(insertbackground="black")
        self.MaxTempIn.configure(selectbackground="#c4c4c4")
        self.MaxTempIn.configure(selectforeground="black")

        self.HumFrame = tk.Frame(self.EnteredData)
        self.HumFrame.place(relx=0.0, rely=0.431, relheight=0.231
                , relwidth=0.976)
        self.HumFrame.configure(relief='groove')
        self.HumFrame.configure(borderwidth="0")
        self.HumFrame.configure(relief="groove")
        self.HumFrame.configure(background="#d9d9d9")
        self.HumFrame.configure(highlightbackground="#d9d9d9")
        self.HumFrame.configure(highlightcolor="black")

        self.HumLabel = tk.Label(self.HumFrame)
        self.HumLabel.place(relx=0.024, rely=0.133, height=21, width=95)
        self.HumLabel.configure(activebackground="#f9f9f9")
        self.HumLabel.configure(activeforeground="black")
        self.HumLabel.configure(background="#d9d9d9")
        self.HumLabel.configure(disabledforeground="#a3a3a3")
        self.HumLabel.configure(foreground="#000000")
        self.HumLabel.configure(highlightbackground="#d9d9d9")
        self.HumLabel.configure(highlightcolor="black")
        self.HumLabel.configure(font=default)
        self.HumLabel.configure(text='''Humidity Range:''')

        self.MinHumLabel = tk.Label(self.HumFrame)
        self.MinHumLabel.place(relx=0.048, rely=0.533, height=21, width=114)
        self.MinHumLabel.configure(activebackground="#f9f9f9")
        self.MinHumLabel.configure(activeforeground="black")
        self.MinHumLabel.configure(background="#d9d9d9")
        self.MinHumLabel.configure(disabledforeground="#a3a3a3")
        self.MinHumLabel.configure(foreground="#000000")
        self.MinHumLabel.configure(highlightbackground="#d9d9d9")
        self.MinHumLabel.configure(highlightcolor="black")
        self.MinHumLabel.configure(font=default)
        self.MinHumLabel.configure(text='''Minimum Value:''')

        self.MinHumIn = tk.Spinbox(self.HumFrame, from_=1.0, to=100.0)
        self.MinHumIn.place(relx=0.313, rely=0.533, relheight=0.28
                , relwidth=0.181)
        self.MinHumIn.configure(activebackground="#f9f9f9")
        self.MinHumIn.configure(background="white")
        self.MinHumIn.configure(buttonbackground="#d9d9d9")
        self.MinHumIn.configure(disabledforeground="#a3a3a3")
        self.MinHumIn.configure(font="TkDefaultFont")
        self.MinHumIn.configure(foreground="black")
        self.MinHumIn.configure(highlightbackground="black")
        self.MinHumIn.configure(highlightcolor="black")
        self.MinHumIn.configure(insertbackground="black")
        self.MinHumIn.configure(selectbackground="#c4c4c4")
        self.MinHumIn.configure(selectforeground="black")

        self.MaxHumLabel = tk.Label(self.HumFrame)
        self.MaxHumLabel.place(relx=0.53, rely=0.533, height=21, width=96)
        self.MaxHumLabel.configure(activebackground="#f9f9f9")
        self.MaxHumLabel.configure(activeforeground="black")
        self.MaxHumLabel.configure(background="#d9d9d9")
        self.MaxHumLabel.configure(disabledforeground="#a3a3a3")
        self.MaxHumLabel.configure(foreground="#000000")
        self.MaxHumLabel.configure(highlightbackground="#d9d9d9")
        self.MaxHumLabel.configure(highlightcolor="black")
        self.MaxHumLabel.configure(font=default)
        self.MaxHumLabel.configure(text='''Maximum Value:''')

        self.MaxHumIn = tk.Spinbox(self.HumFrame, from_=1.0, to=100.0)
        self.MaxHumIn.place(relx=0.783, rely=0.533, relheight=0.28
                , relwidth=0.181)
        self.MaxHumIn.configure(activebackground="#f9f9f9")
        self.MaxHumIn.configure(background="white")
        self.MaxHumIn.configure(buttonbackground="#d9d9d9")
        self.MaxHumIn.configure(disabledforeground="#a3a3a3")
        self.MaxHumIn.configure(font="TkDefaultFont")
        self.MaxHumIn.configure(foreground="black")
        self.MaxHumIn.configure(highlightbackground="black")
        self.MaxHumIn.configure(highlightcolor="black")
        self.MaxHumIn.configure(insertbackground="black")
        self.MaxHumIn.configure(selectbackground="#c4c4c4")
        self.MaxHumIn.configure(selectforeground="black")

        self.TimeMssgIn = tk.Spinbox(self.EnteredData, from_=1.0, to=100.0)
        self.TimeMssgIn.place(relx=0.471, rely=0.708, relheight=0.065
                , relwidth=0.504)
        self.TimeMssgIn.configure(activebackground="#f9f9f9")
        self.TimeMssgIn.configure(background="white")
        self.TimeMssgIn.configure(buttonbackground="#d9d9d9")
        self.TimeMssgIn.configure(disabledforeground="#a3a3a3")
        self.TimeMssgIn.configure(font="TkDefaultFont")
        self.TimeMssgIn.configure(foreground="black")
        self.TimeMssgIn.configure(highlightbackground="black")
        self.TimeMssgIn.configure(highlightcolor="black")
        self.TimeMssgIn.configure(insertbackground="black")
        self.TimeMssgIn.configure(selectbackground="#c4c4c4")
        self.TimeMssgIn.configure(selectforeground="black")

        self.NumMssgsIn = tk.Spinbox(self.EnteredData, from_=1.0, to=100.0)
        self.NumMssgsIn.place(relx=0.471, rely=0.862, relheight=0.065
                , relwidth=0.504)
        self.NumMssgsIn.configure(activebackground="#f9f9f9")
        self.NumMssgsIn.configure(background="white")
        self.NumMssgsIn.configure(buttonbackground="#d9d9d9")
        self.NumMssgsIn.configure(disabledforeground="#a3a3a3")
        self.NumMssgsIn.configure(font="TkDefaultFont")
        self.NumMssgsIn.configure(foreground="black")
        self.NumMssgsIn.configure(highlightbackground="black")
        self.NumMssgsIn.configure(highlightcolor="black")
        self.NumMssgsIn.configure(insertbackground="black")
        self.NumMssgsIn.configure(selectbackground="#c4c4c4")
        self.NumMssgsIn.configure(selectforeground="black")

        self.Title = tk.Label(top)
        self.Title.place(relx=0.0, rely=0.024, height=41, width=424)
        self.Title.configure(background="#d9d9d9")
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(font=font9)
        self.Title.configure(foreground="#000000")
        self.Title.configure(text='''Azure Device and Data Generator''')

if __name__ == '__main__':
    vp_start_gui()
