import os
import shutil
import subprocess
import sys
from tkinter import *
from tkinter.ttk import *
import importlib.util
import time


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


spec = importlib.util.find_spec("PySimpleGUI")
if spec is None:
    install("PySimpleGUI")

window = Tk()

Label(window, text="Pik tis minion veela")

percent = StringVar()
folder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def start():
    countFiles = len(folder)
    for i in range(countFiles + 1):
        time.sleep(0.5)
        bar['value'] = (i / countFiles) * 100
        percent.set(str(int((i / countFiles) * 100)) + "%")
        window.update_idletasks()


bar = Progressbar(window, orient=HORIZONTAL, length=750)
bar.pack(pady=10)
percentLabel = Label(window, textvariable=percent).pack()

start()
window.mainloop()
folder = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(folder):
   file_path = os.path.join(folder, filename)
   try:
      if os.path.isfile(file_path) or os.path.islink(file_path):
         # os.unlink(file_path)
      elif os.path.isdir(file_path):
         # shutil.rmtree(file_path)
   except Exception as e:
      # sg.Popup('Ilkyen da adzmo, to sama vivo nunu muggey dia %s. Reason: %s' % (file_path, e))
# sg.Popup('Tadda tu dim kaylay bem teepus')

