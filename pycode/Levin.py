# Python : - It is a high-level, interpreted, interactive and object-oriented scripting language. 1Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.

# print("Welcome to the class of the Python Programming")

# variables and data types :- 

# variables : - A variable is a name given to a memory location. It is the basic unit of storage in a program. The value stored in a variable can be changed during program execution.

# data types : - Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

# Data types:-

# 1. Integer (int) : - It is a whole number, positive or negative, without decimals, of unlimited length. eg. 10, -20, 1000, 1000000,etc.

# 2. Float (float) : - It is a number, positive or negative, containing one or more decimals. eg. 1.5, 10.5, 20.5, etc.

# 3. String (str) : - It is a sequence of characters enclosed within single quotes, double quotes, or triple quotes. eg. "Anvi", 'Nidhi', "Riya", etc.

# 4. Boolean (bool) : - It is a data type that can have one of two values, either True or False.

# a = True
# print(type(a))

# Operators and Operands :-

# a+b

# Operator : - An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations. Python language supports the following types of operators.

# 1. Arithmetic Operators : - Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

# a. Addition (+) : - It is used to add two operands.
# b. Subtraction (-) : - It is used to subtract the right operand from the left operand.
# c. Multiplication (*) : - It is used to multiply two operands.
# d. Division (/) : - It is used to divide the left operand by the right operand.
# e. Floor Division (//) : - It is used to divide the left operand by the right operand and return the integer value.
# f. Modulus (%) : - It is used to return the remainder of the division.
# g. Exponent (**) : - It is used to raise the left operand to the power of the right operand.

# a = str(input("Enter the first number: "))
# print(type(a))


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# print("The addition of two numbers is: ",a+b)


# Conditional Statements :-

# 1. if statement : - It is used to check a condition. If the condition is true, the code block will be executed.

# Syntax:

# if condition:
#     statements

# 2. if else statement : - It is used to check a condition. If the condition is true, the code block inside the if statement will be executed, otherwise the code block inside the else statement will be executed.

# Syntax:

# if condition:
#     statements
# else:
#     statements

# 3. if elif else statement : - It is used to check multiple conditions. If the condition in the if statement is false, it will check the condition in the elif statement. If the elif statement is also false, the code block inside the else statement will be executed.

# Syntax:

# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# age = int(input("Enter your age: "))

# if age>18:
#     print("You're eligible to drive")
# elif age == 18:
#     print("You're a teenager")
# else:
#     print("You're not eligible to drive")

# 1. Take two inputs from users and check which one is greater, or if they are equal.

# Python Loops :-

# 1. for loop : - It is used to iterate over a sequence (list, tuple, string) or other iterable objects.
    
# 2. while loop : - It is used to execute a block of statements repeatedly until a given condition is true.


# for loop :

# # Syntax:

# for variable in range(start,stop,step):
#     statements

# for i in range(10,0,-1):
    # print(i,end=" ")

# print("Welcome to the class of the Python Programming",end=" ")
# print("Let's start the class of the Python Programming")

# 10 9 8 7 6 5 4 3 2 1

# formatting up th string 

# name = "Levin"
# print(f"Hello {name}")

# 1. Print the multiplication table of a given number using for loop.

# 8X1=8
# 8X2=16
# 8X3=24
# 8X4=32
# 8X5=40
# 8X6=48
# 8X7=56
# 8X8=64
# 8X9=72
# 8X10=80


# while loop :

# Syntax:

# while conditions:
#     statements


# for i in range(1,11):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1 #i+=1

# num = int(input("Enter the number: "))

# count = 0
# for i in range(2,num):
#     if num%i==0:
#         count+=1

# if count==0:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


# 0 1 1 2 3 5 8 13 21 34 55 89

# num = int(input("Enter the number to be reversed: "))  # 123

# ans = 0

# while num!=0:
#     rem = num%10   # 3
#     ans = ans*10+rem  # 0*10+3=3
#     num = num//10  # 12

# print(f"The reversed number is: {ans}")

# 153 = 1^3+5^3+3^3 = 153