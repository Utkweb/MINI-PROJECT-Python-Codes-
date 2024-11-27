# print("Welcome to the class of Python")

# Variables : It stores the values 
# a = 10
# a = 10.5
# name = "Navya"
# flag = True

# Data types:

# 1. Integer(int) : It is a whole number without decimals in it.
# 2. Float(float) : It stores the number with decimals in it.
# 3. String (str) : It stores the words, characters, sentences,etc
# 4. Boolean (bool) : It stores the values either in True or False

# a = True

# type() - It helps you to know the type of the data

# a = False
# print(type(a))

# Operators and Operands:

# a+b

# Operator - +
# Operands - a,b

# Operators:

# 1. Arithmetic Operators:

# (+) Addition
# (-) Subtraction
# (*) Multiplication
# (/) Division
# (//) Floor Division
# (%) Modulus
# (**) Exponent

# a = 8
# b = 9
# print("Addition",a+b)

# conditional Statements - it is used to check the condition

# three types of conditional statements:

# 1. if statements - It helps you to check the condition only once

# syntax:

# if condition:
#     statements

# if 10 > 5:
#     print("10 is greater than 5")

# age = 21
# if age > 18:
#     print("You are eligible to drive")


# 2. if-else statements - It helps you to check the condition and if the condition is false then it will execute the else block

# syntax:

# if condition:
#     statements
# else:
#     statements

# age = 15

# if age > 18:
#     print("You are eligible to drive")
# else:
#     print("You are not eligible to drive")


# Ques - Write a program and take two variables a and b and check whether a is greater than b or not.

# 3. if elif else condition - It helps you to check the multiple conditions

# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements


# a>b = a is greater than b
# a<b = a is less than b
# a == b = a is equal to b


# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))


# if a>b:
#     print("a is greater than b")
# elif a<b:
#     print("a is less than b")
# else:
#     print("a is equal to b")


# loops : It helps you to execute the block of code multiple times


# we are having two types of loops:

# 1. for loop

# syntax:

# for variable in range(start, end, step):
#     statements

# for i in range(1,101,2):
#     print(i)


# 1 2 3 4 5 6 7 8 9 10

# 2 4 6 8 10 12 14 16 18 20

# 10 9 8 7 6 5 4 3 2 1

# for i in range(10,0,-1):
#     print(i)

# 2. while loop


# 8 X 1 = 8
# 8 X 2 = 16
# 8 X 3 = 24

# num = int(input("Enter the number of which you want the multiplication table of : "))
# for i in range(1,21):
#     print(num," X ",i," = ",num*i)


# 1+2+3+4+5+6+7+8+9+10 = 55

# piggy_bank = 0
# for i in range(1,11):
#     piggy_bank = piggy_bank + i
# print(piggy_bank)
    

# 1 100

# even_sum = 0
# odd_sum = 0 
# for i in range(1,101):
#     if i%2 == 0:
#         even_sum=even_sum+i
#     else:
#         odd_sum = odd_sum+i
# print("Even Sum : ",even_sum)
# print("Odd Sum : ",odd_sum)

# count = 0
# num = int(input("Enter the number to check prime : "))
# for i in range(2,num//2):
#     if num % i == 0:
#         count = count + 1

# if count == 0:
#     print("Prime")
# else:
#     print("Not Prime")


# 40
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39


# 59

# 24

# 5! = 5*4*3*2*1 = 120
# 8! = 8*7*6*5*4*3*2*1 = 40320

# fact = 1
# num=int(input("Enter the number to find the factorial : "))
# for i in range(1,num+1):
#     fact = fact*i

# print("Factorial of ",num," is ",fact)



# Number guessing game


# random module - it chosses the number randomly


# import random

# print(random.randint(1,10))


# 1 20

# import random

# print("Welcome to the Number guessing game!!!")
# print("You need to guess the number between 1 to 30")
# print("You have only 3 attempts")


# secret_number = random.randint(1,30)
# attempts = 0

# max_attempts = 5

# while attempts < max_attempts:
#     guess = int(input("Enter your guess : "))

#     attempts = attempts+1
#     if guess == secret_number:
#         print("You won the Jackpot")
#         break
#     elif guess>secret_number:
#         print("Too high.. Try again!!!")
#     else:
#         print("Too low.. Try again!!!")
        
#     if attempts == max_attempts:
#         print("ohhoooo You lost the game !!!!!!!!!!!. The sceret number is",secret_number)
#         break


# 123 =>  321

# /
# //
# %

# 123 % 10 = 3*10 = 30 + 2 = 32*10 =320+ 1 = 321

# 123 // 10 = 12%10 = 2

# 12 // 10 = 1%10 = 1

# num = int(input("Enter the number : "))   #num = 123
# ans = 0

# while num>0:

#     rem = num%10    #rem = 1%10 = 1
#     ans = ans*10+rem    #ans = 32*10 + 1 = 321
#     num = num // 10    #num = 12//10 = 1


# print("The reverse of the number is",ans)


# 123 = 1+2+3 = 6

# 0 1 1 2 3 5 8 13 21 34 

# previous = 0
# current = 1

# print(previous,current,end= " ")

# for i in range(1,11):
#     next = previous+current
#     print(next,end=" ")
#     previous = current
#     current = next



# formatting strings

# My name is Navya

# name = "Navya"
# age = 11

# # print("My name is",name,"and I'm",age,"years old.")

# print(f"My name is {name} and I'm {age} years old.")



# name = "Navya"

# for i in name:
#     print(i)

# length of the word

# word = "circumstances"
# print(len(word))

# memberships operators

# in : including
# not in : excluding

# name = "Navya"

# if 'z' not in name:
#     print("present")

# name = str(input("Enter the name :"))
# vowel = "AEIOUaeiou"

# count = 0

# for i in name:
#     if i not in vowel:
#         count = count+1

# print(f"The name consists {count} consonants.")


# data types:

# string
# int
# float
# boolean



# Arrays:

# 1. list - it can store multiple values in it.
# They are enclosed by [].
# It allows duplicate values

# num = [1,2,3,4,5,7,8,9,10]
# names = ["Navya","Utkarsh","Izzy","Ele","Molly"]
# num1 = [10.2,15.2,78.0,89.21]
# num2 = [True,False,True]
# num3 = ["Navya",11,15.0,True]


# names = ["Navya","Utkarsh","Izzy","Ele","Molly"]
# print(names)

# for finding the length of the list we can use len():

# names = ["Navya","Utkarsh","Izzy","Ele","Molly"]
# print(len(names))

# if we need to access a particluar element we can access them with the index
# negative indexing - it starts from -1 to -n and goes from right to left

# names = ["Navya","Utkarsh","Izzy","Ele","Molly"]

# print(names[-1])

# slicing 

# names = ["Navya","Utkarsh","Izzy","Ele","Molly"]

# print(names[1::3])

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num[-8:-2:2])

# items = ['first', 'second', 'third', 'fourth']
# print(items[::-1])

# movies = ['Inception', 'Titanic', 'Avatar', 'The Godfather', 'Pulp Fiction']
# print(movies[-4:-1])

# [start:end:steps]

# how to find the length of the list

# num = [ 17,14,23,11,12,30]
# print(len(num))



# today we learn about how to print the list with the loops

# num = [ 17,14,23,11,12,30]
# for i in num:
#     print(i)

# movies = ['Inception', 'Titanic', 'Avatar', 'The Godfather', 'Pulp Fiction']
# for i in movies:
#     print(i)

# num = [ 17,14,23,11,12,30]
# piggy_bank = 0

# for i in num:
#     piggy_bank = piggy_bank + i

# print(f"The sum of the list is {piggy_bank}")


# import random 

# choices = ["Rock","Paper","Scissors"]

# def determine_winner(player,computer):
#     if player == computer:
#         return "It's a tie"
#     elif (player == "Rock" and computer == "Scissors") or \
#         (player == "Scissors" and computer == "Paper") or \
#         (player == "Paper" and computer == "Rock"):
#         return "Daddada wins"
#     else:
#         return "Computer wins"



# while True:
#     # user choices
#     user_choice = input("Enter Rock, Paper & Scissors (or 'quit' to exit ) : ")
#     if user_choice == 'quit':
#         print("Thanks for playing!")
#         break
#     elif user_choice not in choices:
#         print("Invalid Choice. Please try it again.")
#         continue 
#     # computer choices

#     computer_choice = random.choice(choices)
#     print(f"Computer Choice : {computer_choice}")

#     result = determine_winner(user_choice,computer_choice)
#     print(result)
#     print()

# change the element of the list

# names = ["Navya","John","Robert","James","Austin"]
# names[0:2] = "Utkarsh"

# print(names)

# add the element into the list 

# We have two ways to do it 

# 1. append() -  It adds the element into the last of the list 

# names = ["Navya","John","Robert","James","Austin"]
# names.append("Utkarsh")

# print(names)

# 2. insert() -  it helps you to adds the element into the specific position

# names = ["Navya","John","Robert","James","Austin"]
# names.insert(1,"Utkarsh")

# print(names)

# Remove the element from the list

# We have again two ways to remove the element 

# 1. remove() - It removes the specific element from the list 


# names = ["Navya","John","Robert","James","Austin"]
# names.remove("Robert")

# print(names)

# 2. pop() - It helps you to rmeove the element from the list by specifying the index of the element. And if you are not specifying the index it will remove the last element of the list

# names = ["Navya","John","Robert","James","Austin"]
# names.pop(2)

# print(names)



# 2. tuple - It also stores multiple element in it.
# It is immutable (CAN'T BE CHANGED)
# It's identified by ()

# names = ("Navya","James","Tony","David","Jessica")
# print(names)

# names = ("Navya","James","Tony","David","Jessica")

# for i in names:

#     print(i)


# names = ("Navya","James","Tony","David","Jessica")

# names[2] = "Austin"

# print(names)

# Type Casting 

# So changing the data type from one to another

# Tuple - > list 

# names = ("Navya","James","Tony","David","Jessica")
# print(f"Before : {names}")
# x = list(names)

# x[2] = "Austin"

# names = tuple(x)

# print(f"After : {names}")





# 3. set : - It's a set of item collected in a variables
# It doesn't allow duplicate values
# It is unindexed
# It is unordered
# It is identified when the elements are enclosed by {}

# fruits = {"Apples","Banana","Apples","Cherry","Blueberries","Pineapple","Pineapple","Cherry"}
# print(fruits)


# for accesing the sets 


# fruits = {"Apples","Banana","Apples","Cherry","Blueberries","Pineapple","Pineapple","Cherry"}

# for i in fruits:
#     print(i)

# remove duplicate elements 

# num = [1,4,8,9,5,2,4,9,63,12,1,4,58,25,28,5,2,5,4,5]

# ans = set(num)

# print(ans)

# 4. Dictionary     