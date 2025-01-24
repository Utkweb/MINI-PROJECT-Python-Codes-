import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import pygame

pygame.mixer.init() #initialize


CAROL_FILE = "carol_song.mp3"


def get_time():
    now = datetime.now() #current time
    newyear = datetime(now.year,1,1)


    if now > newyear:
        newyear = datetime(now.year + 1,1,1)

    time_remaining = newyear - now
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds,3600)
    minutes,seconds = divmod(remainder,60)

    return days,hours,minutes,seconds

def update_countdown():
    days,hours,minutes,seconds = get_time()
    countdown_label.config(text=f"{days} Days , {hours:02d}:{minutes:02d}:{seconds:02d}")
    root.after(1000,update_countdown)

def play_carol():
    try:
        pygame.mixer.music.load(CAROL_FILE)
        pygame.mixer.music.play(-1) # Play the song on a loop
    except pygame.error:
        messagebox.showerror("Error", "Unable to play the carol. Make sure the MP3 file exists.")

# Function to stop the Christmas carol
def stop_carol():
    pygame.mixer.music.stop()

def show_message():
    messagebox.showinfo("Holiday Message","Merry Christmas and Happy New Year!")



root = tk.Tk()

root.title("New Year countdown timer")
root.geometry('500x400')
root.configure(bg="red")



countdown_label = tk.Label(root,text="",font=("Comic Sans MS",24,"bold"),fg="white",bg="#003366")
countdown_label.pack(pady=20)

play_button = tk.Button(root,text="Play Song",font=("Comic Sans MS",14,"bold"),bg="blue",fg="white",command=play_carol)
play_button.pack(pady=10)

stop_button = tk.Button(root,text="Stop Song",font=("Comic Sans MS",14,"bold"),bg="blue",fg="white",command=stop_carol)
stop_button.pack(pady=10)

message_button = tk.Button(root,text="New years Message",font=("Times New Roman",14,"bold"),bg="blue",fg="white",command=show_message)
message_button.pack(pady=10)

update_countdown()

root.mainloop()

pygame.mixer.music.stop()