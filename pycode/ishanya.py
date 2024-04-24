# variables:- it is a container which stores some value in it.
# valid variable names:-

# num = 10
# _num =10 X
# 1num = 10 X

# a = 10  valid variable name

# data types:- 
# 1. int     -2147483647 to 2147483647
# 2. float   1.2, 2.3, 3.4, 4.5
# 3. str     "Shrika", "Anvi", "Rahul"
# 4. bool     True/False  1/0


# single line comment
# print("Hello, How are you?")

# '''



# '''


# Arithmetic Operators:-
# 1. +   Addition
# 2. -   Subtraction
# 3. *   Multiplication
# 4. /   Division
# 5. %   Modulus
# 6. //  Floor Division
# 7. **  Exponentiation

# a = 10
# b = 4

# print(a%b) --> remainder =2

# base = 4
# power = 2

# print(base**power)

# keywords/Reserved words/predifined words:- It is a word which is already defined in python.

# selection statements : if, if else, if elif elif elif .... else

# if statements:-

# Syntax of if statement:-

# if condition:
#     statement

# num = float(input("Enter a number:"))
# print(type(num))



# if num%5==0:
#     print("The number is divisible by 5")

# syntax of if else:-

# if condition:
#     statement
# else:
#     statement

# string formatting : %d, %f, %s

# num = 10
# print("The number is %d"%num)

# print($"The number is {num}")


# if elif else: 
    
# if condition:
#     statement
        # break
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement





# year = int(input("Enter a year:"))
# if year%4==0:
#     print("The year is leap year")
# else:
#     print("The year is not a leap year")

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))

# c = input("Enter a operator:")
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# else:
#     print("Invalid operator")

# break - it is used to terminate the loop

# if 10>5:
#     print("Hello")
#     break
#     print("Hi")

# loops:- for, while

# for loop:- it is used to iterate over a sequence(list, tuple, string, dictionary, set)

# syntax of for loop:-

# for variable in range(start,end,step):
#     statement

# 1 2 3 4 5 6 7 8 9 10


# money_saver  = 0
# for i in range(1,11):
#       money_saver = money_saver+i    #1+2+3+4+5+6+7+8+9+10 =55
# print(money_saver)






# start
# i = 1
# if i<10
# print i
# end if

# i =1 
# if i<10:
#         print(i)


# function - it is a block of code which is used to perform a specific task.

# def - keyword
# def function_name():
#     statements



# defining a function
# def add(a,b):   #arguments
#         return a+b

# # main function

# print("Hello")

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# # calling a function
# print(add(a,b))   #parameters

# def square(num):
#         return num**2
        
# # main function
# num = int(input("Enter a number:"))
# print(square(num))
