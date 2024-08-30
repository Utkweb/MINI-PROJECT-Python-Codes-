from tkinter import *
import math

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
    
def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
        
def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def percentage():
    try:
        global expression
        total = str(eval(expression)/100)
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def square_root():
    try:
        global expression
        total = str(math.sqrt(eval(expression)))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
    
def divisible_by():
    try:
        global expression
        total = str(1/eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
if __name__ == "__main__":
    gui = Tk()
    
    gui.configure(background="light green")
    gui.title("Simple Calculator")
    gui.geometry("270x150")
    
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    
    # Creating number buttons
    b1 = Button(gui, text='1', fg="black", bg="white", command=lambda: press(1), height=1, width=7)
    b1.grid(row=2, column=0)
    b2 = Button(gui, text='2', fg="black", bg="white", command=lambda: press(2), height=1, width=7)
    b2.grid(row=2, column=1)
    b3 = Button(gui, text='3', fg="black", bg="white", command=lambda: press(3), height=1, width=7)
    b3.grid(row=2, column=2)
    b4 = Button(gui, text='4', fg="black", bg="white", command=lambda: press(4), height=1, width=7)
    b4.grid(row=3, column=0)
    b5 = Button(gui, text='5', fg="black", bg="white", command=lambda: press(5), height=1, width=7)
    b5.grid(row=3, column=1)
    b6 = Button(gui, text='6', fg="black", bg="white", command=lambda: press(6), height=1, width=7)
    b6.grid(row=3, column=2)
    b7 = Button(gui, text='7', fg="black", bg="white", command=lambda: press(7), height=1, width=7)
    b7.grid(row=4, column=0)
    b8 = Button(gui, text='8', fg="black", bg="white", command=lambda: press(8), height=1, width=7)
    b8.grid(row=4, column=1)
    b9 = Button(gui, text='9', fg="black", bg="white", command=lambda: press(9), height=1, width=7)
    b9.grid(row=4, column=2)
    b0 = Button(gui, text='0', fg="black", bg="white", command=lambda: press(0), height=1, width=7)
    b0.grid(row=5, column=0)
    
    # Creating operator buttons
    plus = Button(gui, text='+', fg="black", bg="white", command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(gui, text='-', fg="black", bg="white", command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(gui, text='*', fg="black", bg="white", command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(gui, text='/', fg="black", bg="white", command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
    equal1 = Button(gui, text='=', fg="black", bg="white", command=equal, height=1, width=7)
    equal1.grid(row=5, column=2)
    clear1 = Button(gui, text='Clear', fg="black", bg="white", command=clear, height=1, width=7)
    clear1.grid(row=5, column=1)
    decimal = Button(gui, text='.', fg="black", bg="white", command=lambda: press("."), height=1, width=7)
    decimal.grid(row=6, column=0)
    
    gui.mainloop()
