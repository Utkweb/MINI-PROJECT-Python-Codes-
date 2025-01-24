import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time 
import pygame

pygame.mixer.init()      #initialize


CAROL_FILE = "carol_song.mp3"


def get_time():
    now = datetime.now()    #current time
    christmas = datetime(now.year,12,25)


    if now > christmas:
        christmas = datetime(now.year + 1,12,25)
    
    time_remaining = christmas - now
    days = time_remaining.days
    hours, remainder = divmod(time_remaining.seconds,3600)
    minutes,seconds = divmod(remainder,60)

    return days,hours,minutes,seconds

def update_countdwon():
    days,hours,minutes,seconds = get_time()
    countdown_label.config(text=f"{days} Days , {hours:02d}:{minutes:02d}:{seconds:02d}")
    root.after(1000,update_countdwon)

def play_carol():
    try:
        pygame.mixer.music.load(CAROL_FILE)
        pygame.mixer.music.play(-1)  # Play the song on a loop
    except pygame.error:
        messagebox.showerror("Error", "Unable to play the carol. Make sure the MP3 file exists.")

# Function to stop the Christmas carol
def stop_carol():
    pygame.mixer.music.stop()

def show_message():
    messagebox.showinfo("Holiday Message","Merry Christmas and Happy New Year!")



root = tk.Tk()

root.title("Christmas countdown timer")
root.geometry('500x400')
root.configure(bg="#003366")



countdown_label = tk.Label(root,text="",font=("Times New Roman",24,"bold"),fg="white",bg="#003366")
countdown_label.pack(pady=20)

play_button = tk.Button(root,text="Play Carol",font=("Times New Roman",14,"bold"),bg="#ffcc00",fg="#003366",command=play_carol)
play_button.pack(pady=10)

stop_button = tk.Button(root,text="Stop Carol",font=("Times New Roman",14,"bold"),bg="#ffcc00",fg="#003366",command=stop_carol)
stop_button.pack(pady=10)

message_button = tk.Button(root,text="Holiday Message",font=("Times New Roman",14,"bold"),bg="#ffcc00",fg="#003366",command=show_message)
message_button.pack(pady=10)

update_countdwon()

root.mainloop()

pygame.mixer.music.stop()