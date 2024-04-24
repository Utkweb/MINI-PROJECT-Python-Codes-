# print("Welcome to the Class!")

# variables and datatypes:-

# a = 10
# a_1 = 10
# num = 10
# name = "Eshaal"

# datatypes:-

# Integer -> int  (-ve numbers to +ve numbers) [1, 2, 3, 4, 5]
# Float -> float (decimal numbers)[ 1.4, 1.5, 1.6]
# String -> str ("Eshaal", "eshaal", "Eshaal", "Eshaal")


# Operators and operands:-

# a+b

# + = operator
# a, b = operands

# operators = ["+", "-", "*", "/", "%", "**", "//"]


# a = "10.58"
# print(type(a))


# a = 10
# b = 20
# print("The summation of the two letters are : ",a+b)

# a = 19
# b = 6

# print("Want me to be your teacher AGAIN?! Fine! The answer for this question is", a // b)


# / = division -> it will give you the quotient(decimal numbers)
# // = floor division -> it will give you the quotient(whole numbers)

# 5 = 25

# ** = exponent -> it will give you the power of the number


# 4**5 = 4*4*4*4*4 = 1024

# Assignment operators:-

# = -> assignment operator
# += -> a = a + b
# -= -> a = a - b
# *= -> a = a * b
# /= -> a = a / b
# //= -> a = a // b
# **= -> a = a ** b
# %= -> a = a % b



# Conditional statements:-

# 3 types of conditional statements:-

# 1. if statements
# 2. elif statements
# 3. else statements


# if statements:-

# Syntax:
    
# if condition:
#     statements




# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))

# print("The summation of the two numbers are : ",a+b)

# age = int(input("Enter your age:"))

# if age>=18:
#     print("You are an adult")
# else:
#     print("You are not an adult")

# num = 9
# num1 = 17

# assignment operators :-

# <, >, <=, >=, ==, !=


# num = int(input("Enter the first number : "))
# num1 = int(input("Enter the second number : "))

# if num>num1:
#     print("The first number is greater than the second number")
# else:
#     print("The second number is greater than the first number")
    
    
# if
# if else
# if elif else


# age = int(input("Enter your age: "))

# if age>=18:
#     print("You are eligible for driving the car")
# elif age>=15:
#     print("You are eligible for driving the bike")
# elif age>=10:
#     print("You are eligible for driving the bicycle")
# else:
#     print("You are not eligible for driving the car")



# num = 14
# num1 = 14

# num = int(input("Enter the number : "))
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")


# loops:

# 2 types of loops:-

# 1. for loop
# 2. while loop


# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")
# print("Eshaal")


# syntax:

# for variable_name in range(start,end,step):
#     statements

# for i in range(1,11,2):
#     print(i)

# print("1. Eshaal")
# print("2. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")
# print("1. Eshaal")




# for i in range(1,11):
#     print(i,". Eshaal")

# input:
# a = 9
# b = 8

# a= int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# a = a+b          # a = 9+8 = 17
# b = a-b          # b = 17-8 = 9
# a = a-b          # a = 17-9 = 8

# print("a = ",a)
# print("b = ",b)


# ouput:

# a = 8
# b = 9


# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610


# if elif else statements



# 1 2 3 4 5 6 7 8 9 10 = 55

# sum = 0

# for i in range(1,11):
#     sum = sum+i
# print("The sum of the first 10 natural numbers are : ",sum)



# 0 - 20 -> even numbers -> 0 2 4 6 8 10 12 14 16 18 20 -> sum of the even numbers from 0 to 20 is : 110


# Multiplication Table program using a for loop:-

# num = int(input("Enter the number: "))

# for i in range(1,11):
#     print(num,"*",i,"=",num*i)



# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24




# 1 2 3 4 5 6 7 8 9 10

# i = 1

# while i<=10:
#     print(i)
#     i = i+1


# i = 100

# while i>=0:
#     print(i)
#     i = i-1


# factorial of a number:-


# 5 = 5*4*3*2*1 = 120

# fact = 1

# num = int(input("Enter the number of which you want to find the factorial: "))
# for i in range(1, num+1):
#     fact = fact*i
# print("The factorial of the number is : ",fact)

# random module:-

# import random

# print(random.randint(1, 50))


# Number guessing game :-

# import random

# secret_number = random.randint(1,50)

# print("Welcome to the number guessing game")
# print("You need to guess the number between 1 and 50")

# max_attempts = 10
# attempts = 0

# while attempts<max_attempts:
#     guess = int(input("Enter your guess:"))
#     attempts = attempts+1
    
#     if guess == secret_number:
#         print("Congratulations! You have guessed the correct number")
#         print("You have guessed the number in ",attempts)
#         break
#     elif guess<secret_number:
#         print("Your guess is too low")
#     else:
#         print("Your guess is too high")
        
# if attempts == max_attempts:
#     print("You have lost the game! The correct number was : ",secret_number)
    


# import random

# quotes = [
#     "The only way to do great work is to love what you do. - Steve Jobs",
#     "Life is what happens when you're busy making other plans. - John Lennon",
#     "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
#     "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
#     "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
#     "The only impossible journey is the one you never begin. - Tony Robbins",
#     "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
#     "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
#     "Believe you can and you're halfway there. - Theodore Roosevelt",
#     "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama"
# ]

# print("Welcome to out random quote generator")
# input("Press enter to get a random quote: ")

# quote = random.choice(quotes)

# print("Random Quote : ",quote)


# int 
# float
# strings
# boolean

# String: it is a sequence of characters enclosed within double quotes or single quotes

# examples: "Eshaal", "eshaal", "Eshaal", "Eshaal"

#Multiline String

# name = '''Eshaal
# jcnwioncie
# incbnwbiuvcnw
# nwienuw 
# ciwunjcow
# uncewov
# iuvnwi
# '''
# print("The name of the student is : ",name)


# Slicing strings:- 

# name = "Eshaal Khan"
#       # 012345678910
# print(name[7:])

# how to find the length of the string 

# len(variable_name)



# some = "Welcome to the class of coding where we are going ot learn about the sliciing strings"
# print(len(some))

# modify string 

# name = "ESHAAL"
# print(name.lower())

# .lower() -> it will convert the string into lowercase
# .upper() -> it will convert the string into uppercase

# sentence = "           hey buddy  !         "
# print(sentence.strip())


# name = str(input("Enter your name: "))
# print("Your name is: ",name.lower())

# concatenate string - it is a process of joining two or more strings together.

# firstname = "utkarsh"
# lastname = "Singh"

# print(firstname+lastname)

# Array:
    
# i) List
# ii) Tuple
# iii) Set
# iv) Dictionary


# Python List: to storre multiple in a single variable

# List are created by using a square bracket[]

# cars = ["Audi","BMW","Mercedes","Jaguar","Lamborghini"]
# print(cars[3])


# cars = ["Audi","BMW","Mercedes","Jaguar","Lamborghini"]
# print(cars[1:3])

# how to calculate the length of a list

# cars = ["Audi","BMW","Mercedes","Jaguar","Lamborghini"]
# print("The total length of the list is :",len(cars))


# String, int and boolean data types:
    
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]
# l3 = ["Eshaal","Khan","Utkarsh","Singh","Aman","Kumar"]
# l4 = [0,1,True,False]


# l5 = ["Eshaal",20,1.5,False]

# How we can change the value of a list?

# f1 = ["redbull","ferrari","mclaren","mercedes","aston martin"]

# f1[0] = "audi"

# print(f1)

# how we can change multiple values of a list?

# f1 = ["redbull","ferrari","mclaren","mercedes","aston martin"]

# f1[0:2] = "audi","bmw"

# print(f1)

# Operators:-

# + - Concatenation
# * - Repetition/Replication

# concatenation
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]

# print(l1+l2)


#replication 

# l1 = [1,2,3,4,5]

# print(l1*3)


# Membership Operator in List:-

# 1. in
# 2. not in

# l1= ['a','b','c','d','e']

# print('a' not in l1)

# Functions in list:-

# 1. append() - it adds up the value or the element at the end of the list

# l1 = [1,2,3,4,5]
# l1.append(8)

# print(l1)

# 2. update : it is used to update the value of a list

# l1 = [1,2,3,5]
# l1[3]=4

# print(l1)

# 3. insert() - it is used to insert the value at a specific index

# l1 = [1,2,3,5]

# l1.insert(3,4)

# print(l1)


# functions - it is a block of code that is used to perform a specific task and can be called again and again


# a = 0
# b = 1

# print(a+b)


# syntax:

# defining of a function
# def function_name():
#     print("Welcome to the function")

# #main function

# function_name()    #calling the function


# def add(a,b):
#     print(a+b)
    
# # main function

# add(2,3)
# add(4,5)

# def subtract(a,b):
#     print(a-b)
# def add(a,b):
#     print(a+b)
# def multiply(a,b):
#     print(a*b)
# def divide(a,b):
#     print(a/b)
    
# # main function

# subtract(2,3)
# add(4,5)
# multiply(6,7)
# divide(8,9)


# °F = (9/5 × °C) + 32




# def cel_to_fahrenheit(celsius):
#     f = (9/5 * celsius) + 32
#     print("The temperature in fahrenheit is : ",f,"°f")
    
# c = int(input("Enter the temperature in celsius: "))
# cel_to_fahrenheit(c)


# °C = (°F - 32) × 5/9

# def fahrenheit_to_cel(fahrenheit):
#     c = (fahrenheit-32) * 5/9
#     print("The temperature in celsius is : ",c,"°c")

# f = int(input("Enter the temp in fahrenheit:"))
# fahrenheit_to_cel(f)



# module - tkinter - it is a standard GUI library for python

# import tkinter as tk
# def f_c():
#     fahrenheit = float(e1.get())
#     c = (fahrenheit-32) * 5/9
#     result.config(text=f"{fahrenheit} Fahrenheit = {c:.2f} Celsius")
    
# def c_f():
#     celsius = float(e1.get())
#     f = (9/5 * celsius) + 32
#     result.config(text=f"{celsius} Celsius = {f:.2f} Fahrenheit")
    
# # creating the main window
# root = tk.Tk()

# # setting the title of the window
# root.title("Temperature Converter")

# l1 = tk.Label(root,text="Temperature Convertor",font=("Arial",20))
# l1.grid(row=0,column=0)


# e1= tk.Entry(root)
# e1.grid(row=1,column=0)
# b1 = tk.Button(root,text="Celsius to Fahrenheit",fg="white",bg="green",command =c_f)
# b1.grid(row=2,column=0)

# b2 = tk.Button(root,text="Fahrenheit to Celsius",fg="white",bg="green",command = f_c)
# b2.grid(row=2,column=1)

# result = tk.Label(root,text="")
# result.grid(row=3,column=1)
# root.mainloop()



# import tkinter as tk

# def press1():
#     result.config(text="Eshaal")
# def press2():
#     result.config(text="Utkarsh")

# root = tk.Tk()

# b1 = tk.Button(root,text="Button 1",fg="white",bg="green",command=press1)
# b1.grid(row=0,column=0)

# b2 = tk.Button(root,text="Button 2",fg="white",bg="green",command= press2)
# b2.grid(row=0,column=1)

# result = tk.Label(root,text="")
# result.grid(row=1,column=0)
# root.mainloop()

# eshaal 
# eshaal
# eshaal 
# eshaal



# Tic Tac Toe Game:-

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


# Rock, Paper and scissor game:-


# rock rock = draw
# rock and paper - winner is paper
# rock and scissor - winner is rock
# paper and scissor - winner is scissor


import random

def user_choice():
    user = input("Enter your choice (rock,paper or scissor): ").lower()
    while user not in ['rock','paper','scissor']:
        print("Invalid Choice. Please enter a valid choice")
        user = input("Enter your choice (rock,paper or scissor): ").lower()
    return user

def computer_choice():
    return random.choice(['rock','paper','scissor'])

def win(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif(user_choice == 'rock' and computer_choice == 'scissor') or \
        (user_choice == 'scissor' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
            return "The user has won !!!!!"
    else:
        return "The bot has won !!!!!"
    
def play_game():
    print("Welcome to the Rock, Paper and Scissor Game !!!!!1")
    while True:
        user = user_choice()
        computer = computer_choice()
        print(f"User choice: {user}")
        print(f"Computer choice: {computer}")
        print(win(user,computer))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for Playing !!!")
            break
        
        
play_game()