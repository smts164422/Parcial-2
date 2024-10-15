import PySimpleGUI as sg

#Ventana para mostrar el nombre ingresado
layout = [[sg.Text('Nombre?')],
          [sg.InputText(k='_nomb_')],
          [sg.Button('OK'), sg.Button('Cancelar')]]

window = sg.Window('Ejemplo Simple', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    nombre = str(values['_nomb_'])
    sg.popup(f'Hola {nombre}')
    print(f"Hola {nombre}")

window.close()