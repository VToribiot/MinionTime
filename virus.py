import os
import shutil
import subprocess
import sys
import importlib.util
import time
import PySimpleGUI as sg

spec = importlib.util.find_spec("PySimpleGUI")
if spec is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PySimpleGUI"])

layout = [[sg.Text('Minion Time', font="Roboto, 50")],
          [sg.Image("C:\\Users\\admin\\Downloads\\minion.png")],
          [sg.ProgressBar(10000, orientation='h', size=(20, 20), key='progressbar')]]

window = sg.Window('Minion Time').Layout(layout)
progress_bar = window.find_element('progressbar')

folder = [1, 2, 3, 4, 5, 6]
countFiles = len(folder)
prcntg = 0
for i in range(countFiles + 1):
    event, values = window.Read(timeout=1000)
    progress_bar.UpdateBar(int((i / countFiles) * 10000))
time.sleep(5)
window.Close()

folder = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            pass
            # os.unlink(file_path)
        elif os.path.isdir(file_path):
            pass
            # shutil.rmtree(file_path)
    except Exception as e:
        pass
        # sg.Popup('Ilkyen da adzmo, to sama vivo nunu muggey dia %s. Reason: %s' % (file_path, e))
# sg.Popup('Tadda tu dim kaylay bem teepus')
