import tkinter as tk
import numpy as np
from tkinter import messagebox
from statistics import mode, median

# Function to roll dice using NumPy and calculate statistics
def roll_dice():
    try:
        num_dice = int(entry.get())
        if num_dice <= 0:
            raise ValueError("Number of dice must be positive.")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        return

    # Roll 'num_dice' dice using NumPy
    rolls = np.random.randint(1, 7, size=num_dice)
    
    # Calculate statistics
    mean_roll = np.mean(rolls)
    median_roll = median(rolls)
    mode_roll = mode(rolls)

    # Display the results
    result_label.config(text=f"Rolls: {rolls}")
    mean_label.config(text=f"Mean: {mean_roll:.2f}")
    median_label.config(text=f"Median: {median_roll}")
    mode_label.config(text=f"Mode: {mode_roll}")

# Create the main window
root = tk.Tk()
root.title("Dice Roll Simulator")

# Input field for the number of dice to roll
entry_label = tk.Label(root, text="Enter number of dice:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

# Button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Labels to display results
result_label = tk.Label(root, text="Rolls: ")
result_label.pack()

mean_label = tk.Label(root, text="Mean: ")
mean_label.pack()

median_label = tk.Label(root, text="Median: ")
median_label.pack()

mode_label = tk.Label(root, text="Mode: ")
mode_label.pack()

# Run the Tkinter main loop
root.mainloop()
