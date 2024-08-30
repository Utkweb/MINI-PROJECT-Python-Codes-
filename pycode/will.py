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