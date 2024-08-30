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

import random

print("Welcome to the Number guessing game!!!")
print("You need to guess the number between 1 to 30")
print("You have only 3 attempts")


secret_number = random.randint(1,30)
attempts = 0

max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Enter your guess : "))

    attempts = attempts+1
    if guess == secret_number:
        print("You won the Jackpot")
        break
    elif guess>secret_number:
        print("Too high.. Try again!!!")
    else:
        print("Too low.. Try again!!!")
        
    if attempts == max_attempts:
        print("ohhoooo You lost the game !!!!!!!!!!!. The sceret number is",secret_number)
        break
