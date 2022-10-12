from __future__ import unicode_literals
from cmath import log
import youtube_dl

import PySimpleGUI as sg

#rest of the code

layout = [
    [sg.Text("Youtube URL:"), sg.Input(key="urlinput")],
    [sg.Text("Output folder:"), sg.Input(key="vidoutput")],
    [sg.Exit(), sg.Button(button_text="Download Video",key="download")],
    ]
    
window = sg.Window("Demo", layout=layout,).read()

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        print("User initiated exit, breaking..")
        break
    if event == "download":
        sg.popup_error("Adding this")

window.close()