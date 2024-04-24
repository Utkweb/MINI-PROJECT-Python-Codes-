import tkinter as tk 


def cel_to_fahr():
    try:
        celsius = float(e1.get())
        fahrenhiet = (celsius*9/5)+32
        
        result.config(text=f"Answer : {fahrenhiet} °F")
    except ValueError:
        result.config(text="Enter a valid number")
        
def fahr_to_cel():
    try:
        fahrenhiet = float(e1.get())
        celsius = (fahrenhiet-32)*5/9
        
        result.config(text=f"Answer : {celsius} °C")
    except ValueError:
        result.config(text="Enter a valid number")
        
        
        
root = tk.Tk()
root.title("Temperature Converter")

# create an input field
l1 = tk.Label(root,text="Temperature Conversion App",font=("Arial",20))
l1.grid(row=0,columnspan=3,padx=20,pady=20)


e1 = tk.Entry(root,width=20)
e1.grid(row=1,column=0,padx=20,pady=20)

# button to comvert the temperature
b1 = tk.Button(root,text="Convert to celsius ",fg= "white",bg="green",command=fahr_to_cel)
b1.grid(row=1,column=1,padx=20,pady=20)

b2 = tk.Button(root,text="Convert to Fahrenhiet ",fg= "white",bg="green",command=cel_to_fahr)
b2.grid(row=1,column=2,padx=20,pady=20)

result_frame = tk.Frame(root, bd=4, relief=tk.GROOVE)
result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# display our result
result = tk.Label(result_frame,text="",borderwidth=20,font=("Comic Sans MS", 20,"bold"))
result.grid(padx=20,pady=20)



root.mainloop()