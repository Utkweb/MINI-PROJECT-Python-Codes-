import tkinter
import random

timeleft = 30
points = 0 
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
current_color_index = 0

def startgame(event=None):
    
    if timeleft==30:
        countdown()
    nextcolor()

def nextcolor():
    global timeleft
    global points
    global current_color_index
    
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[current_color_index].lower():
            points+=1 #points = points + 1
            feedback.config(text="Correct",fg='green')
        else:
            feedback.config(text="incorrect",fg='red')
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        current_color_index = random.randint(0,len(colors)-1)
        label.config(fg=str(colors[current_color_index]),text=colors[random.randint(0,len(colors)-1)])
        score.config(text="Score : "+str(points),font=('Georgia',15),fg='green')

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft = timeleft - 1
        time.config(text="Time Left : "+str(timeleft),fg='red',font=('Georgia',15))
        time.after(1000,countdown)
    else:
        label.config(text="Time's Up!!!!",font=('Georgia',15))
        feedback.config(text="Final Score : "+str(points),font=('Georgia',15))

root = tkinter.Tk()
root.title("Color Game")
root.geometry("375x200")

head = tkinter.Label(root,text="Word Color Game",font=('Arial',40))
head.pack()

score = tkinter.Label(root,text="Press enter to start")
score.pack()

time = tkinter.Label(root,text="Time left : "+str(timeleft))
time.pack()

label = tkinter.Label(root,font=('Georgia',40))
label.pack()

feedback = tkinter.Label(root,text="",fg="black")
feedback.pack()

e = tkinter.Entry(root)
e.pack()

e.bind('<Return>',startgame)
e.focus_set()

root.mainloop()
