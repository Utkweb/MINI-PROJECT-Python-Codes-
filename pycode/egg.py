import tkinter as tk
import random
import time

class EggCatchGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Egg Catch Game")
        self.master.resizable(False, False)
        
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()

        self.basket = self.canvas.create_rectangle(180, 360, 220, 400, fill='blue')
        self.score = 0
        self.score_display = self.canvas.create_text(50, 20, text=f"Score: {self.score}", anchor='nw', font=('Arial', 14))
        
        self.eggs = []
        self.speed = 1200  # Initial speed of falling eggs in milliseconds
        self.start_time = time.time()

        self.master.bind('<Left>', self.move_left)
        self.master.bind('<Right>', self.move_right)
        
        self.spawn_eggs()

    def spawn_eggs(self):
        x = random.randint(20, 380)
        egg = self.canvas.create_oval(x, 0, x + 20, 20, fill='yellow')
        self.eggs.append(egg)
        self.move_eggs()
        self.master.after(self.speed, self.spawn_eggs)

    def move_eggs(self):
        for egg in self.eggs[:]:
            self.canvas.move(egg, 0, 10)
            if self.canvas.coords(egg)[3] >= 360:  # Check if egg reaches the basket level
                egg_x = self.canvas.coords(egg)[0]
                if egg_x >= self.canvas.coords(self.basket)[0] and egg_x <= self.canvas.coords(self.basket)[2]:
                    self.score += 1
                    self.canvas.itemconfig(self.score_display, text=f"Score: {self.score}")
                self.canvas.delete(egg)
                self.eggs.remove(egg)

        if time.time() - self.start_time > 30:  # Increase speed every 30 seconds
            self.speed -= 50
            self.start_time = time.time()

        self.master.after(50, self.move_eggs)

    def move_left(self, event):
        if self.canvas.coords(self.basket)[0] > 0:
            self.canvas.move(self.basket, -20, 0)

    def move_right(self, event):
        if self.canvas.coords(self.basket)[2] < 400:
            self.canvas.move(self.basket, 20, 0)

def main():
    root = tk.Tk()
    game = EggCatchGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
