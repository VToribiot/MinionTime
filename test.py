import PySimpleGUI as sg

# layout the window
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(20, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]

# create the window`
window = sg.Window('Custom Progress Meter').Layout(layout)
progress_bar = window.find_element('progressbar')
# loop that would normally do something useful
for i in range(11):
    event, values = window.Read(timeout=1000)
    progress_bar.UpdateBar(i * 2)
window.Close()