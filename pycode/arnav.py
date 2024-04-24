# name = "Arnav"
# age = 10
# print("My name is ", name,"and I'm", age, "years old.")

# # My name is Arnav and I'm 10 years old.

# My favorite color are red, blue, and green.

# Data Types: 
    
# 1. integers - int       
# 2. float - float    10.2, 1.3, 1.4
# 3. string - str     "Arnav"   "Welcome to Python"
# 4. boolean - bool    True/False  1/0


# name = str(input("What's your name ? "))
# print("My name is ", name)

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print(a+b)



# import random 

# a = random.randint(1,10)
# print(a)


# area of square = side * side

# side = int(input("Enter side of sqaure:"))
# print(side**2)

# perimeter of sqaure = 4*side


# Area of rectangle = length * breadth

# length = 9
# breadth = 5

# print(length*breadth)

# Perimeter of rectangle = 2*(length + breadth)

# length = 9
# breadth = 6
# print("Perimeter of Rectangle :",2*(length+breadth))





# if condition:
#     statement1
#     statement2
    
# a = 10 
# b = 20 


# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# person_age = 19
# if person_age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# if elif else statements
# if condition:
#     statement1
# elif condition:
#     statement2
# elif condition:
#     statement3
# else:
#     statement4

# num = int(input("Enter a number:"))
# if num>0:
#     print("The number is positive")
# elif num<0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# loops:- for loop, while loop 

# for variable_name in range(start,end,step):
#     statements
    
# for i in range(1,11,2):
#     print(i)


# 0 2 4 6 8 10 12 14 16 18 20

# num = int(input("Enter a number:"))

# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")


# 

# for i in range(start,end,step):
#     statements

# 1 2 3 4 5 6 7 8 9 10
# for i in range(1,11,2):
#     print(i,end=" ")


# even numbers from 0 to 40 

# odd numbers from 0 to 40


# piggy_bank =0
# for i in range(1,11):
#     piggy_bank = piggy_bank+i
#     print(piggy_bank)



# loops:- for loop, while loop



# for variable_name in range(start,end,step):
#     statements

# piggy_bank = 0
# for i in range(0,21,2):
#     piggy_bank=piggy_bank+i
# print(piggy_bank)

# even_count=0
# odd_count=0
# for i in range(1,21):
#     if i%2==0:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1

# print("Even numbers:",even_count)
# print("Odd numbers:",odd_count)



# num = int(input("Enter a number:"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)


# for i in range(1,11):
#     print(i)

# count=0

# for i in range(1,11):
#     if i%2==0:
#         count=count+1
# print(count)


# num = int(input("Enter a number :"))
# if num%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")

# factorial = 1
# num = int(input("Enter a number:"))
# for i in range(1,num+1):
#     factorial=factorial*i
# print("Factorial of",num,"is",factorial)

# 696

# ARNAV -> VANRA

# 1=1112233
#1+1=2= 0 1 1 2 3 5 8 1

# 0 1 1 2 3 5 8 13 21 34 55

# a = 0
# b = 1

# print(a,b, end = " ")
# for i in range(2,11):
#     c = a+b
#     print(c, end = " ")
#     a = b
#     b = c

# name =  "Arnav"
#       #  01234
# print(name[4]+name[3]+name[2])

# indexing :-
# name = "Arnav"
#       01234567891011
# name = "Utkarsh Singh"
# print (name[0]+name[1])

# reverse a string 
# print(name[::-1])


# t
# l
# u
#  name = "chengchuang liu"

# print(name[::-1])




# counting Characters :-

# how we can find the length of a string

# name = "chengchuang liu"

# # len -> Length of the string 

# print(len(name))



# name = "chengchuang liu"

# print(len(name))


# uppercase and lowercase

# name = "arnav"
# name1 ="AARYAKI"
# print(name.upper())
# print(name.lower())

# # concatenating strings

# firstname ="Arnav"
# lastname = " Jetly"

# print(firstname+lastname)


# replications

# name = "Arnav "
# print(name*3)



# import random

# num = random.randint(1,101)

# print(num)

# number guessing game

# import random

# print("Welcome to the number guessing game")
# print("You have 10 attempts to guess the number")
# print("The number is between 1 and 100")
# secret_number = random.randint(1,101)
# attempts = 0

# while attempts<=10:
#     guess = int(input("Enter your guess:"))
#     attempts= attempts+1
    
#     if guess == secret_number:
#         print("SS! You guessed the right number")
#         break
#     elif guess<secret_number:
#         print("The number is too low")
#     else:
#         print("The number is too high")

# if attempts>=10:
#     print("You have exhausted all your attempts. The number was:",secret_number)



# F = (9/5 × C) + 32


# desktop application - module that is said to be as Tkinter


# import tkinter as tk

# root = tk.Tk()

# name = tk.Label(root,text="Arnav Jetly")
# name.grid(row=0,column=0)

# b1 = tk.Button(root,text="Click me",fg="white",bg="green")
# b1.grid(row=1,column = 0)


# root.mainloop()


# ROCK ROCK = TIE
# PAPER PAPER = TIE
# SCISSORS SCISSORS = TIE
# ROCK PAPER = PAPER WINS
# ROCK SCISSORS = ROCK WINS
# PAPER SCISSORS = SCISSORS WINS


import random

def user_choice():
    user = input("Enter your choice (rock/paper/scissor):").lower()
    while user not in ['rock','paper','scissor']:
        print("Invalid Choice. Please enter a valid choice ( rock, paper, scissor)")
        user = input("Enter your choice (rock/paper/scissor):").lower()
    return user

def bot_choice():
    return random.choice(['rock','paper','scissor'])

def win(user_choice ,bot_choice):
    if user_choice == bot_choice:
        return "TIE"
    elif (user_choice == 'rock' and bot_choice == 'scissor') or \
        (user_choice == 'scissor' and bot_choice == 'paper') or \
        (user_choice == 'paper' and bot_choice == 'rock'):
            return "User Wins"
    else:
        return "Bot Wins"

def play_game():
    print("Welcome to the Rock Paper Scissor Game")
    while True:
        user = user_choice()
        bot = bot_choice()
        
        print(f"User choice: {user}")
        print(f"Bot choice: {bot}")
        print(win(user,bot))
        play = input("Do you want to play again? (yes/no):").lower()
        if play!="yes":
            print("Thanks for playing the game")
            break
        
play_game()




if user == bot:
    print("The User wins")
else:
    print("You lose!!!")
