# Python - It is easy to use and understand.

# our first program to print a message

# print("Welcome to Python Programming!!!")


# print("Welcome to the world of Python Programming!!!")


# print("my name is kwame")


# variables : it is used to store the data in the memory


# a = 10

# print(a)

# a = 10
# b = 10.5896
# c = "kwame"
# d = True

# Data types : It is used to specify the type of data that we are using in the program.

# 1. Integer (int) : It is used to store the whole numbers.
# Example : a = 10,b =-10,c = 0,etc

# 2. Float (float) : It is used to store the decimal numbers.
# Example : a = 10.5896, b = -10.5896, c = 0.0, etc

# 3. String (str) : It is used to store the characters.
# Example : a = "kwame", b = "python", c = "10", etc

# 4. Boolean (bool) : It is used to store the True or False values.
# Example : a = True, b = False, etc

# a = -9 # integer
# name = "kwame" # string
# pi = 3.14895247 # float
# is_student = True # boolean

# comments in python : It is used to write the comments in the program.

# single line comment

# multi line comment
# '''
# i moew
#  oeinm e
#   oinemp 
#   m ioems

# '''

# operators and operands: 

# a+b

# operator : +
# operands : a,b

# Operators : It is used to perform the operations on the operands.

# 1. Arithmetic operators : It is used to perform the arithmetic operations.

# a. Addition (+) : It is used to add the two operands.
# b. Subtraction (-) : It is used to subtract the two operands.
# c. Multiplication (*) : It is used to multiply the two operands.
# d. Division (/) : It is used to divide the two operands.
# e. Modulus (%) : It is used to find the remainder of the two operands.
# f. Exponentiation (**) : It is used to find the power of the two operands.
# g. Floor division (//) : It is used to find the quotient of the two operands.

# a = 48
# b = 58
# print(ga+b)


# a =36
# b =52
# print (a-b)

# g =24
# h =46
# print (g*h)

# I =90
# j =50
# print (I/j)

# Note : Python is case sensitive language.

# i and I

# o =92
# c =54
# print (o%c)


# b =36
# c =22
# print (b**c)

# a =112
# c=56
# print (a//c)


# Conditional statements : It is used to perform the operations based on the conditions.

# 1. if statement : It is used to execute the block of code when the condition is True.

# Syntax:

# if condition:
    # block of code


# age = 19
# if age>18:
#     print("You are eligible for driving!!!")

# 2. if-else statement : It is used to execute the block of code when the condition is True and another block of code when the condition is False.

# age = 18
# if age>18:
#     print("You are eligible for driving!!!")
# else:
#     print("You are not eligible for driving!!!")

# 3. if elif else: It is used to execute the block of code based on the multiple conditions.

# if condition:
#     block of code
# elif condition:
#     block of code
# else:
#     block of code

# age = 15
# if age>18:
#     print("You are eligible for driving!!!")
# elif age == 18:
#     print("You are eligible for driving!!!")
# else:
#     print("You are not eligible for driving!!!")


# age = 15
# if age>18:
#     print("you are eligable for driving")
# elif age == 18:
#      print ("you are eligable for driving")
# else:
#      print ("you are not  eligable for driving")


# a = 5
# b = 51
# if a>b:
#     print("a is greater than b")
# elif a == b:
#     print ("a is equal to b")
# else:
#     print ("a is less than b")

# num = 16
# if num%2==0:
#     print("Even Number!!!")
# else:
#     print("Odd Number!!!")





# If we want to check positive or negative number

# a = 16
# if a > 0:
#     print("Positive Number!!!")
# else:
#     print("Negative Number!!!")


# loops: It is used to execute the block of code multiple times.

# 1. for loop : It is used to iterate over the sequence.

# Syntax:

# for variable_name in range(start,end,step):
#     block of code

# for i in range(1,11,1):
#     print(i)
    
# 2. while loop : It is used to execute the block of code until the condition is True.



# num = int(input("Enter the number of which you want the multiplication table of : "))

# for i in range(1,11):
#     print(num," X ",i," = ",num*i)


# 8 * 1 = 8
# 8 * 2 = 16



# while loop:

# We are either known about the starting point or the ending point 

# while conditions:
#     statements


# 1 2 3 4 5 6 7 8 9 10

# i = 1

# while i <= 10:
#     print(i)
#     i = i + 1  

# 10 11 12 13 14 15 16 17 18 19 20

# 10 9 8 7 6 5 4 3 2 1 

# 5 10 15 20 25 30 35 40 45 50


# 123 => 321

# num = int(input("Enter the number : "))
# ans = 0
# while num > 0:
#     rem = num%10      # num = 1 % 10 = 1
#     ans = ans * 10 + rem   # ans = 32*10+1 = 321
#     num = num // 10    # num = 12//10 = 1

# print("The reverse of the number is ",ans)


# Number guessing game

# random module

# import random

# num = random.randint(1,30)
# print(num)


# import random

# print("Welcome to the Number Guessing Game!!!")
# print("You have only 5 chances to guess the number between 1 to 30")

# secret_number = random.randint(1,30)

# attempts = 0
# max_attempts = 5

# while attempts<5:

#     guess = int(input("Guess the number : "))
#     attempts = attempts + 1

#     if guess == secret_number:
#         print(f"Congratulation, You've won the game in {attempts} attempts.")
#         break
#     elif guess > secret_number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low")

# if attempts == max_attempts:
#     print(f"Game Over !!! . The secret number is {secret_number}")


# 0 1 1 2 3 5 8 13 21 34 

# prev = 0
# current = 1

# print(prev,current,end=" ")

# for i in range(2,10):
#     next = prev+current
#     print(next,end=" ")
#     prev = current
#     current = next