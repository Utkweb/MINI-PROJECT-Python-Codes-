import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class EggCollectorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Egg Collector Game")
        self.score = 0

        # Load and display the egg image
        self.egg_image = Image.open("egg.png")
        self.egg_image = self.egg_image.resize((100, 100), Image.ANTIALIAS)
        self.egg_photo = ImageTk.PhotoImage(self.egg_image)

        # Create a label to display the score
        self.score_label = tk.Label(root, text=f"Eggs Collected: {self.score}", font=("Helvetica", 24))
        self.score_label.pack(pady=20)

        # Create an egg button to click
        self.egg_button = tk.Button(root, image=self.egg_photo, command=self.collect_egg)
        self.egg_button.pack(pady=20)

        # Create a reset button
        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 24), command=self.reset_score)
        self.reset_button.pack(pady=20)

    def collect_egg(self):
        self.score += 1
        self.score_label.config(text=f"Eggs Collected: {self.score}")
        if self.score == 10:  # Change this number for a different winning score
            messagebox.showinfo("Egg Collector Game", "Congratulations! You collected 10 eggs!")

    def reset_score(self):
        self.score = 0
        self.score_label.config(text=f"Eggs Collected: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = EggCollectorGame(root)
    root.mainloop()
