# Variables - 

# Rules for variable names:
    
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. Variable names cannot contain spaces
# 6 Variable names should be descriptive and meaningful (a variable name like x is not descriptive)

# a = 10
# age = 20

# Data Types -

# Python has the following data types built-in by default, in these categories:

# 1. Integer(int) - Whole numbers, positive or negative, without decimals, of unlimited length.
# example : x = 1, y = 35656222554887711, z = -3255522

# 2. Float(float) - Floating point numbers, positive or negative, containing one or more decimals.
# example : x = 1.10, y = 1.0, z = -35.59

# 3. String(str) - A string in Python is a sequence of characters.
# example : x = "hello", y = 'Kareena', z = "hello"

# 4. Boolean(bool) - Boolean represents one of two values: True or False.

# print("Hey, Kareena how are you?")



# type() - # The type() function returns the data type of the specified object.

# a = False
# print(type(a))

# Operators/operands:

# a+b 

# Operands = a, b
# Operator = +

# Arithmetic Operators:

# 1. Addition (+) - Adds two operands
# 2. Subtraction (-) - Subtracts right operand from the left operand
# 3. Multiplication (*) - Multiplies two operands
# 4. Division (/) - Divides left operand by right operand
# 5. Modulus (%) - Divides left operand by right operand and returns remainder
# 6. Exponent (**) - Performs exponential (power) calculation on operators
# 7. Floor Division (//) - The division of operands where the result is the quotient in which the digits
#  after the decimal point are removed.


# a = 10
# b = 20

# print("Addition :",a+b)


# a = 10
# b = 20


# print("")

# a = 9
# b = 5

# when i print a and b then their values need to be swapped 

# a = 9 - 4 = 5

# only need to use a and b and + and -

# // and *

# a = 9
# b = 5

# a = a*b   #a = 45
# b = a//b   #b = 9
# a = a//b   #a = 5
# a,b = b,a

# print('a :',a)
# print('b :',b)

# Conditional Statements:-

# 1. if statments -checks only 1 condition at a time 

# syntax :

# if condition:
#     statements

# age = int(input("Enter the age of the person : "))

# if age>17:
#     print("you are eligible to drive car")

# 2. if else statements - checks two condition at a time 

# if condition:
#     statments
# else:
#     statements


# age = int(input("Enter the age of the person : "))

# if age>17:
#     print("you are eligible to drive car")
# else:
#     print("You are not eligible to drive the car")

# a = 8
# b = 7


# if elif else statements - it helps you to check three or more condition at a time 

# if conditons:
#     statements
# elif condition:
#     statements
# else:

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# if a>b:
#     print("a greater")
# elif a == b:
#     print("Both are equal")
# else:
#     print("b greater")


# a = 5
# b = 9

# # a needs to be greater than b or less than or equals to 5

# if a>b or a <=5:
#     print("Yes ")

# if a>b and a>c:
#     print("a is greatwe")


# strings : it stores words, sentences and characters

# name = "circumstances"

# index : it helps you to get in touch with each character of the string

# print(name[-2])

# name= "Utkarsh"

# print(name[0:3])

# Concatenation - 

# adding two things together 
# firstName = "Utkarsh "
# lastName = "Singh"


# print(firstName*4)


# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")

# loops:

# 1. for loop

# syntax : 

# for i in range(start,end,step):
#     System.out.println("Kareena")

# for i in range(1,101):
#     print(i,".Kareena")

# 1 10

# 2. while loop


# for i in range(1,101,1):
#     print(i)

# 1 + 2+ 3+... +10  = 55

# piggy_bank = 0 
# for i in range(1,11):
#     piggy_bank = piggy_bank+i
# print("The total sum of elements are : ",piggy_bank)

# 8 X 1 = 8
# 8 X 2 = 16


# formatting up a string


# num = int(input("Enter the value : "))

# print(f"The multiplication table of {num}")

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")



# factorial = 

# 5! = 5*4*3*2*1 = 120

# num = int(input("Enter the number : "))
# piggy_bank = 1
# for i in range(1,num+1):
#     piggy_bank = piggy_bank * i

# print(f"The factorial of {num} is {piggy_bank}")


# 2. while loop

# while condition:
#     statements


# 1 - 10

# i = 10
# while i <= 51:
#     print(i)
#     i = i+1   #i =11

# 10 51


# 123 -> 321

# 3*10 = 30+2 = 32*10 = 320 +1 = 321

# num = 123

num = int(input("Enter the number : "))
ans = 0
while num>=0:
    rem = num % 10  #rem = 1
    ans = ans*10+rem   #ans = 321
    num = num // 10    #num = 1

print(ans)

