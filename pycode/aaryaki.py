# variables and datatypes:-

# variables = 10

# numbers,words,sentence = 10, "Hello", "Hello World"

# valid variables:-

# num,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z

# _,2,$

# num_1, num_2, num_3, num_4, num_5

# data types;-

# int = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# float = 10.20, 20.30, 30.40, 40.50, 50.60, 60.70, 70.80, 80.90, 90.100
# str = "Hello", "Hello World", "Hello World of Python"
# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# dict = {"name":"Aaryaki", "age":20, "city":"Delhi"}
# set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# bool = True, False


# a = "10.4"
# print(type(a))

# type()- to check the data type of a variable

# operands and operators:-

# a+b

# operators:
    
#     1. Arithmetic operators:-
#         +, -, *, /, %, //, **

# 2. Comparison operators:-
#     ==, !=, >, <, >=, <=
    
# 3. Logical operators:-
#     and, or, not

# 4. Assignment operators:-
#     =, +=, -=, *=, /=, %=, //=, **=

# 5. Identity operators:-
#     is, is not

# 6. Membership operators:-
#     in, not in

# 7. Bitwise operators:-
#     &, |, ^, ~, <<, >>




# a = (input("Enter the value of a : "))

# print(type(a))


# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# print("The summation of a and b is :",a+b)

# a = 6
# b = 6
# print(a+b)

# 4**2


# a = 8
# b = 9

# a = a+b
# b = a-b
# a = a-b

# print("a :",a)
# print("b :",b)


# *,//


# a = 10




# loops:

# for, while


# for loop:

# syntax:
    
# for variable_name in range(start,stop,step):
#     statements

# for name in range(1,101):
#     print("Aaryaki")
    
# 1 2 3 4 5 6 7 8 9 10

# for i in range(1,11,2):
#     print(i)


# 10 9 8 7 6 5 4 3 2 1

# for i in range(10,0,-1):
#     print(i)


# 2 4 6 8 10 12 14 16 18 20
# 5 10 15 20 25 30 35 40 45 50
# 1 4 9 16 25 36 49 64 81 100

# 0 1 1 2 3 5 8 13 21 34 55 89 144


# 1 2 3 4 5 6 7 8 9 10 = 55


# new_account = 0
# for i in range(1,11):
#     new_account = new_account+i
# print("The total sum of all the numbers from 1 to 10 is :",new_account)


# if elif else  => nested if else


# if inside the for loop:

# even_count = 0
# odd_count = 0

# for i in range(1,11):
#     if i%2==0:
#         even_count = even_count+1
#     else:
#         odd_count = odd_count+1
# print("The total number of even numbers are :",even_count)
# print("The total number of odd numbers are :",odd_count)


# for loop -> when you know the range
# while loop -> when you don't know the range

# example for while loop

# syntax:

# while condition:
#     statements (code to be executed)


# i = 10
# while i>=0:
#     print(i)
#     i=i-1

# 357 -> 3+5+7 = 15

# num = int(input("Enter the number: "))
# sum = 0

# while num>0:
#     rem = num%10  
#     sum = sum+rem 
#     num = num//10    
    
# print("The total sum of the digits is :",sum)

# reverse number
# 357 -> 753

# armstrong number:-

# 153 -> 1^3+5^3+3^3 = 153


# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 

# for 
# for



# random module  -> random number

# import random

# print(random.randint(1,20))


# number guessing game:-


# 1  50

# target = 45



# 1 50 

# 10
# too low

# import random

# secret_number = random.randint(1,50)

# print("Welcome to the number guessing game")
# print("You have to guess the number between 1 and 50")


# max_attempts = 10
# attempts = 0

# while attempts < max_attempts:
#     guess = int(input("Enter your guess: "))
#     attempts = attempts+1
    
#     if guess == secret_number:
#         print("Congratulations! You have guessed the correct number")
#         print("You have guessed the number in ",attempts)
#         break
#     elif guess<secret_number:
#         print("your guess is too low")
#     else:
#         print("your guess is too high")
        
# if attempts == max_attempts:
#     print("Sorry! You have exhausted all your attempts")



# Nested loops:-

# for variable_name in range(start,end,step):
#     for variable_name in range(start,end,step):
#         statements
        
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# for rows in range(1,6):
#     for columns in range(1,rows+1):
#         print(rows,end=" ")
#     print()
    

# 1
# 1 2





# print("Aaryaki",end="+")
# print("mukherjee")



#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *


# n = int(input("Enter the number of rows: "))

# # iterationg from 0 to n-1 0 - 6
# for i in range(n):
#     # print out the spaces
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("* ",end="")
        
#     print()



# cars = ["Audi","BMW","Mercedes","Toyota","Honda","Hyundai","Maruti","Tata","Mahindra","Ford"]


# print(cars)

# metadata = data of data

# how we can access the values?
# cars = ["Audi","BMW","Mercedes","Toyota","Honda","Hyundai","Maruti","Tata","Mahindra","Ford"]
# print(cars[4])

# slicing
# cars = ["Audi","BMW","Mercedes","Toyota","Honda","Hyundai","Maruti","Tata","Mahindra","Ford"]
# print(cars[3:6])
# print(cars[:6])

# how i can know the length of the list
# cars = ["Audi","BMW","Mercedes","Toyota","Honda","Hyundai","Maruti","Tata","Mahindra","Ford"]
# print("The length of the list :",len(cars))

# Q - In the below list you need to swap the first value and the last value of the list?

# input:
# cars = ["Audi","BMW","Mercedes","Toyota","Honda","Hyundai","Maruti","Tata","Mahindra","Ford"]


# Output:
# cars = ["Ford","BMW","Mercedes","Toyota","Honda","Hyundai","Maruti","Tata","Mahindra","Audi"]



# Patterns: - 

# ******
# *    *
# *    *
# *    *
# *    *
# ******


# for rows in range(0,5):
#     for columns in range(0,5):
#         if rows == 4 or rows == 0 or columns == 0 or columns == 4:
#             print("*",end= " ")
#         else:
#             print(" ",end= " ")
#     print()
    
# *******
# *******
# *******
# *******
# *******
# *******
# *******



#      *
#     **
#    ***
#   ****
#  *****
# ******



# functions: it helps to reduce the redundancy of the code.

# syntax:

# defining up a funtion
# def function_name(a,b):
#     print("Hello World")

# #main funtion

# function_name()     # calling a function


# def add(a,b):
#     print(a+b)
    

# #main function
# # a = int(input("Enter the value of a: "))
# # b = int(input("Enter the value of b: "))
# add(8,7)
# add(10,20)
# add(30,40)


# str1 = "Hello World"
# str2 = "Hello World of Python"

# print(str1.concat(str2))


# String reversal 

# def rever



# adding



# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# print(a+b)


# def add(a,b):
#     return (a+b)
    
# print(add(8,4))
# print(add(9,7))



# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i,"FizzBuzz")
#     elif i%5==0:
#         print(i,"Buzz")
#     elif i%3==0:
#         print(i,"Fizz")
#     else:
#         print(i)

# def fizbuzz(lr,ur):
#     for i in range(lr,ur+1):
#         if i%3==0 and i%5==0:
#             print(i,"FizzBuzz")
#         elif i%5==0:
#             print(i,"Buzz")
#         elif i%3==0:
#             print(i,"Fizz")
#         else:
#             print(i)

# # main fucntion

# lr = int(input("Enter the lower range: "))  
# ur = int(input("Enter the upper range: "))   

# fizbuzz(lr,ur)

# a = 3
# b = 9 
# c = 5

# print(a,b,c)


# Strings : -

# eg:-

# name = "Aaryaki"
# city = "Delhi"

# sentence = '''

#        1. Variables and Datatypes
#        2. Operators

# '''
# print(sentence)


# formatting up a string

# name = "Aaryaki"
# age = 20

# # print("My name is",name,"and I'm",age,"years old.")
# print(f"My name is {name} and I'm {age} years old.")
# # output = My name is Aaryaki and i'm 20 years old

# name = "Utkarsh"
# print(name[2:5])

# print(name[-2])


# b = "Hello, World!"
# print(b[2:8])

# llo, w

# Convert the string into the upper case
# name = "UTKARSH"
# print(name.lower())


# strip -> removes the white spaces from the string


# name = "   Utkarsh       "
# print(name.strip())

# replace -> replaces the string with the new string

# name = "Aaryaki Nukherjee"
# print(name.replace("N","M"))

# Concatenation -> Add two strings together

# w1 = "hello"
# w2 = " what's up?"

# print(w1+w2)


# Escape Characters

# \n -> new line
# \t -> tab space

# print("Hello\tworld")

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



# rock rock = tie
# rock scissor || paper rock || scissor paper = "user wins"

# if user_choice == bot_choice :
#     tie
    
# elif 

# else:
#     bot wins