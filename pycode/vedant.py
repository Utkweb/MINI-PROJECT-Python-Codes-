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

# l1 = [1,-8,9,-4,7,8,-2,-3,6,4,8,10]

# sum = 0 
# for i in l1:
#     if i > 0:
#         sum = sum + i

# print(f"The sum of all positive numbers in the list is : {sum}")


# 10 9 8 7 6 5 4 3 2 1


# syntax:

# for variable_name in range(start,end,step):
#     statements

# for i in range(10,0,-1):
#     print(i,end=" ")

# 0 5 10 15 20 25 30 35 40 45 50
# sum =0 
# for i in range(1,51):
#     sum = sum+i
# print(sum)

# List - it is used to store multiple values in a single variable.

# list is mutable.
# it is represented by [].

# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = ["Vedant","Utkarsh","Vishal","Vikas","Vivek"]
# l3 = [1.54,2.45,3.45,4.56,5.67]
# l4 = [True,False,True,False]
# l5 = [1,2,3,4,5,6,7,8,9,10,"Vedant","Utkarsh","Vishal","Vikas","Vivek",1.54,2.45,3.45,4.56,5.67,True,False,True,False]


# How we can access the data in the list?

# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# print(cars[1])

# slicing - it is used to get the subset of the list.

# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# print(cars[1:3])

# Change the value in the list

# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# cars[1] = "Mercedes"

# print(cars)

# Add a new item in the list

# append() - it is used to add an element at the end of the list.
# insert() - it is used to add an element at a specific index.

# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# cars.append("Mercedes")

# print(cars)

# cars = ["Ford", "Volvo", "BMW", "Toyota"]

# cars.insert(2,"Mercedes")

# print(cars)

# Delete the element in the list

# remove() - it is used to remove the element from the list.
# pop() - it is used to remove the element from the list.

# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# cars.pop(2)

# print(cars)


# if you wanna find out the length of the list how can you find it?

# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# print(len(cars))

# names = ["Anvi","Levin","Nidhi","Arnav","Utkarsh"]


# Nested Loops:

# for rows in range(1,6):
#     for columns in range(1,6):
#         print("*",end=" ")
#     print()

# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5


# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * * 

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# num = 1
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(num,end= " ")
#         num +=1
#     print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10


# Sorting algorithms :-


# 1. Ascending order
# 2. Descending order

# Techniques of sorting:-

# 1. Bubble sort


# def bubble_sort(lst):
#     for x in range(len(lst)-1,0,-1):
#         for y in range(x):
#             if lst[y] > lst[y+1]:
#                 lst[y],lst[y+1] = lst[y+1],lst[y]

#     return lst

# lst = [15,5,20,35,2,42,67,17,8,9]
# print("Unsorted list :",lst)

# print("Sorted list :",bubble_sort(lst))

# def bs(arr, target):
#     l, r = 0, len(arr) - 1

#     while l <= r:
#         mid = l + (r - l) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return -1

# arr = [53, 64, 73, 85, 87, 91, 93, 97]
# target = 90

# index = bs(arr, target)
# if index != -1:
#     print("Element found at index", index)
# else:
#     print("Element not found")


# Insertion sort - it is a simple sorting algorithm that builds the final sorted array one item at a time.


# def IS(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i -1

#         while j>=0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr

# arr = [14,46,43,27,57,41,45,21,70]

# print("Unsorted list :",arr)

# print("Sorted list :",IS(arr))

# GUI - Graphical User Interface

# from tkinter import *

# root = Tk()

# root.title("Vedant's GUI")
# root.geometry("400x400")

# l1 = Label(root,text="Sign Up",font=("Arial",20))
# l1.pack()

# l2 = Label(root,text="Name ",font=('Arial',10))
# l2.pack()

# e1 = Entry(root)
# e1.pack()

# b1 = Button(root,text="Submit",fg='white',bg='green',font=('Arial',12))
# b1.pack()

# root.mainloop()



# First Name
# Last Name
# Email
# Pasword
# Confirm Password

# Submit



# from tkinter import *

# root = Tk()

# root.title("Calculator")
# root.geometry("300x300")

# t1 =Text(root,height=2,width=45)
# t1.grid(row=0,column=0,columnspan=3)

# l1 = Button(root,text="1",height = 2,width = 8,fg="black",bg="white")
# l1.grid(row=2,column=0)

# l2 = Button(root,text="2",height = 2,width = 8,fg="black",bg="white")
# l2.grid(row=2,column=1)

# l3 = Button(root,text="3",height = 2,width = 8,fg="black",bg="white")
# l3.grid(row=2,column=2)

# l4 = Button(root,text="4",height = 2,width = 8,fg="black",bg="white")
# l4.grid(row=3,column=0)

# l5 = Button(root,text="5",height = 2,width = 8,fg="black",bg="white")
# l5.grid(row=3,column=1)

# l6 = Button(root,text="6",height = 2,width = 8,fg="black",bg="white")
# l6.grid(row=3,column=2)

# l7 = Button(root,text="7",height = 2,width = 8,fg="black",bg="white")
# l7.grid(row=4,column=0)

# l8 = Button(root,text="8",height = 2,width = 8,fg="black",bg="white")
# l8.grid(row=4,column=1)

# l9 = Button(root,text="9",height = 2,width = 8,fg="black",bg="white")
# l9.grid(row=4,column=2)

# root.mainloop()


# import tkinter as tk 


# temp = tk.Tk()
# temp.title("Temperature Converter")


# def ftoc():
#     f = temp1.get()
#     c = (5/9) * (float(f) - 32)
#     temp2["text"] = f'{round(c, 2)}\N{DEGREE CELSIUS}'


# frame = tk.Frame(temp)
# frame.grid(row=0, column=0, padx=10)


# temp1 = tk.Entry(frame, width=10)
# temp1.grid(row=0, column=0)


# f_label = tk.Label(frame, text="\N{DEGREE FAHRENHEIT}")
# f_label.grid(row=0, column=1)


# button = tk.Button(temp, text="\N{RIGHTWARDS BLACK ARROW}", command=ftoc)
# button.grid(row=0, column=1, pady=10)


# temp2 = tk.Label(temp, text="\N{DEGREE CELSIUS}")
# temp2.grid(row=0, column=2, padx=10)


# temp.mainloop()




# def find_max(l1):
#     max = l1[0]

#     for i in l1:
#         if i > max:
#             max = i
#     return max

# l1 = [1,2,3,4,5,25,84,7,8,9,10]
# print("The maximum value in a list :",find_max(l1))


# sqaures = {i:i**2 for i in range(1,6)}


# for key,value in sqaures.items():
#     print(f"{key} : {value}")


# def is_palindrome(str1):
#     if str1.lower() == str1[::-1].lower():
#         return "Yes, it is a palindrome"
#     return "No, it is not a palindrome"

# str1 = "Malayalam"

# print(is_palindrome(str1))


# student_scores = [("Vedant", 40), ("Utkarsh", 0), ("Vishal", 70), ("Vikas", 60), ("Vivek", 50)]

# sorted_ss = sorted(student_scores,key=lambda x : x[1],reverse=True)

# for student,scores in sorted_ss:
#     print(f"{student} : {scores}")


# import tkinter as tk

# def button_click():
#     label.config(text="Button Clicked")

# root = tk.Tk()
# root.title("Example")

# root.geometry("400x400")

# label = tk.Label(root,text="")

# button = tk.Button(root,text="Click Me",command = button_click)

# label.pack(pady = 20)
# button.pack(pady = 20)

# root.mainloop()



# Module - mysql.connector

# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="utkarsh"
# )

# if mydb.is_connected():
#     print("Connected to the database")



# from tkinter import * 
# from tkinter import messagebox
# import mysql.connector


# def signup():
#     username = e1.get()
#     password = e2.get()

#     if not username or not password:
#         messagebox.showwarning("Input error","All fields are required!")
#         return 
    
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database = "utkarsh"
#     )

#     if mydb.is_connected():
#         cursor = mydb.cursor()
#         cursor.execute('Insert into users (username,password) values (%s,%s)',(username,password))

#         mydb.commit()
#         messagebox.showinfo("Success"," Signup Successful")
# root = Tk()
# root.title('Sign Up Page')
# root.geometry('400x300')

# l1 = Label(root,text="Username")
# l1.pack()

# e1 = Entry(root)
# e1.pack()

# l2 = Label(root,text="Password")
# l2.pack()

# e2 = Entry(root)
# e2.pack()


# b1 = Button(root,text="Create Account",bg="green",fg="white",command =signup)
# b1.pack()
# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
# import mysql.connector


# def signup():
#     FN = e1.get()
#     LN = e2.get()
#     Email = e3.get()
#     password = e4.get()
#     CP = e5.get()

#     # Check if any field is empty
#     if not FN or not LN or not Email or not password or not CP:
#         messagebox.showwarning("Input error", "All fields are required")
#         return
    
#     # Check if passwords match
#     if password != CP:
#         messagebox.showerror('Error', "Password doesn't match")
#         return

#     # Connect to the database
#     try:
#         mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="utkarsh"
#         )

#         if mydb.is_connected():
#             cursor = mydb.cursor()

#             # Insert data into the database
#             cursor.execute(
#                 'INSERT INTO users (FN, LN, Email, password, CP) VALUES (%s, %s, %s, %s, %s)', 
#                 (FN, LN, Email, password, CP)
#             )
            
#             mydb.commit()
#             messagebox.showinfo("Success", "Signup Successful")

#     except mysql.connector.Error as err:
#         messagebox.showerror('Database Error', f"Error: {str(err)}")


# # Create the main window
# root = Tk()
# root.title("Hacker's GUI")
# root.geometry("400x400")

# # Create and pack widgets
# l1 = Label(root, text="Sign Up", font=("Arial", 20))
# l1.pack()

# l2 = Label(root, text="First Name", font=("Arial", 10))
# l2.pack()
# e1 = Entry(root)
# e1.pack()

# l3 = Label(root, text="Last Name", font=("Arial", 10))
# l3.pack()
# e2 = Entry(root)
# e2.pack()

# l4 = Label(root, text="Email", font=("Arial", 10))
# l4.pack()
# e3 = Entry(root)
# e3.pack()

# l5 = Label(root, text="Password", font=("Arial", 10))
# l5.pack()
# e4 = Entry(root, show='*')  # Hide password input
# e4.pack()

# l6 = Label(root, text="Confirm Password", font=("Arial", 10))
# l6.pack()
# e5 = Entry(root, show='*')  # Hide confirm password input
# e5.pack()

# b1 = Button(root, text='Create Account', fg='white', bg='Green', font=('Arial', 15), command=signup)
# b1.pack()

# root.mainloop()

# import mysql.connector
# from tkinter import *
# from tkinter import messagebox

# # MySQL connection
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="user_info"
# )
# cursor = conn.cursor()

# def inputError():
#     if enterTaskField.get() == "":
#         messagebox.showerror("Input Error", "Please enter a task")
#         return 0
#     return 1

# def clear_taskNumberField():
#     taskNumberField.delete(0.0, END)

# def clear_taskField():
#     enterTaskField.delete(0, END)

# def insertTask():
#     global counter
#     value = inputError()
#     if value == 0:
#         return
    
#     content = enterTaskField.get()

    
#     cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (content,))
#     conn.commit()

   
#     cursor.execute("SELECT id, task FROM tasks ORDER BY id DESC LIMIT 1")
#     result = cursor.fetchone()

#     task_id = result[0]
#     task_content = result[1]

#     TextArea.insert('end', "[ " + str(task_id) + " ] " + task_content + "\n")
#     clear_taskField()

# def deleteTask():
#     global counter
#     if taskNumberField.get(1.0, END).strip() == "":
#         messagebox.showerror("Input Error", "Please enter a task number")
#         return
    
#     task_no = taskNumberField.get(1.0, END).strip()
#     clear_taskNumberField()

#     try:
#         task_id = int(task_no)
#         cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
#         conn.commit()

        
#         TextArea.delete(1.0, END)
#         cursor.execute("SELECT id, task FROM tasks")
#         for task in cursor.fetchall():
#             TextArea.insert('end', "[ " + str(task[0]) + " ] " + task[1] + "\n")
#     except ValueError:
#         messagebox.showerror("Input Error", "Invalid task number")

# def loadTasks():
#     cursor.execute("SELECT id, task FROM tasks")
#     for task in cursor.fetchall():
#         TextArea.insert('end', "[ " + str(task[0]) + " ] " + task[1] + "\n")

# if __name__ == "__main__":
#     gui = Tk()
#     gui.configure(background="light green")
#     gui.title("ToDo App")
#     gui.geometry("250x300")

#     enterTask = Label(gui, text="Enter Your Task", bg="light green")
#     enterTaskField = Entry(gui)
#     Submit = Button(gui, text="Submit", fg="Black", bg="Red", command=insertTask)
#     TextArea = Text(gui, height=5, width=25, font="lucida 13")
#     taskNumber = Label(gui, text="Delete Task Number", bg="blue")
#     taskNumberField = Text(gui, height=1, width=2, font="lucida 13")
#     delete = Button(gui, text="Delete", fg="Black", bg="Red", command=deleteTask)
#     Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=gui.quit)

#     enterTask.grid(row=0, column=2)
#     enterTaskField.grid(row=1, column=2, ipadx=50)
#     Submit.grid(row=2, column=2)
#     TextArea.grid(row=3, column=2, padx=10, sticky=W)
#     taskNumber.grid(row=4, column=2, pady=5)
#     taskNumberField.grid(row=5, column=2)
#     delete.grid(row=6, column=2, pady=5)
#     Exit.grid(row=7, column=2)

#     loadTasks()  
#     gui.mainloop()

    
#     cursor.close()
#     conn.close()



# from tkinter import *
# from tkinter import messagebox
# import pyperclip
# import string
# import random

# def gen_pwd():
#     length = pass_len.get()
#     inc_upper = include_uppercase.get()
#     inc_lower = include_lowercase.get()
#     inc_digits = include_number.get()
#     inc_symbols = include_symbol.get()

#     if not (inc_upper or inc_lower or inc_digits or inc_symbols):
#         messagebox.showwarning("Selection Error","Select at least one option!")
#         return 
    
#     char = ""
#     if inc_upper:
#         char = char + string.ascii_uppercase
#     if inc_lower:
#         char = char + string.ascii_lowercase
#     if inc_digits :
#         char = char + string.digits
#     if inc_symbols:
#         char = char + string.punctuation
    
#     password = ''.join(random.choice(char) for _ in range(length))
#     pwd_entry.delete(0,END)
#     pwd_entry.insert(0,password)



# def copy_pwd():
#     password = pwd_entry.get()
#     if password :
#         pyperclip.copy(password)
#         messagebox.showinfo("Copied","Password copied to clipboard!")
#     else:
#         messagebox.showwarning("No Password","Generate a password first")

# root=Tk()
# root.title("Tech Code Yeah")
# root.geometry("500x300")
# label=Label(root,text="Password Length :")
# label.pack()

# pass_len = IntVar(value=8)
# Scale(root,from_=4,to_=32,orient=HORIZONTAL,variable=pass_len).pack()

# include_uppercase = BooleanVar()
# include_lowercase = BooleanVar()
# include_number = BooleanVar()
# include_symbol = BooleanVar()


# check=Checkbutton(root,text="Upper Case Letter's",variable=include_uppercase)
# check.pack()
# check1=Checkbutton(root,text="Lower Case Letter's",variable=include_lowercase)
# check1.pack()
# check2=Checkbutton(root,text="Numbers",variable=include_number)
# check2.pack()
# check3=Checkbutton(root,text="Symbols",variable=include_symbol)
# check3.pack()

# pwd_entry = Entry(root)
# pwd_entry.pack(pady = 10)

# Button(root,text="Generate Password",command=gen_pwd).pack(pady=10)
# Button(root,text="Copy Password",command=copy_pwd).pack(pady=10)
# root.mainloop()


# Snake Game :

# A food for snake.
# if it hits the walls and eats itself game over
# increase the length by 1 when it eats 
# a background
# snake 
# score 
# start button 


import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

root = turtle.Screen()
root.title("Snake Game")
root.bgcolor("black")
root.setup(width=600, height=600)
root.tracer(0)

# Snake's head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'pink', 'orange', 'white', 'yellow'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0   High Score : 0", align="center", font=("Arial", 24, "bold"))

# Key direction functions
def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

def goRight():
    if head.direction != "left":
        head.direction = "right"

# Move function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Bind keys
root.listen()
root.onkeypress(goUp, "w")
root.onkeypress(goDown, "s")
root.onkeypress(goLeft, "a")
root.onkeypress(goRight, "d")

segments = []

# Main game loop
while True:
    root.update()
    move()  # Ensure move() is called in the loop to keep the snake moving

    # Check for collisions with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'green', 'pink', 'orange', 'white', 'yellow'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    # Move the end segments first in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check for collision with self
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'green', 'pink', 'orange', 'white', 'yellow'])
            shapes = random.choice(['square', 'triangle', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    time.sleep(delay)

root.mainloop()
