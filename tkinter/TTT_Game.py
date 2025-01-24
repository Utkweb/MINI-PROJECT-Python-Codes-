from tkinter import *
from tkinter import messagebox

# initialzing the board 
board = [["" for _ in range(3)]for _ in range(3)]

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0]!="":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]!="":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!= "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]!= "":
        return board[0][2]
    if all(board[row][col]!="" for row in range(3) for col in range(3)):
        return "Tie"
    return None

def ai_moves():
    best_score = -float("inf")
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row] == "":
                board[row][col] == "O"
                score = 0

                board[row][col] = ""

                if score > best_score:
                    best_score = score
                    best_move = (row,col)
    
    if best_move:
        row,col = best_move
        board[row][col] = "O"
        buttons[row][col].config(text="O",state="disabled")
        result = check_winner()
        if result:
            # functon needs to be implemet of end game 


root = Tk()
root.title('Tic Tac Toe Game')
buttons = [[None for _ in range(3)]for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(root,text="",font=('Arial',24),width=5,height=2)
        buttons[row][col].grid(row=row,column = col)


root.mainloop()
