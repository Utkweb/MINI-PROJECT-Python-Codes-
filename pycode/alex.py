# variables:

# valid variables :
# n =5
# a=7
# name = "Alex"

# invalid variables:
    
# 1n = 5
# $ = 7
# _name = "Alex"

# datatypes:
    
# Integer -> int(-inf to +inf)
# Float -> float(1.2, 3.4, 5.6)
# String -> str("Alex","123","4")
# Boolean -> bool(True, False)



# operands and operators:

# a+b

# operands -> a,b
# operator -> +
 
# a*b

# operands -> a,b
# operators -> *


# print("Welcome to the first class of python")

# name = "Alex"
# print(name)

# Operators: 

# 1. Arithmetic Operators: +, -, *, /, %,//, **

# a = 10

# b = 9

# print("Addition:",a+b)


# a = 10
# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))

# print("Addition:",a+b)



# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))

# print("Division",a/b)
# print("Modulus",a%b)
# print("Floor Division",a//b)

# ** -> Exponentiation

# 4**2 = 16

# 4**2 = 4*4 = 16
# 4**3 = 4*4*4 = 64

# base = int(input("Enter the base value:"))
# exponent = int(input("Enter the exponent value:"))

# print("Exponentiation:",base**exponent)


# Ques 1-> Write a program to take two numbers from the user and print the sum,multiplication,division,modulus,subtraction,floor division of those numbers.


# # input

# a = 7
# b = 9


# # output:

# a = 9
# b = 7


# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))

# a = a+b    # a = 7+9 = 16
# b = a-b    # b = 16-9 = 7
# a = a-b    # a = 16-7 = 9

# print("a:",a)
# print("b:",b)


# // *


# Conditional Statements:

# 1. if statements
# 2. if else statements
# 3. if elif else statements

# 1. if statements:
    
# Syntax:
    
# if condition:
#     statements

# a = int(input("Enter the value of a : "))
# print(a)


# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))
# print(a + b)


# a is greater than b

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))

if a > b:
    print("a is greater than b")