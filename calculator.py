# mini-project: simple arithmetic calculator
# by Agustín Peña

# import tkinter
from tkinter import *

# initiate variables
entry = ''
x = 0.0
y = 0.0
result = 0.0

# define functions which perform the buttons actions
def num1():
    global entry
    entry += '1'
    label.config(text = entry)

def num2():
    global entry
    entry += '2'
    label.config(text = entry)

def num3():
    global entry
    entry += '3'
    label.config(text = entry)

def num4():
    global entry
    entry += '4'
    label.config(text = entry)

def num5():
    global entry
    entry += '5'
    label.config(text = entry)

def num6():
    global entry
    entry += '6'
    label.config(text = entry)

def num7():
    global entry
    entry += '7'
    label.config(text = entry)

def num8():
    global entry
    entry += '8'
    label.config(text = entry)

def num9():
    global entry
    entry += '9'
    label.config(text = entry)

def num0():
    global entry
    if entry == '':
        label.config(text = '0')
    else:
        entry += '0'
        label.config(text = entry)

def erase():
    global entry, x, y
    x = y = 0
    entry = ''
    result = 0.0
    label.config(text = '0')

def dot():
    global entry
    entry += '.'
    label.config(text = entry)

def equal():
    global entry, x, y, operation, result
    y = float(entry)
    x = float(x)
    if operation == 'add':
        result = x + y
    elif operation == 'sub':
        result = x - y
    elif operation == 'mult':
        result = x * y
    elif operation == 'div':
        result = x / y
    entry = ''
    x = y = 0
    label.config(text = str(result))

# define functions for the buttons peforming
# arithmetic operations

def add():
    global entry, x, operation
    x = entry
    entry = ''
    operation = 'add'

def sub():
    global entry, x, operation
    x = entry
    entry = ''
    operation = 'sub'

def mult():
    global entry, x, operation
    x = entry
    entry = ''
    operation = 'mult'

def div():
    global entry, x, operation
    x = entry
    entry = ''
    operation = 'div'

# start the window and define buttons and their actions
root = Tk()
label = Label(bg = 'black', fg = 'green', width = 28)
button1 = Button(text = '1', command = num1)
button2 = Button(text = '2', command = num2)
button3 = Button(text = '3', command = num3)
button4 = Button(text = '4', command = num4)
button5 = Button(text = '5', command = num5)
button6 = Button(text = '6', command = num6)
button7 = Button(text = '7', command = num7)
button8 = Button(text = '8', command = num8)
button9 = Button(text = '9', command = num9)
button0 = Button(text = '0', command = num0)
buttonDel = Button(text = 'Del', command = erase)
buttonplus = Button(text = '+', command = add)
buttonminus = Button(text = '-', command = sub)
buttonmult = Button(text = 'X', command = mult)
buttondiv = Button(text = '/', command = div)
buttondot = Button(text = '.', command = dot)
buttonequal = Button(text = '=', command = equal)
copyright = Label(text = 'Simple Calculator by Agustín Peña',
                        font = ('Times New Roman', 16, 'italic'))

# define location of widgets
label.grid(row = 0, column = 0, columnspan = 4)
buttonDel.grid(row = 1, column = 0)
buttondot.grid(row = 1, column = 1)
button0.grid(row = 1, column = 2)
buttonplus.grid(row = 1, column = 3)
button1.grid(row = 2, column = 0)
button2.grid(row = 2, column = 1)
button3.grid(row = 2, column = 2)
buttonminus.grid(row = 2, column = 3)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
buttonmult.grid(row = 3, column = 3)
button7.grid(row = 4, column = 0)
button8.grid(row = 4, column = 1)
button9.grid(row = 4, column = 2)
buttondiv.grid(row = 4, column = 3)
buttonequal.grid(row = 5, column = 3)
copyright.grid(row = 6, column = 0, columnspan = 4)

mainloop()
