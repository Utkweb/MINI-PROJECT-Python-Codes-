# Python - To solve the problems and for making the projects as well.

# 8th grade

# Variable : 

# a = 15,"Pratik"

# Data types:

# We are having four data types:

# 1. Integer (int) : It stores without decimals.
# example: a = 5, num = 98,etc.

# 2. Float (float) : It stores numbers with decimals 
# ex: pi = 3.14,etc.

# 3. String (str) : It stores characters,sentences and even words.
# ex: name = "Pratik", word = "Python",etc

# 4. Boolean (bool) : It stores two values either True or False
# ex: flag = True,flag = False,etc.

# type() : It helps you to identify the data is of which type

# a = True
# print(type(a))

# a+b 

# Operands = a,b
# and operators = +


# Operators : 

# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Exponential (**)
# 6. Floor Division (//)
# 7. Modulus (%)

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# print("The sum of two numbers is : ",a+b)


# base = int(input("Enter the base : "))
# power = int(input("Enter the power : "))

# print(base**power)

# a  = 9 
# b = 2

# print(a%b)

# Input

# a = 9
# b = 4

# output:

# a = 4
# b = 9


# a = int(input("Enter the value of a : "))  #9
# b = int(input("Enter the value of b : "))  #2

# a = a+b  #11
# b = a-b  #9
# a = a-b  #2

# print("a : ",a)
# print("b : ",b)

# You need to use * and // 

# Conditional statements

# 1. If statement : It helps you to check one condition at a time

# syntax:

# if condition:
    # statements

# age = int(input("Enter your age for license verification : "))

# if age > 18:
#     print("You are allowed to drive the car")

# 2. If-else statements - It helps you to check two condition at a time

# syntax:

# if condition:
    # statements
# else:
#     statements

# age = int(input("Enter your age for license verification : "))

# if age > 18:
#     print("You are allowed to drive the car")
# else:
#     print("You are not allowed to drive the car")

# 3. If-elif-else: It helps you to check multiple condition at a time

# syntax:

# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# age = int(input("Enter your age for license verification : "))

# if age > 18:
#     print("You are allowed to drive the car")
# elif age == 18:
#     print("You just got eligible for driving the car")
# else:
#     print("You are not allowed to drive the car")

# you need to take two values from user and needs to check which value is the greater one


# Loops : for loops and while loop


# for loops

# syntax:

# for variable_name in range(start,end,steps):
#     statements

# for i in range(1,11,5):
#     print(i)


# 1 3 5 7 9 11 13 15 17 19 21

# 0 2 4 6 8 10 12 14 16 18 20

# 5 10 15 20 20 25 30 35 40 45 50

# 10 9 8 7 6 5 4 3 2 1 0

# 1 4 9 16 25 36 49 64 81 100

# 8 X 1 = 8

# num = int(input("Enter the number of which you want the multiplication number of :"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# while loop : 

# initialization 
# while condition:
#     statements

# 1 - 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1


# 1 - 10 = 55

# piggy_bank = 0
# for i in range(1,11):
#     piggy_bank = piggy_bank + i

# print("The sum of all elements in the list : ",piggy_bank)


# 567% = 7*10 = 70+6=76*10=760+5=765
# 56%10 = 6

# 5%10 = 5

# 765


# num = int(input("Enter the number to make it reverse : "))  #num = 123
# ans = 0
# while num != 0:
#     rem = num % 10    # rem = 1% 10 = 1
#     ans = ans * 10 + rem   #ans = 321
#     num = num // 10   #num = 1

# print(f"The reverse : {ans}")


# 854 = 8+5+4 =     


# == : used for comparing 
# != : not equals to 


# 0 1 1 2 3 5 8 13 21 34 55

# prev = 0
# current = 1

# print(prev,current,end= " ")

# for i in range(2,101):
#     next = prev + current 
#     print(next,end= " ")
#     prev = current    #prev = 1
#     current = next   #current = 2

# 0 1 1 2 3 5 8

# import random 

# print("Welcome to number guessing game!!!")

# max_chances = 5

# chances = 0

# secret_number = random.randint(1,30)

# while chances < max_chances:
    
#     guess = int(input("Guess the number : "))
#     chances = chances + 1

#     if guess == secret_number:
#         print("COngrats")
#         break
#     elif guess > secret_number:
#         print("Guess to high")
#     else:
#         print("Guess too low")

# if chances == max_chances:
#     print("You ran out of chances")




# num = int(input("Enter the number : "))

# count = 0

# for i in range(2,(num//2+1)):
#     if num % i == 0:
#         count = count + 1


# if count == 0:
#     print("The number is prime")
# else:
#     print("The number is not prime")



# Strings : Any characters ,words or sentences are said to be as strings 

# name = "Utkarsh Singh"

# index :

# 1. positive indexing - it starts from left to right from 0 to n-1
# 2. Negative indexing - It starts from right to left from -1 to -n


# print(name[-1])

# Slicing 

# print(name[::2])

# printing in reverse order
# print(name[::-1])

# [:end:steps]

# len() - it helps you to find the length of the string 

# name = "Pratik Karki"
# print(f"The length of {name} is {len(name)}")

# count = 0 

# for i in name:
#     count = count + 1

# print(f"The length of {name} is {count}")


# Arrays: It stores mutliples elements in it 

# 1. List - It allow duplicate elements to store 
# It is mutable
# It is being identified as or enclosed by []

# num = [7,8,9,5,3,4,1,2,6,9,8]
# names = ["Pratik","Utkarsh","David","Jessica","Julia"]
# radius = [47.8,85.3,9.04,55.63,77.49]
# flag = [True,False,False,False,True]

# student_info = ["Pratik",14,75.2,"Fairfes",True]


# names = ["Pratik","Utkarsh","David","Jessica","Julia"]
# # print(names[2])
# print(names[1:4])


# num = [7,8,9,5,3,4,1,2,6,9,8]
# for i in num:
#     print(i)

# num = [7,8,9,5,3,4,1,2,6,9,8]
# sum = 0 
# for i in num:
#     sum = sum + i 
# print(f"The sum of all element in a list are {sum}")


# Write a program to identify how many even and odd numbers are there in the list 

# 2. Tuple
# 3. Set
# 4. Dictionary 


# 5 = 5*4*3*2*1



# num = [7,8,9,5,3,4,1,2,6,9,8]

# max = num[0]

# for i in num:
#     if max < i:
#         max = i

# print(f"The maximum number in the list is : {max}")


# names = ["Pratik, Utkrash, David, Ryan, Emily, Matthew, Laith, Brandon"]
# v_count = 0
# vowels = "aeiouAEIOU"
# for i in names:
#     if i[0] in vowels:
#         v_count = v_count + 1
# print(f"The ammount of names starting up with vowels are {v_count}")