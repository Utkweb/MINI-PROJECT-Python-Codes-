import tkinter as tk

def click():
    global counter
    counter=counter+1
    label.config(text=f"Clicks :{counter}")
    
counter = 0

root = tk.Tk()
root.title("Counter")


label = tk.Label(root,text="Clicks: 0")
label.pack()

button = tk.Button(root,text="Click me!",command=click)
button.pack()

root.mainloop()