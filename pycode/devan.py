# print("Hello World!, I'm going to learn python from now")

# variables - a,b

# data types - int
#                 float
#                 string
#                 boolean



# a = 4 
# b = 5

# print(a+b)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))


# String formatting
# print("Summation of two numbers are :",(a+b))


# name = input("Enter your name: ")
# standard = input("Enter your class: ")
# age = input("Enter your age: ")


# My name is Devan and I am 20 years old, and i study in 12th standard


# + 
# -
# *
# /
# //
# %
# **

# print(6**2)

# P - PARANTHESIS({})
# E - EXPONENT
# M - MULTIPLICATION
# D - DIVISION
# A - ADDITION
# S - SUBTRACTION




# a = int(input("Enter a number :"))
# b = int(input("Enter a number :"))

# print(a+b)


# conditional statements -

# if statements
# if-else statements
# if-elif-else statements


# if-statement 

# if(condition):
#     statements

# age = int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")




# if- else statements

# if(condition):
#     statements
# else:
#     statements


# if-elif-else statements

# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements



# num = int(input("Enter a number: "))
# if(num%2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")
    
    
# loops: for loop, while loop
# for variable in range(start,stop,step):
#     statements

# for i in range(1,11):
#     print(i,end =" ")



# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
# 8 * 10 = 80


# num = int(input("Enter the number of which you want the table of : "))
# for i in range(1,21):
#     print(num,"X",i,"=",num*i)

# for loop -> if else statements


# even_count = 0
# odd_count = 0
# for i in range(1,11):
#     if(i%2==0):
#         even_count+=1
#     else:
#         odd_count+=1
# print("Even numbers are :",even_count)
# print("Odd numbers are :",odd_count)



# while loop

# while condition:
#     statements

# i = 15
# while i>-20:
#     print(i,end =" ")
#     i=i-1


# import turtle

# sk = turtle.Turtle()

# for i in range(4):
#     sk.forward(100)
#     sk.right(90)


# import turtle
# star = turtle.Turtle()


# star.right(75)
# star.forward(100)

# for i in range(4):
#     star.right(144)
#     star.forward(100)

# turtle.done()

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("black")

# pen = turtle.Turtle()
# pen.speed(0)

# pen.fillcolor("white")
# pen.begin_fill()

# pen.circle(100)

# pen.end_fill()
# pen.hideturtle()

# turtle.done()

# import turtle


# t = turtle.Turtle()


# t.fillcolor("cyan")


# t.begin_fill()


# for _ in range(5):
#     t.forward(200)
#     t.right(288)


# t.end_fill()


# t.hideturtle()





# import turtle


# turtle.forward(200)

# turtle.left(90)

# turtle.forward(100)

# turtle.left(90)

# turtle.forward(200)

# turtle.left(90)
# turtle.forward(100)




# turtle.mainloop()



# import turtle

# turtle.forward(100)

# turtle.left(120)

# turtle.forward(100)

# turtle.left(120)

# turtle.forward(100)

# turtle.mainloop()
# import turtle

# turtle.seth(0)
# turtle.forward(80)
# turtle.write("East")
# turtle.home()

# turtle.setheading(90)
# turtle.forward(80)
# turtle.write("North")
# turtle.home()

# turtle.seth(180)
# turtle.forward(80)
# turtle.write("West", align="right")
# turtle.home()

# turtle.setheading(270)
# turtle.forward(80)
# turtle.write("South")
# turtle.ht()




# import turtle

# turtle.forward(150)
# turtle.right(90)
# turtle.forward(80)
# turtle.right(90)
# turtle.forward(150)
# turtle.right(90)
# turtle.forward(80)


# turtle.mailoop()


# import turtle 

# t = turtle.Turtle()


# t.speed(1)

# for _ in range(2):
#     t.forward(200)
#     t.left(120)
# t.forward(200)


# turtle.done()


# import turtle

# # Create a turtle object
# t = turtle.Turtle()

# # Draw the obtuse triangle
# side_length = 100
# angle = 120  # Angle for an obtuse triangle
# t.forward(side_length)  # Draw the first side
# t.left(angle)  # Turn left
# t.forward(side_length)  # Draw the second side
# t.left(angle)  # Turn left
# t.forward(side_length)  # Draw the third side

# # Close the turtle graphics window
# turtle.done()




# import random 

# def user_choice():
#     user = input("Enter your choice between ('rock','paper','scissor') : ").lower()
#     while user not in ['rock','paper','scissor']:
#         print("Invalid choice")
#         user = input("Enter your choice between ('rock','paper','scissor') : ").lower()
#     return user
    
# def bot_choice():
#     return random.choice(['rock','paper','scissor'])

# def winner(user_choice,bot_choice):
#     if user_choice == bot_choice:
#         return "It's a TIE"
#     elif (user_choice == 'rock' and bot_choice == 'scissor') or \
#         (user_choice == 'scissor' and bot_choice == 'paper') or \
#         (user_choice == 'paper' and bot_choice == 'rock'):
#             return "User wins"
#     else:
#         return "Bot wins"

# def play_game():
#     print("Welcome to the Rock Paper and Scissor Game!!!!!!!!")
#     while True:
#         user = user_choice()
#         bot = bot_choice()
        
#         print(f"User Choice : {user}")
#         print(f"Bot Choice : {bot}")
#         print(winner(user,bot))
#         play = input("do you wanna play the game again? (yes/no) : ").lower()
#         if play!='yes':
#             print("Thanks for playing up the game")
#             break
        
# play_game()


# Function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Get the interval from the user
# start = int(input("Enter the start of the interval: "))
# end = int(input("Enter the end of the interval: "))

# print(f"Prime numbers between {start} and {end} are:")

# for num in range(start, end + 1):
#     if is_prime(num):
#         print(num)


# We are going to be learn about some data types in python


# List : List is a collection of items in a particular order. It is mutable and it is represented by square brackets []


# l1 = [1,2,3,4,5,6,7,8,9,10]
# print(l1)

# l1 = ['Will','Devan','John','Mike','Tom','Jerry','Harry','Sam','Dean','Castiel']
# l2 = [1,2,3,4,5,6,7,8,9,10]
# l3 = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.10]
# l4 = [True,False,True,False,True,False,True,False,True,False]
# l5 = ['Will',1,2.2,True]


# lst = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# print(lst[10])


# Basic Access:

# 1. Given the list my_list = [10, 20, 30, 40, 50], what is the output of my_list[2]?  # 30
# 2. Given the list fruits = ['apple', 'banana', 'cherry', 'date'], what is the output of fruits[0]? # apple

# Negative Indexing:

# 1. For the list numbers = [5, 10, 15, 20, 25], what is the output of numbers[-1]? # 25
# 2. Given letters = ['a', 'b', 'c', 'd', 'e'], what is the output of letters[-3]? # c

# Good!!


# Slicing 

# cars = ['audi', 'bmw', 'ford', 'toyota', 'tesla', 'volvo','lamborghini','ferrari','mercedes','jaguar']

# print(cars[0::2])


# start:end:step


# Slicing:

# 1. Given my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], what is the output of my_list[2:5]? # [2,3,4]
# 2. If colors = ['red', 'green', 'blue', 'yellow', 'purple'], what is the output of colors[1:4]? # ['green','blue','yellow']


# Step in Slicing:

# 1. For the list data = [1, 2, 3, 4, 5, 6, 7, 8, 9], what is the output of data[::2]? # [1,3,5,7,9] 
# 2. Given nums = [10, 20, 30, 40, 50, 60, 70, 80], what is the output of nums[1:7:2]? # [20,40,60]

# Good Job !!

# Combining Access Methods:J

# 1. What is the output of my_list[-3:][1] for my_list = [100, 200, 300, 400, 500]? # 400

# [300,400,500]

# 2. Given alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], what is the output of alphabet[2:5][-1]? # 


# cars = ['audi', 'bmw', 'ford', 'toyota', 'tesla', 'volvo']
# cars.append('lamborghini')

# print(cars)

# cars[-4] = "transfomer"

# print(cars)


# cars = ['audi', 'bmw', 'ford', 'toyota', 'tesla', 'volvo']
# cars.insert(0,'lamborghini')

# print(cars)


# Python GUI Application (GUI - Graphical User Interface)
# tkinter - library in python which is used to create GUI applications


# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox



# window = tk.Tk()
# window.title("Todo Application")


# frame_task = tk.Frame(window)
# frame_task.pack()

# listbox = tk.Listbox(
#     frame_task,
#     height=10,
#     width=50,
#     bg="cyan",
#     fg="black",
#     font=("Helvetica", 16),
#     borderwidth=1,
# )
# listbox.pack(side=tk.LEFT)

# scrollbar = tk.Scrollbar(frame_task)
# scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# window.mainloop()



# tkinter 

# from tkinter import *

# root = Tk()

# root.title("Devan's Application")
# root.configure(bg='#FF00FF')
# root.geometry('400x300')

# label = Label(root,text="Sign Up!!!",fg='white',bg='#FF00FF',font=('Merriweather',20))
# label.pack(pady=20)

# name_label  = Label(root,text="Name ",fg='white',bg='#FF00FF')
# name_label.pack(pady = 10)


# name_entry = Entry(root)
# name_entry.pack(pady=10)

# root.mainloop()




from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Devan's ipad")
# root.configure(bg='#FF00FF')
root.geometry('400x1000')


image = Image.open("pr.jpg")
bg_image = ImageTk.PhotoImage(image)

background_label = Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1) 

label =Label(root,text="sign in O_O",fg='white',bg='#FF00FF',font=('Merriweather',20))
label.pack(pady=20)
name_label = Label(root,text="name",fg='white',bg='#FF00FF')
name_label.pack(pady=10)

name_entry = Entry(root)
name_entry.pack(pady=10)

email_label = Label(root,text='email',fg='white',bg='#FF00FF')
email_label.pack(pady=10)

email_entry = Entry(root)
email_entry.pack(pady=10)


root.mainloop()