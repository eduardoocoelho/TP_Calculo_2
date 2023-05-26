from sympy import *

#TESTE INTERFACE
#import pyautogui
#import time
#pyautogui.press('winleft')
#pyautogui.write('bloco de notas')
#pyautogui.press('enter')
#time.sleep(5)
#pyautogui.write('x = Symbol("x") f = (x) / ((x - 6)) expr = f.apart() print(integrate(expr, (x)))')

x = Symbol('x')
f = ((x - 9) / ((x + 5) * (x - 2)))
expr = f.apart()
print(integrate(expr, (x)))