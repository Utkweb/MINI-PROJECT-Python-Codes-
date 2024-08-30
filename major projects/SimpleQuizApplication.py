import tkinter as tk
from tkinter import messagebox
# import mysql.connector

# class QuizApp:
#     def __init__(self,root):
#         self.root = root
#         self.root.title("Simple Quiz Application")

#         self.question_number = 0
#         self.score = 0
#         self.questions = []
#         self.load_questions()

#         self.question_label = tk.Label(root,text="",wraplength=400,font=("Arial",14))
#         self.question_label.pack(pady=20)

# main application
# 
root = tk.Tk() 

root.title("Quiz Manager")


label_question = tk.Label(root, text="Question", font=("Arial", 16))
label_question.grid(row=0, column=0,  pady=10,padx=10,sticky="w")
entry_question = tk.Entry(root, width=50, font=("Arial", 14))
entry_question.grid(row=0, column=1, pady=10,padx=10,sticky="w")


label_option1 = tk.Label(root, text="Option 1", font=("Arial", 16))
label_option1.grid(row=1, column=0,  pady=10,padx=10,sticky="w")
entry_option1 = tk.Entry(root, width=50, font=("Arial", 14))
entry_option1.grid(row=1, column=1, pady=10,padx=10,sticky="w")

label_option2 = tk.Label(root, text="Option 2", font=("Arial", 16))
label_option2.grid(row=2, column=0,  pady=10,padx=10,sticky="w")
entry_option2 = tk.Entry(root, width=50, font=("Arial", 14))
entry_option2.grid(row=2, column=1, pady=10,padx=10,sticky="w")

label_option3 = tk.Label(root, text="Option 3", font=("Arial", 16))
label_option3.grid(row=3, column=0,  pady=10,padx=10,sticky="w")
entry_option3 = tk.Entry(root, width=50, font=("Arial", 14))
entry_option3.grid(row=3, column=1, pady=10,padx=10,sticky="w")

label_option4 = tk.Label(root, text="Option 4", font=("Arial", 16))
label_option4.grid(row=4, column=0,  pady=10,padx=10,sticky="w")
entry_option4 = tk.Entry(root, width=50, font=("Arial", 14))
entry_option4.grid(row=4, column=1, pady=10,padx=10,sticky="w")

label_answer = tk.Label(root, text="Correct Answer (1-4): ", font=("Arial", 16))
label_answer.grid(row=5, column=0,  pady=10,padx=10,sticky="w")
entry_answer = tk.Entry(root, width=50, font=("Arial", 14))
entry_answer.grid(row=5, column=1, pady=10,padx=10,sticky="w")

add_button = tk.Button(root, text="Add Question", font=("Arial", 16))
add_button.grid(row=6, column=0, columnspan=2, pady=10,padx=10,sticky="w")

start_button = tk.Button(root, text="Start Quiz", font=("Arial", 16))
start_button.grid(row=7, column=0, columnspan=2, pady=10,padx=10,sticky="w")

root.mainloop()