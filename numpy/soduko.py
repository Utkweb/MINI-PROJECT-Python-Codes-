import numpy as np

# Step 1: Initialize a 9x9 Sudoku board with some pre-filled values (0 represents empty spaces)
sudoku_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# Step 2: Function to check if a number can be placed in a cell
def is_valid(board, num, row, col):
    # Check if the number is not in the current row and column
    if num in board[row, :] or num in board[:, col]:
        return False
    
    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

# Step 3: Backtracking function to solve the Sudoku puzzle
def solve_sudoku(board):
    # Loop through each cell on the board
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:  # If the cell is empty (0)
                for num in range(1, 10):  # Try numbers from 1 to 9
                    if is_valid(board, num, row, col):
                        board[row, col] = num  # Place the number
                        if solve_sudoku(board):  # Recursively try to solve the rest
                            return True
                        board[row, col] = 0  # Reset if the guess was wrong
                return False  # Trigger backtracking
    return True

# Step 4: Print the original board
print("Original Sudoku Puzzle:")
print(sudoku_board)

# Step 5: Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Puzzle:")
    print(sudoku_board)
else:
    print("No solution exists.")
