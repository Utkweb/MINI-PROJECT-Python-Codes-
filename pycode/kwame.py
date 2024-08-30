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



num = int(input("Enter the number of which you want the multiplication table of : "))

for i in range(1,11):
    print(num," X ",i," = ",num*i)


# 8 * 1 = 8
# 8 * 2 = 16