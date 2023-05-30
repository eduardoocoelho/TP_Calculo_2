from sympy import *
import PySimpleGUI as sg


def beggining_scream():
  #Theme
  sg.theme('Dark2')
  
  integrals1 = [

        [sg.Input(size=(2, 0),
                justification='center',
                enable_events=True,
                font='arial 10 bold',
                pad=(0, 30),
                key='-UPPER-')
        ],

        [sg.Input(size=(2, 0),
                    justification='center',
                    enable_events=True,
                    font='arial 10 bold',
                    pad=(0, 0),
                    key='-LOWER-')
        ]
  ]

  integrals2 = [   

        [
            sg.Text('∫', font='arial 40', pad=(0, 0)),
            sg.Input(size=(30, 0),
                    font='arial 15',
                    pad=(0, 0),
                    key='-FUNCTION-'),
          sg.Text('dx', font='arial 20', pad=(5, 0))
        ],
    ]



  buttons = [[
    sg.Button('Calcular',
              font='arial 15',
              size=(10, 1),
              pad=((0, 15), 0),
              key='-CALCULATE-'),
    sg.CButton('Sair', font='arial 15', size=(8, 1))
  ]]

  layout = [[sg.Text('Calculadora De Integrais', font='arial 18 bold')],
            [sg.Text('Entre com a Integral:', font='arial 15', pad=(0, 0))],
            [
              [sg.Column(integrals1, justification='center'),
               sg.Column(integrals2, justification='center')],
            ], 
            [sg.Text('Resultado da integral: ', font='arial 15')],
            [sg.Text(font='arial 15 bold', key='-OUT-', size=(30, 1))],
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
    break    result = str(logcombine(result.expand(), force=true)).replace("log", "ln").replace("**", "^")
    window['-OUT-'].update(result)

  if events == sg.WIN_CLOSED:
    break