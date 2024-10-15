import PySimpleGUI as sg


#Aqui se crea el diseño de la calculadora(tamaño, posisión, estilos y colores)
layout: list = [
    [sg.Text(text='CALCULADORA BÁSICA',size=(50,3), justification='center', background_color='#272533', 
             text_color='white', font=(14))],
    [sg.Text('0.0000',size=(18,2), justification='right', background_color='black', text_color='red', 
             font=(60), relief='sunken', key="_DISPLAY_")],
    [sg.Button('C', size=(12,3), button_color='green'), sg.Button('CE', size=(12,3)), sg.Button('%', size=(12,3)), sg.Button('/', size=(12,3))],
    [sg.Button('7', size=(12,3)), sg.Button('8', size=(12,3)), sg.Button('9', size=(12,3)), sg.Button('*', size=(12,3))],
    [sg.Button('4', size=(12,3)), sg.Button('5', size=(12,3)), sg.Button('6', size=(12,3)), sg.Button('-', size=(12,3))],
    [sg.Button('1', size=(12,3)), sg.Button('2', size=(12,3)), sg.Button('3', size=(12,3)), sg.Button('+', size=(12,3))],
    [sg.Button('0', size=(12,3)), sg.Button('.', size=(12,3)), sg.Button('=', size=(25,3), bind_return_key=True)]
]

#Con la variable "window" iniciamos la ventana en la cual se mostrará la calculadora
window = sg.Window(title='Calculadora',layout=layout, size=(450,520), return_keyboard_events=True)

#La variable "var" es la cual tomará el valor en forma de cadena según el botón presionado
var: dict = {'font':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

#Función la cual transformará y devolverá el valor ingresado en formato float
    #incluyendo si son decimales o no
def format_number() -> float:

    return float(''.join(var['font']).replace(',','') + '.' + ''.join(var['back']))

#Esta función permite actualizar la pantalla según el valor ingresado o resultado obtenido
def update_display(display_value: str):

    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)

#La función number_click hecha para derterminar si el numero valor ingresado 
    # es decimal o no y actualizará la pantalla segun ello
def number_click(event: str):

    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['font'].append(event)
    update_display(format_number())

#Esta función clear_click se encargará de borrar los valores de las variables
    # entera y decimal al presionar los botones de borrado
def clear_click():

    global var
    var['font'].clear()
    var['back'].clear()
    var['decimal'] = False


#La función operator_click  se encargará de darle el valor del operador 
    # seleccionado por el usario para realizar la operación
def operator_click(event: str):

    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()


#La funcion calculate_click se ocupa para recopilar los datos proporcionados
    # y segun la operación elegida dar el resultado al momento de darle =
def calculate_click(event: str):

    global var
    try:
        var['y_val'] = format_number()
    except ValueError: 
        var['x_val'] = var['result']
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()
    except:
        update_display("ERROR! DIV/0")
        clear_click()


#Bucle de eventos
while True:
    event, values = window.read()
    print(event)

    if event == sg.WIN_CLOSED or event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        number_click(event)
    if event in ['Escape:27', 'C', 'CE']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+', '-', '*', '/']:
        operator_click(event)
    if event == '=':
        calculate_click(event)
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)
