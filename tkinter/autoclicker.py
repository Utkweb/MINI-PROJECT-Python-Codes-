import tkinter as tk
from tkinter import messagebox
import pyautogui
import threading
import time

# Function to start auto-clicking
def start_clicking():
    try:
        interval = float(entry_interval.get())
        messagebox.showinfo("Auto Clicker", "Auto clicker started! Press 'Stop' to end.")
        global running
        running = True
        threading.Thread(target=auto_click, args=(interval,)).start()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the interval.")

# Function to stop auto-clicking
def stop_clicking():
    global running
    running = False
    messagebox.showinfo("Auto Clicker", "Auto clicker stopped!")

# Function to perform clicks
def auto_click(interval):
    while running:
        pyautogui.click()
        time.sleep(interval)

# Create the main window
root = tk.Tk()
root.title("Auto Clicker")

# Create and place widgets
tk.Label(root, text="Click Interval (seconds):").pack(pady=5)
entry_interval = tk.Entry(root)
entry_interval.pack(pady=5)

start_button = tk.Button(root, text="Start", command=start_clicking, bg="green", fg="white")
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_clicking, bg="red", fg="white")
stop_button.pack(pady=5)

# Initialize running flag
running = False

# Run the Tkinter event loop
root.mainloop()
