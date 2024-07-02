# variables:- 

# num,a,b

# data types:-

# int -> 
# float -> 1.5,10.5,20.5
# string -> "Anvi","Nidhi","Riya"
# boolean -> True/False 0/1

# type() -> to check the data type of a variable

# num = "7.5"
# print(type(num))


# num = 7
# num1 = 15
# print(num+num1)

# operators and operands 

# operator -> +,-,*,/,//,%,**

# print(20%3)

# firstname ="Anvi"
# surname = " Chugh"

# print(firstname+surname)

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("1. Addition",a+b)


# Conitional :-

# if statement
# if else statement
# if elif else statement


# if condition:
#     statements


# age = int(input("Enter your age: "))

# if age>=18:
#     print("you're an adult")
# if age<18:
#     print("you're a child")


# age = int(input("Enter your age: "))

# if age>18:
#     print("you're an adult")
# elif age == 18:
#     print("you're a teenager")
# else:
#     print("you're a child")


# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement


# a = 9
# b = 8
# ab = int(input("input a number: "))
# cd = int(input("input a  number 2: "))
   
    
# if ab>cd:
#     print("ab is greater")
# elif ab == cd:
#     print("both are equal")
# else:
#     print("cd is greater")

# %-> modulus operator -> remainder

# // -> floor division -> whole number
# / -> division -> decimal



# ** -> power operator

# oe= int(input("enter a number: "))
# if oe%2==0:
#     print("even")
# else:
#     print("odd")

# le= int(input("enter a year: "))

# if le%4 ==0:
#     print("leap year")
# else:
#     print( "not a leap year")



# base ** power = 4 ** 2 = 16

# loops:-

# 1. for loop : used to iterate over a sequence (that can be a list, tuple, dictionary, string or range) with a specific step value.

# syntax:

# for variable_name in range(start,end,step):
#     statements

# for a in range(1,21,2):
#     print(a)



# 2. while loop : used to execute a block of statements repeatedly until a given condition is satisfied.



# 0 2 4 6 8 10 12 14 16 18 20

# 0 5 10 15 20 25 30 35 40 45 50

# 10 9 8 7 6 5 4 3 2 1

# 1 2 3 4 5 6 7 8 9 10 = 55

# piggy_bank = 1

# for i in range(1,21):
#     piggy_bank = piggy_bank*i
    
# print(piggy_bank)


# 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 = 260



# random numbers-

# import random

# v = random.randint(1,10) # generates a random integer between 1 and 10

# print(v)


# 1 50

# break - to stop the loop



# Number guessing game:-

# random module - > randint() -> generates a random number between the given range

# import random

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# secret_number = random.randint(1, 100)
# attempts = 0

# while attempts < 10:
#     guess = int(input("Make a guess: "))
#     attempts = attempts + 1
    
#     if guess == secret_number:
#         print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
#         break
#     elif guess < secret_number:
#         print("Too low.")
#     else:
#         print("Too high.")

# if attempts > 10:
#     print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")



# strings:- it is a sequence of characters enclosed in single or double quotes.


# example:
    
# name = "Utkarsh Singh"
# print(name[-1])


# how we can find the length of a string?

# name = "Welcome to the class of python we are studying string in today's class"
# print(len(name))


# slicing :

# name = "Welcome to the class of python we are studying string in today's class"
# print(name[0:7])

# Modifying a string

# name = "ANVI"
# print(name.lower())


# replace method

# message = "I like to play football"
# print(message.replace("I","You"))

# concatenation

# firstname = "Anvi"
# lastname = "Chugh"

# print(firstname+lastname)


# replication

# name = "Anvi"

# print(name*3)

# formatting a string 

# age = 20
# name = "Anvi"

# print("My name is",name,"and I am",age,"years old.")
# print(f"My name is {name} and I am {age} years old.")


# Python List

# List is a collection of items which is ordered and changeable. Allows duplicate members.

# myList = ["apple","banana","cherry","apple","banana","cherry"]

# mylist1-[4,"apple",False,3.5]

# print(len(myList))


# myList = ["apple","banana","cherry","apple","banana","cherry"]

# print(myList[-4])

# myList = ["apple","banana","cherry","apple","banana","cherry"]

# # print(myList[1:4x``])


# myList = ["banana","cherry","banana","cherry"]

# if "apple" not in myList:
#     print("Yes it's present")
# else:
#     print("No it's not present")

# .lower() -> it converts the string into lowercase    ANVI.lower() = anvi




# name = "Anvi"
# print(name)

# name = "Anvi"
# print(name[::-1])


# .append()-> It adds up the elements/item at the last of the list.
# .insert()-> It adds up the elements/item at the required position of user.

# l2 = ["Audi","Mercedes","Toyota","Honda"]
# l2.insert(2,"BMW")


# print(l2)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])


import random

def getuser_choice():
    choices = ['rock','paper','scissors']
    user_choice = input("Enter your choice (rock,paper,scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock,paper,scissors): ").lower()
    return user_choice

def getcomputer_choice():
    choices = ['rock','paper','scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def check_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!!!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
    (user_choice == 'scissors' and computer_choice == 'paper') or \
    (user_choice == 'paper' and computer_choice == 'rock'):
        return "User's win!!!"
    else:
        return "Computer's win!!!"
    
def play_game():
    print("Welcome to the Rock-Paper-Scissors Game!")

    user_score = 0
    computer_score = 0
    while True:
        user = getuser_choice()
        computer = getcomputer_choice()
        print(f"User's choice: {user}")
        print(f"Computer's choice: {computer}")
        result = check_winner(user,computer)

        if result == "User's win!!!":
            user_score += 1
        elif result == "Computer's win!!!":
            computer_score += 1
        else:
            pass

        print(f"Current Score -> User: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print(f"Final Score -> User: {user_score}, Computer: {computer_score}")
    print("Thanks for playing the game!")

play_game()