# Python :

# 1. Multipurpose programming 
# 2. easy to learn
# 3. interpreted programming language 
# 4. Expressive Language 

# Vaiables - It stores up a value in a character or a word


# Data Types : - It defines of which type the data is : 

# 1. Integer (int) - it stores up values without decimal. eg - 1,5,8,-5,7,0,etc
# 2. Float (float) - it stores up values with decimals . eg - 1.5,-1.9969,0.57,etc
# 3. String (str) - It stores up values like words or sentences. eg - "will","Utkarsh","Welcome to the first class!!!!"
# 4. Boolean (bool) - it stores up True, False, 1,0

# type() - this function helps you to know of which type the data is 

# a = False
# print(type(a))

# name = "Will"
# print("Hi what's up ?",name)


# My first name is Will
# My last name is Wijekoon

# comments : - it is used to write a note or a message in the code. It is not executed by the compiler or interpreter

# I'm trying to print my first name
 
# print("My first name is Will")


# a = 10 (integer -> int)
# b = 10.5 (float -> float)
# c = "Will" (string -> str)
# d = True (boolean -> bool)

# a = "10.5"

# print(type(a))

# operators: - It is used to perform operations on variables and values

# 1. Arithmetic Operators : - It is used to perform mathematical operations

# a. Addition (+) - it is used to add two values
# b. Subtraction (-) - it is used to subtract two values
# c. Multiplication (*) - it is used to multiply two values
# d. Division (/) - it is used to divide two values
# e. Modulus (%) - it is used to find the remainder of the division
# f. Exponentiation (**) - it is used to raise a number to the power of another number
# g. Floor Division (//) - it is used to divide and return the integer value of the result/


# a = 10
# b = 15

# print("Addition of a & b is : ",a+b)



# % => remainder of the division 
# // => in terms of whole number
# / => it means we get the answer in terms of decimal numbers

# Conditional Statements : 

# We are having 3 types of conditional statements in python :

# 1. if statement - It is used to check a condition and execute a block of code if the condition is True

# syntax:

# if condition:
#     # block of code

# age = 17
# if age>18:
#     print("You are an adult")

# 2. if else statement - 

# syntax:

# if conditions:
    # block of code
# else:
    # block of code


# age = 17
# if age>18:
#     print("You are an adult")
# else:
#     print("You are a kid")

# You have to take to values and check which one is greater.

# 3. if elif else statements


# syntax:


# if condition:
    # block of code
# elif condition:
    # block of code
# else:
    # block of code

# num = 0
# if num > 0:
#     print("Positive Number")
# elif num < 0:
#     print("Negative Number")
# else:
#     print("Zero")


# age = 18
# if age>18:
#     print("You are an adult")
# elif age == 18:
#     print("You are a teenager")
# else:
#     print("You are a kid")


# Loops :

# Two type of loops in python :

# 1. for loop

# syntax:

# for variable_name in range(start,end,step):
    # block of code

# for number5 in range(1,1001,1):
#     print(number5,". Will")


# 2. while loop


# print("Will")
# print("Will")
# print("Will")
# print("Will")
# print("Will")
# print("Will")
# print("Will")
# print("Will")
# print("Will")
# print("Will")

# 5 10 15 20 25 30 35 40 45 50

# for number8 in range(5,51,5):
#     print(number8)


# 10 20 30 40 50 60 70 80 90 100

# 10 9 8 7 6 5 4 3 2 1

# 1 2 3 4 5 6 7 8 9 10 = 55

# for i in range(1,11):
#     print(i+1)


# 1+2+3+4+5+6+7+8+9+10 = 55
# 1 - 50 = 

# count = 0
# for i in range(1,51):
#     if i%2 == 0:
#         count = count + 1

# print("The even number total count is :",count)

# 1 - 150 

# you need to add all the even numbers from 1 - 150



# random module

# import random 


# num = random.randint(1,15)

# print(num)

# import random

# print("Welcome to the Number Guessing Game 🔢")
# print("You need to guess the number between 1 to 30 in 5 chances")


# secret_number = random.randint(1,30)

# max_attempts = 5
# attempts = 0

# while attempts < 5 :
#     guess = int(input("Guess the number : "))
#     attempts = attempts + 1


#     if guess == secret_number:
#         print("Congratulations, You've won the game in",attempts,"attempts.")
#         break
#     elif guess > secret_number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low")


# if attempts == max_attempts:
#     print("Game Over!!! The secret number is",secret_number)


# either our starting point is not fixed or ending point


# while condition:
#     statements

# 1 - 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i+1

# 10 11 12 13 14 15 16 17 18 19 20

# 10 9 8 7 6 5 4 3 2 1 0

# 5 10 15 20 25 30 35 40 45 50


# boolean,float,string,int


# new data types:

# 1. List - It stores multiple items in it.
# It is being enclosed by []
# It allows duplicate values

# example:

# addition = [1,2,3,4,5,6,7,8]
# l1 = [1.0,2.0,5.0,6.0,4.8]
# l2 = ["Will","Utkarsh","Max","Aryan"]
# l3 = [True,False,False]

# l4 = ["Will",11,24.87,True]

# num = [51,48,97,5,6,7,2]

# print(num[-2])


# indexes - are the identity of the numbers to access them
# positive indexing starts from 0 to n
# negative indexing starts from -1 to n

# num = [51,48,97,5,6,7,2]
# print(num[1:5])

# Given the list 
# colors = ['red', 'green', 'blue', 'yellow', 'purple']
# what is the output of 
# print(colors[1:4])


# Given the list 
# animals = ['cat', 'dog', 'elephant', 'giraffe', 'lion'],
# what is the output of animals[-4:-1]?


# Given the list 
# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 
# what is the output of students[1:-1]?

# students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'] 
# print(students[::-1])


# num = [14,94,66,29,21,37]
# for i in num:
#     print(i)



# add all elements
# count of how many even and how many odd numbers are there in the list?


# 2. Tuple
# 3. set
# 4. Dictionary


# import random 

# def user_choice():
#     user_choice = input("Enter your choice (Rock,Paper,Scissors) : ")
#     while user_choice not in ['Rock','Paper','Scissors']:
#         print("Invalid input Try Again!")
#         user_choice = input("Enter your choice (Rock,Paper,Scissors) : ")
#     return user_choice

# def computer_choice():
#     choices = ['Rock','Paper','Scissors']
#     return random.choice(choices)


# def determine_winner(user_choice,computer_choice):
#     if user_choice == computer_choice:
#         return "It's a Tie!"
#     elif (user_choice == 'Rock' and computer_choice == 'Scissor') or \
#     (user_choice == 'Scissor' and computer_choice == 'Paper') or \
#     (user_choice == 'Paper' and computer_choice == 'Rock'):
#         return "User Wins 😎"
#     else:
#         return "Computer Wins 💻"

# print("Welcome to the Rock, Paper and Scissors Game!")
# user_score = 0 
# computer_score = 0

# while True:
#     user = user_choice()
#     computer = computer_choice()

#     print(f"Computer Choice : {computer}")

#     result = determine_winner(user,computer)

#     if result == "User Wins 😎":
#         user_score = user_score + 1
#     elif result == "Computer Wins 💻":
#         computer_score = computer_score +1
    
#     print(f"Score:    User: {user_score}   ||      Computer : {computer_score}")

#     play_again = input("Do you want to play the game again> (yes/no)").lower()
#     if play_again!='yes':
#         break

# print("Thanks for playing the game")

# print(f"Final Score:    User: {user_score}   ||      Computer : {computer_score}")

# List is Mutable 

# We are gonna learn how to add the elements and delete them 

# Adding the elements into the list 

# there are two ways how we can add the elements 

# 1. append() - It adds the element at the last of the list.

# names = ["Will","Sharon","Timmy","Jack"]

# names.append("Jimmy")
# print(names)

# 2. insert() -  It also adds the elements into the list but at the desired position 

# names = ["Will","Sharon","Timmy","Jack"]

# names.insert(2,"Jimmy")
# print(names)


# delete elements 

# 1. remove() - it delete the element in the bracket whatever you are writing 


# names = ["Will","Sharon","Timmy","Jack"]

# names.remove("Sharon")
# print(names)

# 2. pop()

# names = ["Will","Sharon","Timmy","Jack"]

# names.pop(2)
# print(names)






# l1 = [1,2,5,6,8,9,3,2,1,4,5,6,8,0]

# new = []

# for i in l1:
#     if i not in new:
#         new.append(i)

# print(new)


from tkinter import *


root = Tk()
root.title("Calculator")
root.geometry('300x400')
root.resizable(False, False)


def on_button_click(value):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,current+value)

def clear():
    entry.delete(0,END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,str(result))
    except Exception:
        entry.delete(0,END)
        entry.insert(0,"Error")


entry = Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)


# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14),command=clear).grid(row=row, column=col, sticky=N+S+E+W)
    elif text == '=':
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14),command=calculate).grid(row=row, column=col, sticky=N+S+E+W)
    else:
        Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: on_button_click(t)).grid(row=row, column=col, sticky=N+S+E+W)


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
