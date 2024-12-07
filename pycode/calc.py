from tkinter import *

# Initialize the root window
root = Tk()
root.title("Calculator")
root.geometry('300x400')
root.resizable(False, False)


# Entry widget for displaying input/output
entry = Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)


# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14)).grid(row=row, column=col, sticky=N+S+E+W)
    elif text == '=':
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14)).grid(row=row, column=col, sticky=N+S+E+W)
    else:
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: on_button_click(t)).grid(row=row, column=col, sticky=N+S+E+W)

# Adjust grid weights for responsiveness
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
