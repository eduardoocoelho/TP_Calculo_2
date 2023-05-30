from sympy import *
import PySimpleGUI as sg


def beggining_scream():
  #Theme
  sg.theme('Dark2')
  integrals = [
               [sg.Text('Entre com a Integral:', font='arial 20', pad=(0, 0))],
               [
                 sg.Text('∫', font='arial 40', pad=(0, 0)),
                 sg.Input(size=(3, 0),
                          font='arial 8',
                          pad=(3, 0),
                          key='-UPPER-'),
                 sg.Input(size=(3, 0),
                          font='arial 8',
                          pad=(3, 0),
                          key='-LOWER-'),
                 sg.Input(size=(40, 0),
                          font='arial 15',
                          pad=(0, 0),
                          key='-FUNCTION-')
               ]
              ]

  column1 = [[sg.Text('Resolução para chegar no passo n1: ', font='arial 12')],
             [sg.Text('Resolução para chegar no passo n2: ', font='arial 12')],
             [sg.Text('Resolução para chegar no passo n3: ', font='arial 12')],
             [sg.Text('Resolução para chegar no passo n4: ', font='arial 12')],
             [sg.Text('Resultado da integral: ', font='arial 15')]]

  column2 = [[sg.Text(font='arial 13 bold', key='-STEP1-', size=(30, 1))],
             [sg.Text(font='arial 13 bold', key='-STEP2-', size=(30, 1))],
             [sg.Text(font='arial 13 bold', key='-STEP3-', size=(30, 1))],
             [sg.Text(font='arial 13 bold', key='-STEP4-', size=(30, 1))],
             [sg.Text(font='arial 15 bold', key='-OUT-', size=(30, 1))]]

  buttons = [[
    sg.Button('Calcular',
              font='arial 15',
              size=(10, 1),
              pad=((0, 15), 0),
              key='-CALCULATE-'),
    sg.CButton('Sair', font='arial 15', size=(8, 1))
  ]]

  layout = [[sg.Text('Calculadora De Integrais', font='arial 18 bold')],
            [
              sg.Column(integrals,
                        justification='center',
                        element_justification='center')
            ], [sg.Column(column1, pad=((0, 20), 0)),
                sg.Column(column2)],
            [sg.Column(buttons, justification='center')]]

  #Window
  window = sg.Window('CalculadoraDeIntegrais',
                     element_padding=(0, 10),
                     layout=layout,
                     size=(700, 500),
                     finalize=True)


#Events
beggining_scream()
while True:
  window, events, values = sg.read_all_windows()

  if events == "-CALCULATE-":
    x = Symbol('x')
    expr = apart(values['-FUNCTION-'])
    upper = values['-UPPER-']
    lower = values['-LOWER-']
    result = integrate(expr, (x, lower, upper))
    result = factor(result)
    result = str(logcombine(result.expand(), force=true)).replace("log", "ln").replace("**", "^")
    window['-OUT-'].update(result)

  if events == sg.WIN_CLOSED:
    break
