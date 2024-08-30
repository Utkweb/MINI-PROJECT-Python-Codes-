from tkinter import *
import random
from tkinter import messagebox
import string

def gp():
    length = int(length_entry.get())
    character = string.ascii_letters

    if include_numbers.get():
        character += string.digits
    if include_symbols.get():
        character +=string.punctuation

    password = ''.join(random.choice(character) for _ in range(length))
    result_entry.delete(0,END)
    result_entry.insert(0,password)



root = Tk()
root.title('Password Generator')
root.geometry('400x300')

length_label = Label(root,text="Password length :")
length_label.pack(pady=5)

length_entry = Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0,"8")  

include_symbols = BooleanVar()
include_numbers = BooleanVar()

numbers_check = Checkbutton(root,text="Include Numbers",variable=include_numbers)
numbers_check.pack(pady=5)

numbers_symbols = Checkbutton(root,text="Include Symbols",variable=include_symbols)
numbers_symbols.pack(pady=5)

generate_button = Button(root,text="Generate Passowrd",command = gp)
generate_button.pack(pady=20)

result_entry = Entry(root,width = 50)
result_entry.pack(pady=10)

root.mainloop()

# insert(0,value)