import PySimpleGUI as sg
from io import BytesIO
import requests

def image_to_data(im):
    """
    Image object to bytes object.
    : Parameters
      im - Image object
    : Return
      bytes object.
    """
    with BytesIO() as output:
        im.save(output, format="PNG")
        data = output.getvalue()
    return data


url = "https://upload.wikimedia.org/wikipedia/commons/d/d9/Test.png"
response = requests.get(url, stream=True)
response.raw.decode_content = True
# img = ImageQt.Image.open(response.raw)
# data = image_to_data(img)
layout = [[sg.Text("Vamos a probar")],
          [sg.Image(data=response.raw.read())]]

window = sg.Window('Minion Time').Layout(layout)
while True:
    event, values = window.read()
    if event is None:
        break
window.close()