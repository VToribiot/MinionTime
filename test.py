import PySimpleGUI as sg

def test():
    import threading
    sg.theme('SystemDefaultForReal')
    layout = [[sg.Text('Testing progress bar:')],
              [sg.ProgressBar(max_value=10, orientation='h', size=(20, 20), key='progress_1')]]

    main_window = sg.Window('Test', layout, finalize=True)
    current_value = 0
    main_window['progress_1'].update(current_value)

    threading.Thread(target=another_function,
                     args=(main_window, ),
                     daemon=True).start()

    while True:
        window, event, values = sg.read_all_windows()
        if event == 'Exit':
            break
        if event.startswith('update_'):
            print(f'event: {event}, value: {values[event]}')
            key_to_update = event[len('update_'):]
            window[key_to_update].update(values[event])
            window.refresh()
            continue
        # process any other events ...
    window.close()

def another_function(window):
    import time
    folder = [1, 2, 3, 4, 5, 6, 7]
    countFiles = len(folder)
    for i in range(countFiles + 1):
        time.sleep(0.5)
        current_value = int((i / countFiles) * 10)
        window.write_event_value('update_progress_1', current_value)
    time.sleep(2)
    window.write_event_value('Exit', '')


test()