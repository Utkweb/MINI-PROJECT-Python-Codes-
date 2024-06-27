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


# name = "     Utkarsh       "
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




# import random


# def user_choice():
#     user = input("Enter your choice ['rock','paper','scissor']").lower()
#     while user not in ['rock','paper','scissor']:
#         print("Invalid choice!!!!!!!")
#         user = input("Enter your choice ['rock','paper','scissor']").lower()
#     return user

# def bot_choice():
#     return random.choice(['rock','paper','scissor'])

# def win(user_choice,bot_choice):
#     if user_choice == bot_choice:
#         return "TIE"
#     elif (user_choice == 'rock' and bot_choice == 'scissor') or \
#     (user_choice =='scissor' and bot_choice == 'paper' ) or \
#         (user_choice == 'paper' and bot_choice=='rock'):
#             return "User Wins"
#     else:
#         return "Bot Wins"
    
# print("Welcome to the Rock Paper Scissor Game")
# score = 0
# while True:
#     user = user_choice()
#     bot = bot_choice()
    
#     print("User choice is :",user)
#     print("Bot choice is :",bot)
    
#     result = win(user,bot)
    
#     if result == 'User Wins':
#         score = score+1
    
    
#     print(score)
        
    
    
#     play = input("Do you wanna play again ? (yes/no)").lower()
#     if play != 'yes':
#         print("Thanks for playing the game!")
#         break



# arrays  : 
    
# 1. list
# 2. tuple
# 3. dictionary
# 4. set


# List : It is represented by [].

# example : cars = ['BMW','Toyota','Mercedes','Honda']
# List are mutable.
# List can have multiple duplicate items

# cars = ['BMW','Toyota','Mercedes','Honda']
# print(cars)

# cars = ['BMW','Toyota','Mercedes','Honda']
# print(cars[2])

# cars = ['BMW','Toyota','Mercedes','Honda']
# print(type(cars))

# cars = ['BMW','Toyota','Mercedes','Honda']
# cars[3] = 'Audi'

# print(cars)


# Membership Operators

# in - it tells you whether a particular items that you are searching for is present in a list or not.
# not in - 


# cars = ['BMW','Toyota','Mercedes','Honda']

# if 'BMW' in cars:
#     print('Yes')

# cars = ['BMW','Toyota','Mercedes','Honda']

# cars[1:3] = ['Maruti','Ferrari']

# print(cars)

# insert - it add
# append - 

# cars = ['BMW','Toyota','Mercedes','Honda']
# cars.insert(2,'Ferrari')

# print(cars)

# cars = ['BMW','Toyota','Mercedes','Honda']
# # cars.remove('Mercedes')
# cars.pop()
# print(cars)

    # cars = ['BMW','Toyota','Mercedes','Honda']
    # cars.clear()

    # print(cars)
    

# loop list:

# cars = ['BMW','Toyota','Mercedes','Honda']

# for x in cars:
#     print(x)


# sum = 0
# lst = [10,9,3,2,1]
# for x in lst:
#     sum = sum+x
    
# print("The sum of all elements in a list", sum)

# lst = [10,9,14,2,71]
# min = lst[0]

# for x in lst[1:]:
#     if x<min:
#         min = x

# print(min)


# max = lst[0]

# for x in lst[1:]:
#     if x<max:
#         max = x

# print(max)


# lst = [10,9,14,2,71]
# for x in lst:
#     print(x)

# for i in range(start,end,step):

# lst = [10,9,14,2,71]

# for i in range(len(lst)-1,-1,-1):
#     print(lst[i],end=" ")
    
# sorting - 

# 1. bubble sort : - 

# arr = [64, 34, 25, 12, 22, 11, 90]

# # j = 0 

# # arr[j] = 64
# # arr[j+1] = 34

# n = len(arr)   #7

# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]


# print(arr)


# arr = [2,4,2,12,5,8,9,1,1,4,2,9]

# # # empty list
# l1 = []

# i = 0

# while i < len(arr):
#     if arr[i] in l1:
#         arr.remove(arr[i])
#     else:
#         l1.append(arr[i])
#         i = i+1
# print(arr)


# You need to understand the bubble sort and write it approximately 5 times.


# l1 = ["aaryaki","utkarsh"]
# l1[1]= "mukherjee"

# print(l1)


# tuples are immutable.
# they are identified by ().
# syntax:

# t1 = ("apples","pineapple")
# t1[1] = "Watermelon"

# print(t1)


# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# type casting : - It changes the datatype of a particular variables

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple)

# l1 = list(thistuple)
# l1[-3] = "watermelon"

# thistuple = tuple(l1)

# print(thistuple)


# t1 = (1,2,3)
# t2 = ('a','b','c')

# print(t1+t2)


# loops with tuples:

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# for i in thistuple:
#     print(i)


# t1 = ("aaryaki","mukherjee")
# print(t1*5)


# count() -> 
# index() ->

# t1 = (1,2,3,4,2,4,5,8,9,0)
# print(t1.index(9))


# Python Sets : It is represented by {}.

# A set is a collection which is unordered, unchangeable and unindexed.

# l1  = {"apples","apples","mango","banana","kiwi"}
# print(l1)

# s1 = {"Mercedez",1,10.5,True}

# How to find the length?

# l1  = {"apples","apples","mango","banana","kiwi"}
# print(len(l1))

# Access items

# l1  = {"apples","apples","mango","banana","kiwi"}
# for i in l1:
#     print(i)

# l1  = {"apples","apples","mango","banana","kiwi"}

# print("pineapple" not in l1)

# add items

# l1  = {"apples","apples","mango","banana","kiwi"}
# l1.add("pineapple")


# print(l1)

# to add items from another set into the current set, use the update() method.

# l1  = {"apples","apples","mango","banana","kiwi"}
# l2 = ["pineapple","watermelon","kiwi","banana","banana"]

# l1.update(l2)

# print(l1)

# l1  = {"apples","mango","kiwi"}
# l1.remove("banana")

# print(l1)

# remove() - removes the specified item
# discard() - removes the specified item but if the item is not present in the set, it will not throw an error.


# clear() - empties the set

# l1  = {"apples","mango","kiwi","banana","pineapple","watermelon","kiwi","banana","banana"}

# del l1

# print(l1)

# JavaScript cool projects :

# 1. To do list
# 2. Weather app
# 3. Calculator
# 4. Quiz app
# 5. Chat app


# celsiuis to fahrenheit conversion


# def c_to_f(temp):

# fahrenheit to celsius conversion