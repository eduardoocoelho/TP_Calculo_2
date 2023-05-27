from sympy import *
import PySimpleGUI as sg

def beggining_scream():
    #Theme
    sg.theme('Dark2')
    integrals = [
        [sg.Text('Entre com a Integral:', font='arial 20', pad=(0, 0))],
        [sg.Input(size=(20,0), font='arial 15', pad=(0, 0), key='integral')]
    ]

    column1 = [
        [sg.Text('Resolução para chegar no passo n1: ', font='arial 12')],
        [sg.Text('Resolução para chegar no passo n2: ', font='arial 12')],
        [sg.Text('Resolução para chegar no passo n3: ', font='arial 12')],
        [sg.Text('Resolução para chegar no passo n4: ', font='arial 12')],
        [sg.Text('Resultado da integral: ', font='arial 15')]
    ]

    column2 = [
        [sg.Input(font='arial 12 bold', key='passo1', size=(30, 1))],
        [sg.Input(font='arial 12 bold', key='passo2', size=(30, 1))],
        [sg.Input(font='arial 12 bold', key='passo3', size=(30, 1))],
        [sg.Input(font='arial 12 bold', key='passo4', size=(30, 1))],
        [sg.Input(font='arial 12 bold', key='resultadoIntegral', size=(20, 1))],
    ]

    buttons = [
        [sg.Button('Calcular', font='arial 15', size=(10, 1), pad=((0, 15), 0)),
        sg.CButton('Sair', font='arial 15', size=(8, 1))]
    ]

    layout = [ 
        [sg.Text('Calculadora De Integrais', font='arial 18 bold')], 
        [sg.Column(integrals, justification='center', element_justification='center')],
        [sg.Column(column1, pad=((0, 20), 0)), 
         sg.Column(column2)],
        [sg.Column(buttons, justification='center')]
    ]

    #Window
    window = sg.Window('CalculadoraDeIntegrais', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True)

#Events
beggining_scream()
while True:
    window, events, values = sg.read_all_windows()

    if events == sg.WIN_CLOSED:
        break

#x = Symbol('x')
#f = ((x - 9) / ((x + 5) * (x - 2)))
#expr = f.apart()
#print(integrate(expr, (x)))