# we are running our first code in python
# print("Welcome to Vedant's world!")

# Data Types:

# 1. int  (integer) - a whole number, positive or negative, without decimals, of unlimited length. Examples include -9, 0, and 42.
# 2. float (floating point number) - a number, positive or negative, containing one or more decimals. Examples include -9.2, 0.0, and 42.0.
# 3. string - a sequence of characters (text). Examples include "hello", 'hello', and "42".
# 4. boolean - a binary value that can be either True or False. Example: is_human = True


# a = True
# print(type(a))

# syntax:

# variable_name = datatype(input("Enter the value:"))

# example:
    
# a = (input("Enter the value:"))
# print(a)


# operators and operands

# a+b

# operands - a, b
# operators - +


# # Arithmetic operators: +, -, *, /, %, **, //
# a=int(input("Enter value a : "))
# b=int(input("Enter Value b : "))
# print(f"Addition of two numbers are : {a+b}")


# a = 4
# b = 2
# print(a**b)



# a = 4897

# print(a//100)


# a = 89
# b = 78


# a = a+b    #a = 16
# b = a-b    #b = 9
# a = a-b    #a = 7

# print(a,b)

# * //

# a=a*b/9
# b=a*9/7
# print(a,b)


# a = 7
# b = 9



# Conditional statemens :

# 1. if statement

# if condition:
#     statement1
#     statement2
#     statement3
#     statement4
#     statement5


# example:

# age = int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible for voting.")


# 2. if-else statement

# if condition:
#     statement1
#     statement2
#     statement3
#     statement4
#     statement5
# else:
#     statement6
#     statement7
#     statement8
#     statement9
#     statement10

# example:

# age = int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible for voting.")
# else:
#     print("You are not eligible for voting.")


# 3. if elif else statement

# syntax:

# if condition1:
#     statement1
#     statement2

# elif condition2:
#     statement3
#     statement4

# elif condition3:
#     statement5

# else:
#     statement6
#     statement7

# example:
    
# age = int(input("Enter your age: "))
# if age>18:
#     print("You are eligible for voting.")
# elif age == 18:
#     print("You are eligible for voting but you are not an adult.")
# else:
#     print("You are not eligible for voting.")


# loops:  loop or looping


# Python loops:

# two types of loop:

# 1. for loop
# 2. while loop

# for loop:

# syntax:

# for variable_name in range(start,end,step):
#     statements

# example: 1 2 3 4 5 6 7 8 9 10

# for i in range(1,11,1):
#     print("Vedant")


# 0 1 2 3 4 5 6 7 8 9

# module - > we need to import that particular module

# import random

# num = random.randint(1,10)

# print(num)

# name = "Vedant"
# print(name)

# name = "Vedant"
# print(name[2].upper())

# name  = "Utkarsh"
# print(name[5].upper())


# sentence = "Welcome to today's class we are learning about String today."
# print(sentence[-1])

# how we can find the length of the string

# sentence = "Welcome to today's class we are learning about String today."
# print(len(sentence))

# how we are going to slice ?

# sentence = "Welcome to today's class we are learning about String today."
# print(sentence[0:7])


# sentence = "Welcome to today's class we are learning about String today."

# name = str(input("Enter a name : "))
# a=int(input("type a random number"))
# print(name[::-a])

# formatting Strings

# My name is Utkarsh and I'm 20 years old.

# name = "Utkarsh"
# age = 20

# print("My name is ",name," and I'm ",age," years old.")

# print(f"My name is {name} and I'm {age} years old")

# String Methods:

# 1. upper() - It converts the string into uppercase.

# name = "vedant"
# print(name[0].upper()+name[1:])

# 2. lower() - It converts the string into lowercase.
# name = "Vishal"
# print(name.lower())

# 3. count():

# string.count(value,start,end)


# a  = "I love apple, apple are my favorite fruit"
# print(a.count("e"))


# islower() - it is used to check whether the string is in lowercase or not.

# name = "Utkarsh"
# print(name.islower())

# isupper() - it is used to check whether the string is in uppercase or not.
# name = "Utkarsh"
# print(name.isupper())


# name ="Utkarsh"
# print(name.count("a,e,o,i,u"))



# name = "Vedant"
# vowel_count = 0
# consonant_count = 0
# for i in name:
#     if i == "a" or i =="e" or i=="i" or i=="o" or i == "u":
#         vowel_count=vowel_count+1
#     else:
#         consonant_count = consonant_count+1
        
# print(f"Vowel count is {vowel_count} and consonant count is {consonant_count}")


# we are going to learn about the arrays : -

# arrays :-
# (i) list
# (ii) tuple
# (iii) set
# (iv) dictionary


# (i)  List  : it is a data type in python which is used to store multiple values in a single variable.
#  In list, we can store multiple values like integer, float, string, boolean etc.
# list is mutable.
# you can identify that the particular variable is a list by [].

# example: -

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = ["Vedant","Utkarsh","Vishal","Vikas","Vivek"]
# list3 = [1.54,2.45,3.45,4.56,5.67]
# list4 = [True,False,True,False]
# list5 = [1,2,3,4,5,6,7,8,9,10,"Vedant","Utkarsh","Vishal","Vikas","Vivek",1.54,2.45,3.45,4.56,5.67,True,False,True,False]

# if you wanna check the datatype you can use the type() function.

# list1 = [1,2,3,4,5,6,7,8,9,10]

# print(type(list1))

# if you wanna print the list then you can use the print() function.

# list1 = [1,2,3,4,5,6,7,8,9,10]

# print(list1)

# list2 = ["Vedant","Utkarsh","Vishal","Vikas","Vivek"]
# for i in list2:
#     print(i)

# list1 = [1,2,3,4,5,6,7,8,9,10]


# output - 1,8,27,64,125,216,343,512,729,1000

# How we can access the elements or values in a list?

# list2 = ["Vedant","Utkarsh","Vishal","Vikas","Vivek"]
# print(list2[0:3])

# Change list elements:-

# thislist = ["apple", "banana", "cherry"]
# thislist[0:2] =["orange","kiwi"]

# print(thislist)

# Add a new item or element in the list:-

# so for adding we are having to methods in the list:-
# (1) append() - it is used to add an element at the end of the list.

# list1 = ["tesla","Honda","Nissan","Jeep","Ford"]
# list1.append("chervolett")

# print(list1)


# (2) insert() - it is used to add an element at a specific index.


# list1 = ["tesla","Honda","Nissan","Jeep","Ford"]
# list1.insert(3,"chervolett")

# print(list1)

# Delete the element in the list?

# list1 = ["tesla","Honda","Nissan","Jeep","Ford"]
# # list1.remove("tesla")
# list1.pop(2)

# print(list1)


# if you want to find out the length of the list how can you find it?

# list1 = ["tesla","Honda","Nissan","Jeep","Ford"]
# print(len(list1))

# the list constructor :-

# list1 = list(("tesla","Honda","Nissan","Jeep","Ford"))
# print(type(list1))


# list1 = ["tesla","Honda","Nissan","Jeep","Ford"]


# check if item exists or not :-

# list1 = ["tesla","Honda","Nissan","Jeep","Ford"]

# if "Benz" in list1:
#     print("Yes, 'Benz' is in the list")
# else:
#     print("The car brand is not in the list")

# Membership Operators:

# in - Returns True if a sequence with the specified value is present in the object
# not in - Returns True if a sequence with the specified value is not present in the object


# Sorting

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)




# import random

# def user_choice():
#     user = input("Enter your choice from ('rock','paper','scissor') : ").lower()
#     while user not in ['rock','paper','scissor']:
#         print("Invalid choice!!!!")
#         user = input("Enter your choice from ('rock','paper','scissor') : ").lower()
#     return user

# def bot_choice():
#     return random.choice(['rock','paper','scissor'])

# def win(user_choice,bot_choice):
#     if user_choice == bot_choice:
#         return ""Tie
#     elif (user_choice == 'rock' and bot_choice == 'scissor') or \
#         (user_choice == 'scissor' and bot_choice == 'paper') or \
#             (user_choice == 'paper' and bot_choice == 'rock'):
#                 return "User Wins"
#     else:
#         return "Bot Wins"
    
# def play_game():
#     print("Welcome to the Game of Rock, Paper & Scissor : ")
#     while True:
#         user = user_choice()
#         bot = bot_choice()
        
#         print(f"User choice : {user}")
#         print(f"Bot Choice : {bot}")
        
#         print(win(user,bot))
#         play = input("Do you wanna play the game again (yes/no) : " ).lower()
#         if play!='yes':
#             print("Thanks for playing up the game !!!!!!!!!")
#             break
# play_game()

# Funtions :-A function is block of code which only runs when it is called.

# print("Welcome ot the class Vedant")

# defining a function   
# def square(a):
    
#     print(f"Square of the number is : {a**2}")
    
# # calling a function
# a = int(input("Enter the number : "))
# square(a)


# def my_function(f):
#   print(f + " Refsnes")


# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# parameters and arguments


# defining a function 
# def add(a,b):
#     return a+b

# # calling a function
# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# print(f"Addition of two numbers is : {add(a,b)}")


# Lambda -  A lambda is a small anonymous function 


# Syntax:

# lambda arguments: expression

# x = lambda a,b : a+b

# print(x(5,6))



# tuple: they are also used to store multiple values
# tuple is immutable
# A tuple is a collection which is ordered and unchangeable
# tuple are written with round brackets ().

# thistuple = ('UNO','Mercedes','ferrari')
# print(type(thistuple))


# how you can find the length of the tuple?
# thistuple = ('UNO','Mercedes','ferrari')
# print(len(thistuple))

# tuple1 = ('vedant',)
# print(type(tuple1))

# tuple1 = ("apple","banana","cherry")
# tuple2 = (1,5,7,9,5)
# tuple3 = (True,False,True)


# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1[-1])

# how we can slice up the tuple?

# tuple1 = ("apple","banana","cherry","orange","kiwi","melon","mango")
# print(tuple1[2:])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])


# type casting : it badically converts the variable from one data type to another

# x = ("apple","banana","cherry")
# y = list(x)
# y[1] = "mango"
# x=tuple(y)
# print(x)


# x = ("apple","banana","cherry")
# for i in x:
#     print(i)

# x = ("apple","banana","cherry")
# for i in range(len(x)):
#     print(x[i])


# join the tuples:


# tuple2 = ('A','B','C')



# print(tuple2*3)

# count() - it helps you to tell the frequency of a particular element that you have asked for.

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# print(thistuple.count(5))

# index() - it basically helps us to know the index of a particular element

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(thistuple.index("kiwi"))

# set , dictionaries


# list : it is indentified by []. it is mutable. 
# tuple : it is identified by (). it is immutable.

# reversing up a string

# name = "Vedant"
# print(name[::-1])

# firstname = "Vedant"
# lastname = "Goswami"

# # concatention
# print(firstname+lastname)

l1 = [1,-8,9,-4,7,8,-2,-3,6,4,8,10]

sum = 0 
for i in l1:
    if i > 0:
        sum = sum + i

print(f"The sum of all positive numbers in the list is : {sum}")