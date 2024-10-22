# Python : 

# it is easy to use 
# it is easy to learn
# it is case sensitive

# i,I


# print("Welcome to Python Programming")

# Varibles - it is a container that stores data values

# how we cn initialize the variables:


# a = 10
# print(a)

# comments : it is a way to write notes in the code

# 1. Single line comment : #

# 2. Multi line comment : ''' ''' or """ """

# a = 10
# pi =3.14785
# name = "Kwarteng"
# is_student = True

# data types : 

# 1. integer (int) : it is a whole number
# Example : 10, 20, 30, 40, 50,etc.

# 2. float : it is a number with decimal point
# Example : 10.5, 20.5, 30.5, 40.5, 50.5, etc.

# 3. string (str) : it is a collection of characters
# Example : "Kwarteng", "Python", "Programming", "10", "20", etc.

# 4. boolean (bool) : it is a data type that has only two values

# True : 1
# False : 0

# Operators and operands

# a+b

# a and b are operands
# + is the operator

# Operator : it is a symbol that performs an operation

# 1. Arithmetic Operators :

# a. Addition : +
# b. Subtraction : -
# c. Multiplication : *
# d. Division : /
# e. Modulus : %
# f. Exponentiation : **
# g. Floor Division : //


# a = 48
# b = 88
# print("Addition :",a+b)

# conditional statements : it is used to make decisions in the program

# 1. if statement : it is used to check a condition

# syntax:

# if condition:
#     statement


# age = 19
# if age > 18:
#     print("You are an adult")

# 2. if else statement : it is used to check two conditions

# syntax:

# if condition:
#     statement
# else:
#     statement

# age = 17
# if age > 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# 3. if elif else statement : it is used to check multiple conditions

# syntax:

# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# age = 18
# if age > 18:
#     print("You are an adult")
# elif age == 18:
#     print("You are a teenager")
# else:
#     print("You are a minor")

# a = 58
# b = 15

# print("Kwarteng")

# loops: it is used to repeat a block of code multiple times

# 1. for loop : it is used to iterate over a sequence

# syntax:

# for varaibble_name in range(start,end,step):
#     block of code

# for i in range(1,101,1):
#     print(i)

# 2. while loop : it is used to repeat a block of code as long as the condition is true


# 8 X 1 = 8
# 8 X 2 = 16
# 8 X 3 = 24

# num = int(input("Enter the number of which you want the multiplication table of : "))
# print("Multiplication table of ",num,"\n")
# for i in range(1,11):
#     print(num," X ",i," = ",num*i)


# 1 2 3 4 5 6 7 8 9 10


# for i in range(1,11):
#     print(i)


# 2 4 6 8 10 12 14 16 18 20  -- Done

# 5 10 15 20 25 30 35 40 45 50  --Done

# for i in range(5,51,5):
#     print(i)

# 10 9 8 7 6 5 4 3 2 1 

# for i in range(10,0,-1):
#     print(i)

# 1 4 9 16 25 36 49 64 81 100

# for i in range(1,11):
#     print(i**2)

# 1*1 = 1
# 2*2 = 4
# 3*3 = 9
# 4 = 16
# 5 = 25 
# 6 = 36 
# 7 = 49 
# 8 = 64
# 9 = 81
# 10 = 100



# 1+2+3+4+5+6+7+8+9+10 = 55

# piggy_bank = 0
# for i in range(1,11):
#     piggy_bank = piggy_bank+i

# print(piggy_bank)


# 5! = 5*4*3*2*1 = 120

# num = int(input("Enter the number : "))
# fact = 1

# for i in range(1,num+1):
#     fact = fact * i 

# print(fact)


# while loop : We arr either not known about the starting or the ending point

# while condition:
#     statements


# 1 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i+1


# 123 => 321

# 123 % 10 = 3 * 10 = 30 + 2 =32*10 = 320+1 =321
# 12 % 10 = 2 

# 1 % 10 = 1

# num = int(input("Enter the number : "))    #num = 123
# ans = 0
# while num > 0:
#     rem = num % 10     # rem = 1 % 10 = 1
#     ans = ans * 10 + rem   #ans = 32*10+1 = 321
#     num = num // 10     #num = 12//10 = 1


# print("The reverse number is",ans)


# 324 = 3+2+4=9

# 0 1 1 2 3 5 8 13 21 34 


# prev = 0
# current = 1

# print(prev,current, end = " ")
# for i in range(2,10):
#     next = prev+current
#     print(next,end =" ")
#     prev = current
#     current = next


# Number Guessing game :

# random module

# import random

# num = random.randint(1,30)
# print(num)


# import random 

# print("Welcome to the Number Guessing Game 🔢")
# print("You have only 5 chances. The number is in between 1 to 30")

# secret_number = random.randint(1,30)
# attempts = 0
# max_attempts = 5

# while attempts < 5:
#     guess = int(input("Guess the number : "))
#     attempts = attempts + 1

#     if guess == secret_number:
#         print(f"Congratulation you won the game in {attempts} attempts.")
#         break
#     elif guess > secret_number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low")

# if attempts == max_attempts:
#     print(f"You've lost the game. The secret number is {secret_number}.")


# four data types :

# int
# float
# string
# boolean



# 1. list - it is used to store multiple items in one variable
# The list is enclosed by []
# It allows duplicate values


# example:

# num = [1,2,3,4,5,6,7,8]
# num1 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0]
# num2 = ["Kwame","Kwarteng","Kwaku","James","Bob"]
# num3 = [True, False]

# num4 = ["Kwame",14,34.8,True]



# num = [1,2,3,4,5]

# print(num[-1])


# index 

# 1. Positive index - it always start from zero
# 2. Negative index - it starts from the backwards of th list and it starts with -1




# 2. tuple
# 3. set
# 4. Dictionary


# slicing 

# num = [1,2,3,4,5,6,7,8,9,10]
# print(num[2:6])



# We are gonna access the list with loops

# num = [1,2,3,4,5,6,7,8,9,10]

# for i in num:
#     print(i)

# num = [48,56,12,70,16,34,66,87,94]

# target = int(input("Enter the number to check :"))

# if target in num:
#     print("The number is present")
# else:
#     print("The number is not present")


# num = [48,56,12,70,16,34,66,87,94]
# WAP to find the count of even numbers and odd numbers are there in the above list?




# num = [48,56,12,70,16,34,66,87,94]
# even_count = 0
# odd_count = 0

# for i in num:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1


# print(f"The count of even number in the list are : {even_count}")
# print(f"The count of odd number in the list are : {odd_count}")


# Write a program to add all the number of the list?
# num = [48,56,12,70,16,34,66,87,94]


# Find the maximum and minimum number in the list ?


# remove duplicates 

