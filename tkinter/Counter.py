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


# color = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"

# red = 255 green = 87 blue = 51

# #ff5733