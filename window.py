from __future__ import unicode_literals
import youtube_dl

import PySimpleGUI as sg

#rest of the code

layout = [[sg.Text("Test Text")]]
sg.Window("Demo", layout=layout, margins=(100, 50)).read()