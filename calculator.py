'''
A working calculator with addition, subtraction, multiplication and division.
Maksym Pronin, July 22-23, 2025
'''

import tkinter as tk
from functools import partial

# puts whatever button you press into the text field
def buttonpress(value):
    field.insert(tk.END, value)

# clears the text field
def clearerror():
    field.delete(0, tk.END)

# does the math, shows result or error
def equals():
    try:
        answer = eval(field.get())
        field.delete(0, tk.END)
        field.insert(0, answer)
    except:
        field.delete(0, tk.END)
        field.insert(0, "Error")
        field.after(1000, clearerror)

# main window
window = tk.Tk()
window.title("Calculator")

# input/output field
field = tk.Entry(window, width=20, font=("Arial", 20))
field.grid(row=0, column=0, columnspan=4)

# number buttons 1-9
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
row = 1
col = 0
for i in numbers:
    button = tk.Button(window, text=i, width=6, height=2, command=partial(buttonpress, i))
    button.grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

# operator buttons
plus = tk.Button(window, text="+", width=6, height=2, command=partial(buttonpress, "+"))
minus = tk.Button(window, text="-", width=6, height=2, command=partial(buttonpress, "-"))
multiply = tk.Button(window, text="*", width=6, height=2, command=partial(buttonpress, "*"))
divide = tk.Button(window, text="/", width=6, height=2, command=partial(buttonpress, "/"))

# equals button
equal = tk.Button(window, text="=", width=6, height=2, command=partial(equals))

# clear button
clear = tk.Button(window, text="Clear", width=6, height=2, command=partial(field.delete, 0, tk.END))

# placing buttons
plus.grid(row=1, column=3)
minus.grid(row=2, column=3)
multiply.grid(row=3, column=3)
divide.grid(row=4, column=3)
equal.grid(row=5, column=3)
clear.grid(row=4, column=0, columnspan=3, rowspan=2, sticky="we")

# keeps the window running
window.mainloop()