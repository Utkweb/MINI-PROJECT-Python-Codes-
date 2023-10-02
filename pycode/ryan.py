# Python - It is a high-level, interpreted, interactive and object-oriented scripting language.


# Example -
# print("Hello World")

# compiler - It is a program that converts the code written in a high-level language to a low-level language.

# Interpretor - It is a program that converts the code written in a high-level language to a low-level language line by line.


# Data Types - 

# 1. Numbers - int, float, complex
# 2. String - str
# 3. Boolean - bool True/False 0/1

# Keywords - it is a reserved word in python. It cannot be used as a variable name, function name or any other identifier.

# comments - #, ''' ''' , """ """


# # 
# print("Hello World")


# a = True

# print(type(a))

# a = 9
# b = 2

# print("The power : ",a**b)

# format String 

# /
# // - floor division

# operators:
    
#     1. Arithmetic Operators - +, -, *, /, %, //, **


# My favorite subjects are Maths, Science and English.


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print("The sum is: ",a+b)


# conditional statements - if, if-else, if-elif-else


# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print(num, "it is the multiple of 2")

# a = 9
# b =27

# if a>b:
#     print("a is greater than b")
#     if a%2 == 0:
#         print("a is even")
# elif a<b:
#     print("a is less than b")
# else:
#     print("a is equal to b")
    

# loops:- for, while

# for variable in range(1,10,2):
#     statement1


# for i in range(0,11,2):
#     print(i,end=" ")


# variable declaration 
# while condition:
#     statements
#     inc/dec

# piggy_bank = 0
# i = 0
# while i<10:
#     piggy_bank = piggy_bank + i
#     piggy_bank += i
#     i+=1
# print(piggy_bank)

# 1 - 20

# even_sum = 0
# odd_sum = 0
# for i in range(1,21):
#     if i%2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
# print("The sum of even numbers: ",even_sum)
# print("The sum of odd numbers: ",odd_sum)    
    
# num1 =42
# num2 = 120


# num1 = 120
# num2 = 42


# num1 = int(input("Enter a number: "))  
# num2 = int(input("Enter a number: "))    

# num1  = num1 + num2     
# num2 = num1 - num2      
# num1 = num1 - num2     

# print("The value of num1: ",num1)
# print("The value of num2: ",num2)   


# 1 - 10

# piggy_bank = 0
# for i in range(1,12,2):
#     piggy_bank += i
# print("The sum of odd numbers: ",piggy_bank)


# Nested Loops:-

# Week 1:
#     Day 1:-
#     Day 2:-
#     Day 3:-
#     Day 4:-
#     Day 5:-
#     Day 6:-
#     Day 7:-
# Week 2:


# for var in range(start,end,step):
#     for var in range(start,end,step):
#         statement1
#         statement2
#         statement3
#     statement4
#     statement5
#     statement6

# for i in range(1,4):
#     for j in range(1,5):
#         print(i," ",j)
        
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()



# fibonacci series:-
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# num1 = 0    
# num2 = 1
# result = 0

# print(num1," ",num2,end=" ")
# for i in range(1,11):
#     result = num1+num2
#     print(result,end=" ")
#     num1 = num2
#     num2 = result

# 123 -->  321
# 345 -->  543

# Random generator - random module

# import math 

# print(math.sqrt(25))

# Random Module - it is a module that is used to generate random numbers.

# pip install name_of_module

# import random

# num = random.randint(1,11)
# print(num)


# randint(start, end) - it is a function that is used to generate random integer numbers.
# randrange(start, end, step) - it is a function that is used to generate random integer numbers.

# randrange(1,11,3)

# 1 4 7 10

# Random Genrator Game:- 

# import random

# # starting point
# start = int(input("Enter the lower bound: "))

# # ending point
# end = int(input("Enter the upper bound: "))

# num = random.randint(start,end)

# print("You have only 5 chances to guess the number.")

# count =0

# while count<5:
#     print("Chance: ",count+1)
#     guess = int(input("Enter your guess:"))
    
#     count+=1
    
#     if guess == num:
#         print("Congratulations! You guessed the number right.")
#     elif guess<num:
#         print("Your guess is too low.")
#     elif guess>num:
#         print("Your guess is too high.")
#     else:
#         print("Invalid Input.")


# Type casting: - it is a process of converting one data type to another data type.

# 1. implicit 
# 2. explicit
# int --> float
# float --> int
# int --> str
# str --> int
# str --> float
# float --> str

# a = 4
# print("Before the casting",type(a))  

# # type casting
# b = str(a)
    
# print("After the casting",type(b))  
# print(b)


# a = 4.5   -> str
# name = "R" ->int
# num =20 -> float

# name = "R"
# print("Before the casting",type(name))

# # type casting
# num = int(name)

# print("After the casting",type(num))
# print(num)

# type caste to integer from string 

# n = "20"
# print("Before the casting",type(n))

# # type casting
# num = int(n)

# print("After the casting",type(num))
# print(num)

# Strings - it is a sequence of characters enclosed within single quotes or double quotes or triple quotes.

# 'hello' "hello" '''hello'''

# name = "Ryan"
# print(name)

# multiline string
# sent = '''




# '''

# index - it is a position of a character in a string.

# name = "Ryan Joseph"

# print(name[5:])