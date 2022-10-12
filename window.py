from __future__ import unicode_literals
from optparse import Values
import youtube_dl

import PySimpleGUI as sg



""" BEGIN CODE """

layout = [
    [sg.Text("Youtube URL:"), sg.InputText()],
    [sg.Text("Output folder:"), sg.Input(key="vidoutput"), sg.FolderBrowse()],
    [sg.Exit(), sg.Button(button_text="Download Video",key="download")],
    ]
    
window = sg.Window("Demo", layout=layout)

def runwindow():
    while True:
        global event, values
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            print("User initiated exit, breaking..")
            break
        if event == "download":
            videodownload()

    window.close()

def videodownload():
    """    ytdl_format_options = {
        'outmpl': values[1]
        } """
    with youtube_dl.YoutubeDL() as ydl:
                ydl.download([values[0]])

def main():
    runwindow()

if __name__ == "__main__":
    main()