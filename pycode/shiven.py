# a = int(input("Enter a number: "))
# print("The square of the number is: ", a**2)


# name = "Shiven"
# age = 18



# # String formatting

# print("My name is: ",name, "and my age is: ", age)

# a = True
# print(type(a))

# Operators and operands:-

# Operators are special symbols in python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.


# a+b

# operators: +
# operands: a,b

# Arithmetic operators:-

# 1. Addition: +
# 2. Subtraction: -
# 3. Multiplication: *
# 4. Division: /
# 5. Modulus: %
# 6. Exponentiation: **              
# 7. Floor division: //
# 8. Assignment: =

# Comparison operators:-
# 1. Equal to: ==    
# 2. Not equal to: != 
# 3. Greater than: >
# 4. Less than: <
# 5. Greater than or equal to: >=
# 6. Less than or equal to: <=


# in & not in operators:-
# 1. in: Returns True if a sequence with the specified value is present in the object
# 2. not in: Returns True if a sequence with the specified value is not present in the 
# object.

# Identity operators:-
# 1. is: Returns true if both variables are the same object
# 2. is not: Returns true if both variables are not the same object

# Logical operators:-
# 1. and: Returns True if both statements are true
# 2. or: Returns True if one of the statements is true
# 3. not: Reverse the result, returns False if the result is true
# 4. xor: Returns True if one of the statements is true but not both
# 5. nand: Returns False if both statements are true
# 6. nor: Returns False if both statements are false
# 7. xnor: Returns True if both statements are true or both statements are false
# 8. xand: Returns True if both statements are false or both statements are true


# if statements
# if else statements
# if elif elif ..... else statements


# if statements:

# if condition:
#     statement

# num = int(input("Enter a number: "))
# if num >10:
#     print("The number is greater than 10")
# else:
#     print("The number is less than 10")

# a = 10
# b = 3
# print(a//b)

# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:

# age = int(input("enter the number between 1 to 7 "))
# if age>18:
#     print("You are eligible to vote")
# elif age==18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")   


# 1. Sunday
# 2. Monday
# 3. Tuesday
# 4. Wednesday 


# loops : for loop, while loop

# for loop: 
    
# syntax:
    
# for i in range(start, stop, step):
#     statement


# Shiven 

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30


# piggy_bank = 0
# for i in range(0,11):
#     print(i) 

    
    
# 2 to 30
# 1 to 27 



# 2x1 = 2
# 2x2 = 4
# 2x3 = 6
# 2x4 = 8
# 2x5 = 10
# 2x6 = 12
# 2x7 = 14
# 2x8 = 16
# 2x9 = 18
# 2x10 = 20



# num = int(input("Enter a number of which you want the table of ?: "))

# print("The table of ",num,"is: ")
# print(" \n")
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
#           8  X 1 = 8

# while loop

# for i in range(start,end,step):
    
    
# intialization
# while condition:
#     statement
#     increment/decrement


    
# while condition:
#     statement
#     increment/decrement

# i = 1
# while i<=10:
#     print(i)
#     i = i+1



# num = int(input("Enter the number you wanna reverse : "))   
# sum = 0
# while num!=0:
    
#     rem = num%10              
#     sum = sum*10 +rem         
#     num = num//10             
    
# print("The reverse of the number is: ",sum)





# print(3//10)




# num = int(input("Enter the number to check whether a number is palindrome or not: "))
# temp = num
# sum = 0
# while num!=0:
#     rem = num%10
#     sum = sum*10 + rem
#     num = num//10

# if sum == temp:
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")

# Nested Loops : 
    
# for i in range(1,6):
#     for j in range(1,i+1): 
#         print(i,end=" ")
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# *
# **
# ***
# ****
# *****


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# piggy_bank = 0
# for i in range(1,101):
#     piggy_bank+=i
# print("The summation of numbers from 1 to 100 are : ",piggy_bank)


# revision :
    
    # loops: for loop, while loop
    
    
    # for loop:
    #     syntax:
    #         for i in range(start,stop,step):
    #             statement
    
# num = int(input("Enter a number of which the multiplication table you want ?: "))
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
                
                
# Strings:- it is a sequence of characters enclosed within single quotes or double quotes.

# name = "Shiven Patel"

# indexing : It is a process of accessing the characters of a string using their index values.
# positive indexing
# negative indexing
# print(name[5])
# print(name[::-1])

# slicing:- It is a process of accessing a substring from a string using their index values.

# print(name[7:])

# len()- It is a function used to find the length of a string.

# print(len(name))


# 321    123  -> Not a palindrome

# 12321 12321 -> palindrome


# print(10//3)

# loops: for loop, while loop


# for iterating_var in range(start,end,step):
#     statements

# for i in range(11):
#     print(i,"Utkarh Singh")

# num = int(input("Enter a number of whihc you want the table of :"))
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
    
    
    

# 8 X 1 = 8



# prime numbers: - A number which is divisible by 1 and itself is called a prime number.

# num = int(input("Enter a number to check whether a number is prime or not: "))

# cnt = 0
# for i in range(2,num):
#     if num%i == 0:
#         cnt = cnt+1
    
# if cnt == 0:
#     print("The number is prime")
# else:
#     print("The number is not prime")
# print(5//2.0)





# a = str(input("I can write strings backwards and tell whether it is a paladrone or not!: "))

# b = (a[::-1])

# if a == b:
#   print("Its a paladrone")
#   print(b)

# else:
#   print("Its not a paladrone")
#   print(b)


# a = "Utkarsh"


# count = 0
# for i in range(0,len(a)):
#     if a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U" or a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] =="o" or a[i] == "u":
#         count+=1
# print(count)


# name = input("Enter your name to find wether you have the letter S ")

# for i in range(0,len(name)):
#   if name[i] == "s":
#     print(i)
    
#   else:
#     print("Your word dosn't have a S")

        
# defining a function:-  
# def add():
#     a = 9
#     b = 8
#     print(a+b)

# # main function
# # calling a function:-


# add()



# def add():
#     a = 9
#     b = 8
#     print(a+b)

    

# def minus():
#     c = 9
#     d = 5
#     print(c-d)

# def mul():
#     e = 4
#     f = 3
#     print(e*f)


# # main function 


# print("The addition of two numbers is: ")
# add()
# print("The subtraction of two numbers is: ")
# minus()
# print("The multiplication of two numbers is: ")
# mul()








# defining a function:-
# def add(a,b):
#     print(a+b)
    
# # main function


# # calling a function:-
# add(7,8)


# def isprime(num):
#     cnt=0
#     for i in range(1,num+1):
#         if num%i==0:
#             cnt+=1
#     if cnt==2:
#         print("The number is prime")
#     else:
#         print("The number is not prime")
        
# # main function

# n = int(input("Enter a number: "))
# isprime(n)

# def palornot(a):
#     b = a[::-1]
#     if a == b:
#         print("The string is palindrome")
#     else:
#         print("The string is not palindrome")
    
# # main function

# name = int(input("Enter a number: "))

# num = str(name)

# palornot(num)
    



# defining a function:-
# def multiply(a,b):
#      print(a*b)

# # main function

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))


# # calling a function
# multiply(a,b)

# Arrays :- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# array: it is a collection of homogeneous data type elements stored in a contiguous memory location.

# fruits = ["apple","mango","banana","grapes","orange","kiwi","watermelon","pineapple","papaya","cherry"]

# print(len(fruits))


# for i in fruits:
#     print(i)


# print(fruits[4:7])


# Now going to learn about how we are going to add the elements in the array.

# 1. append() --- add the element at the end of the array.
# 2. insert() --- add the element at the specified index.

# fruits = ["apple","mango","banana","grapes","orange","kiwi","watermelon","pineapple","papaya","cherry"]

# fruits.remove("watermelon")

# print(fruits)

# remove the element from the array:-

# 1. pop() --- remove the element from the end of the array.
# 2. remove() --- remove the element from the specified index.




# import random

# x = random.randint(1,2)

# print(x)


# " Number guessing game "

# import random

# l = int(input("Enter the lower limit : "))
# u = int(input("Enter the upper limit : "))

# x = random.randint(l,u)

# print("\n You have only 5 chances to guess the number! \n")


# cnt = 0

# while cnt<5:
#     cnt = cnt+1
    
#     guess = int(input("Enter your guess : "))
    
#     if guess ==x:
#         print("Congratulations! You guessed the number in ",cnt,"chances")
#         break
#     elif x > guess:
#         print("You guess is too low")
#     elif x < guess:
#         print("You guess is too high")
    
    
# if cnt>=5:
#     print("Game over! You have exceeded the number of chances")


# patterns:-


# * * * *
# * * * *
# * * * *
# * * * *
    
    
# for i in range(0,4):
#     for j in range(0,4):
#         print("*",end=" ")
#     print()



# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4


# matpltolib :- It is a library used for data visualization.

# it is an open source library.

# command for installing matplotlib library:-

# pip install matplotlib


# pip install name_of_the_library

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints,'o')
# plt.show()



# file handling :- It is a process of storing the data in a file and retrieving the data from the file.

# open()

# "r"-> read mode
# "w"-> write mode
# "a"-> append mode
# "x"-> create mode

# f = open("nitya.txt",'r')


# print(f.read())

# import os
# os.remove("nitya.txt")


# f = open("nitya.txt",'x')

# Program for partial screenshot

# import pyscreenshot

# image = pyscreenshot.grab()

# # To view the screenshot
# image.show()

# # To save the screenshot
# image.save("GeeksforGeeks.png")


# gui -> graphical user interface

# tkinter:- It is a standard GUI library for python.




# import tkinter as tk

# class CalculatorApp:
#     def __init__(self,master):
#         self.master = master
#         master.title("Simple Calculator")
        
#         self.displa
        

# from tkinter import *

# top = Tk()

# b1 = Button(top,text="Button 1",fg="red")
# b1.pack(side=LEFT)
# b2 = Button(top,text="Button 2",fg="blue")
# b2.pack(side=RIGHT)
# b3 = Button(top,text="Button 3",fg="green")
# b3.pack(side=TOP)
# b4 = Button(top,text="Button 4",fg="orange")
# b4.pack(side=BOTTOM)
# top.mainloop()

# import tkinter as tk

# def click():
#     global counter
#     counter=counter+1
#     label.config(text=f"Clicks :{counter}")
    
# counter = 0

# root = tk.Tk()
# root.title("Counter")


# label = tk.Label(root,text="Clicks: 0")
# label.pack()

# button = tk.Button(root,text="Click me!",command=click)
# button.pack()

# root.mainloop()



# import tkinter as tk

# root = tk.Tk()

# l1 = tk.Label(root,text="Hello Shiven !!!!!")
# l1.pack(side = LEFT)

# root.mainloop()

# def sum(a, b, c ):
#     return a + b + c

# def printBoard(xState, zState):
#     zero = 'X' if xState[0] else ('O' if zState[0] else 0)
#     one = 'X' if xState[1] else ('O' if zState[1] else 1)
#     two = 'X' if xState[2] else ('O' if zState[2] else 2)
#     three = 'X' if xState[3] else ('O' if zState[3] else 3)
#     four = 'X' if xState[4] else ('O' if zState[4] else 4)
#     five = 'X' if xState[5] else ('O' if zState[5] else 5)
#     six = 'X' if xState[6] else ('O' if zState[6] else 6)
#     seven = 'X' if xState[7] else ('O' if zState[7] else 7)
#     eight = 'X' if xState[8] else ('O' if zState[8] else 8)
#     print(f"{zero} | {one} | {two} ")
#     print(f"--|---|---")
#     print(f"{three} | {four} | {five} ")
#     print(f"--|---|---")
#     print(f"{six} | {seven} | {eight} ")

# def checkWin(xState, zState):
#     wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#     for win in wins:
#         if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
#             print("X Won the match")
#             return 1
#         if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
#             print("O Won the match")
#             return 0
#     return -1
    
# if __name__ == "__main__":
#     xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     turn = 1 # 1 for X and 0 for O
#     print("Welcome to Tic Tac Toe")
#     while(True):
#         printBoard(xState, zState)
#         if(turn == 1):
#             print("X's Chance")
#             value = int(input("Please enter a value: "))
#             xState[value] = 1
#         else:
#             print("O's Chance")
#             value = int(input("Please enter a value: "))
#             zState[value] = 1
#         cwin = checkWin(xState, zState)
#         if(cwin != -1):
#             print("Match over")
#             break
        
#         turn = 1 - turn

# rock rock = tie

# paper rock = paper wins
# scissor rock = rock wins
# scissor paper = scissor wins

# import random


# def get_user():
#     user = str(input("Enter your choice (rock/paper/scissor) : ")).lower()
#     while user not in ['rock','paper','scissor']:
#         print("Invalid choice")
#         user = str(input("Enter your choice (rock/paper/scissor) : ")).lower()
#     return user

# def get_bot():
#     return random.choice(['rock','paper','scissor'])

# def win(user_choice,bot_choice,name):
#     if user_choice == bot_choice:
#         return "It's a tie"
#     elif    (user_choice == 'rock' and bot_choice == 'scissor') or \
#             (user_choice == 'paper' and bot_choice == 'rock')or \
#             (user_choice == 'scissor' and bot_choice=='paper'):
#             return f"{name} wins 👍"
#     else:
#         return "Bot wins"
    
# def play():
#     print("Welcome to the game of rock paper scissor")
#     name = input("Enter your name : ")
#     while True:
#         user_choice = get_user()
#         bot_choice = get_bot()
#         print(f"User choice : {user_choice}")
#         print(f"Bot choice : {bot_choice}")
#         print(win(user_choice,bot_choice,name))
#         play_again = str(input("Do you want to play again (yes/no) : ")).lower()
#         if play_again!='yes':
#             print("Thanks for playing the game!!!")
#             break
    

# play()


# OOPS:

# 1. Its abbreviated as Object Oriented Programming System.
# 2. It is a programming paradigm that uses objects and classes in programming.

# Objects : It is an instance of a class.

# Class : It is a blueprint of an object.

# create a class:-

# class Student:
#     name = "Shiven"
#     age = 12

# # create an object:-

# s1 = Student()
# print(s1.age,s1.name)


# __init__() -> It is a special method in python which is used to initialize the object of a class.
# self -> It is a reference variable that refers to the current object.

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Shiven",18)
# p2 = Person("Nitya",19)

# print(p1.name,p1.age)
# print(p2.name,p2.age)


# __str__() -> It is a special method in python which is used to return the string representation of the object.


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# p1 = Person("Shiven",18)  //object creation 
# p2 = Person("Nitya",19)

# print(p1)
# print(p2)


# Create a class name as Car with the following attributes:

# 1. brand
# 2. model
# 3. year
# 4. price