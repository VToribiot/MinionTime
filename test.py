from getpass import getpass
import PySimpleGUIQt as sg
import requests
import os

folder = os.path.dirname(os.path.abspath(__file__))
f = open(f'{folder}/minion.png', 'wb')
response = requests.get('https://qph.cf2.quoracdn.net/main-qimg-31248f5a1fd7efe4f5d9c0bd2ce18aac-pjlq')
f.write(response.content)
f.close()

layout = [[sg.Image(f'{folder}/minion.png')]]

event, (number,) = sg.Window('Enter a number example').Layout(layout).Read()

