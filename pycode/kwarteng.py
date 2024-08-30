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

num = int(input("Enter the number of which you want the multiplication table of : "))
print("Multiplication table of ",num,"\n")
for i in range(1,11):
    print(num," X ",i," = ",num*i)