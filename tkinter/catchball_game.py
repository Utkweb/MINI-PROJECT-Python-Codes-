import tkinter as tk
import random

class CatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball Game")
        
        # Create canvas
        self.canvas = tk.Canvas(self.root, width=400, height=600, bg='lightblue')
        self.canvas.pack()
        
        # Create the basket (player)
        self.basket = self.canvas.create_rectangle(160, 580, 240, 590, fill='brown')
        
        # Create the ball
        self.ball = self.canvas.create_oval(180, 0, 220, 20, fill='red')
        
        # Initialize variables
        self.basket_speed = 20
        self.ball_speed = 5
        self.missed_balls = 0
        self.score = 0
        
        # Display score and missed balls
        self.score_text = self.canvas.create_text(50, 20, text="Score: 0", font=('Arial', 16), fill='black')
        self.missed_text = self.canvas.create_text(350, 20, text="Missed: 0", font=('Arial', 16), fill='black')
        
        # Bind arrow keys
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        
        # Start game loop
        self.update_ball()
    
    def move_left(self, event):
        # Move basket to the left
        self.canvas.move(self.basket, -self.basket_speed, 0)
    
    def move_right(self, event):
        # Move basket to the right
        self.canvas.move(self.basket, self.basket_speed, 0)
    
    def update_ball(self):
        # Move ball down
        self.canvas.move(self.ball, 0, self.ball_speed)
        
        # Get current positions of ball and basket
        ball_pos = self.canvas.coords(self.ball)
        basket_pos = self.canvas.coords(self.basket)
        
        # Check if the ball reaches the bottom
        if ball_pos[3] >= 600:
            self.canvas.coords(self.ball, random.randint(0, 380), 0, random.randint(40, 400), 20)
            self.missed_balls += 1
            self.canvas.itemconfig(self.missed_text, text=f"Missed: {self.missed_balls}")
        
        # Check if the ball is caught by the basket
        if basket_pos[0] < ball_pos[2] < basket_pos[2] and ball_pos[3] >= basket_pos[1]:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.canvas.coords(self.ball, random.randint(0, 380), 0, random.randint(40, 400), 20)
        
        # Check if player missed too many balls
        if self.missed_balls < 3:
            self.root.after(50, self.update_ball)  # Continue game loop
        else:
            self.canvas.create_text(200, 300, text="Game Over", font=('Arial', 30), fill='red')

# Create the game window
root = tk.Tk()
game = CatchGame(root)
root.mainloop()
