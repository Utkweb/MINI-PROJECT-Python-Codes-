import tkinter as tk
def press1():
    image = tk.PhotoImage(file="summer.png")
    
    result.config(image = image)
    
    result.image=image
def press2():
    image = tk.PhotoImage(file="winter.png")
    
    result.config(image = image)
    
    result.image=image

root = tk.Tk()

b1 = tk.Button(root,text="Winter",command = press2)
b1.grid(row=0,column=0)

b2 = tk.Button(root,text="Summer",command= press1)
b2.grid(row=0,column=1)

result = tk.Label(root,text="")
result.grid(row=1,column=0,columnspan=2)
root.mainloop()

# you can make 5 button and with name of the 