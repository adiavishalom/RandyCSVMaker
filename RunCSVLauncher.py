#RunConfigWriter.py
#This file will create a page with 2 options
#One to generate EBCS Commend Board configs and one for IR829

import PySimpleGUI as sg
import os

# All the stuff inside your window.
layoutMain = [ [sg.Button('CSV Writer'), sg.Exit()]
]

# Create the Window
window = sg.Window('Config Writer', layoutMain).Finalize()

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    elif event == 'CSV Writer':
        os.system('py RandyCSVMaker.py')

window.Close()
