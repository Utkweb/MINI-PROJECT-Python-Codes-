# Python -

# variables = 

# a = "Mannat"

# Data Types in Python

# 1. Integers:
    # a = 10
    # a = int(input("Enter a number: "))
    
# 2. Float: 
#     a = 10.5
#     a = float(input("Enter a number: "))

# 3. String

# a= "Welcome to the class of Python"
# a= input("Enter a string: ")


# 4. Boolean : 
    
    # a = True/False or 1/0
    
    
    
# # 5. List

# # a = [1.5,2.5,"flower",4,5,6,7,8,9,10]
# # a = list(input("Enter a list: "))   

# 6. Tuple
# 7. Dictionary
# 8. Set



# a=9
# b=4
# print(a%b)

# / - Division 
# // - Floor Division 
# % - Modulus

# operators & operands 

# 1. Arithmetic Operators

# P - Parenthesis (){}[]
# E - Exponent  **
# M - Multiplication *
# D - Division /
# A - Addition +
# S - Subtraction -


# 2. Assignment Operators

# = Assiginment Operator
 
# != Not Equal to

# += Addition Assignment Operator

# == Equal to

# a=5
# b=9

# a=a+b
# b=a-b
# a=a-b



# print(a,b)

# identifiers = variable names _ , 1, 


# keywords = reserved words in python
# example : int, input, print, if, else, elif, for, while, break, continue, pass, return, def, class, try, except, finally, raise, assert, import, from, as, with, in, is, del, global, nonlocal, lambda, or, and, not, True, False, None, yield, await, async,

# type cast the values: 
    
# a = True

# print(type(a))

# a = 9
# a = float(a)

# print(type(a))
# print(a)

# if statements 

# if condition:

# if (expression)):
#     # statements
#     print("This is if block")

# num = 15
# num1 = 15
# if num==num1:
#     print("You are in if block")

# if condition:
#     # statements
#     print("This is if block")
# else:
#     # statements
#     print("This is else block")


# if else statements

# age = 18
# if age>18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


# if elif elif .... else statements

# if condition:
#     # statements
#     print("This is if block")
# elif condition:
#     #statements
# elif condition:
#     #statements
# .
# .
# .
# .
# .
# else:
#     # statements
#     print("This is else block")

# age = 18
# if age>18 or age==18:
#     print("You are eligible to vote")
# elif age==18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# and - 
# or - 

# loops : for loop, while loop

# for loop: 

# Syntax:
    
#     for variable in sequence:
#         statements

# piggy_bank = 0
# for i in range(0,21,2):
#     print(i)

# user-input : 
    
# a = input("Enter a number: ")
# print(type(a))
    
# for loops : 

# n = int(input("Enter a number : "))
# cnt=0
# for i in range(1,n+1,2):
#     cnt+=i
# print("The sum of all odd number upto the given range : ",cnt)
    
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 - Fibonacci Series

# n = int(input('Enter a number: '))

# first=0
# second = 1 
# result = 0 
# print(first,' ', second)
# if n==1:
#     print(first)
# elif n==2:
#     print(second)
# else:
#     for i in range(2,n):
#         result = first + second
#         first = second
#         second = result
#         print(result,end=' ')

# while loop:

# Syntax: 

# i=1
# while condition:
#     statements
#     increment/decrement

# i=1
# while i<=10:
#     print(i, end=" ")
#     i+=1
    
# break and continue statements: 

# i=1
# while i<=10:
#     print(i, end=" ")
#     if i == 4:
#         break
#     i+=1

# i = 10
# while i>=0:
#     print(i, end= " ")
#     i-=1


# continue statements :

# for val in sequence:
#     # code 
#     if condition:
#         continue
#     # 

# for i in range(6):
#     if i == 5:
#         continue
#     print(i)

# functions : it is also known as methods in python

# use : code reusability 

# types of functions : 
    
# 1. Built-in functions & standard library functions : 
# 2. User-defined functions : 

# Python function declaration :
    
# def function_name(parameters):
#     #function body
    
#     return  

# 1. def - keyword used to declare a function
# 2. function_name - name of the function
# 3. parameters - input to the function
# 4. function body - code inside the function
# 5. return - keyword used to return the value from the function


#  declaring a function
# def message():
#     return "Welcome to the class mannat"
    

# #main function
# print(message())

# def add(num1,num2):
#     return num1+num2

# # calling a function
# a=int(input("Enter a 1st number: "))
# b=int(input("Enter a 2nd number: "))
# print(add(a,b))

# def prime(num):
#     cnt = 1
#     for i in range(2,num+1):
#         if num%i==0:
#             cnt+=1   
#         else:
#             return False
#     if cnt==2:
#         return num
#     else:   
#         return False

# # main function
# num = int(input("Enter a number: "))
# sum=0
# for i in range(2,num+1):
#     sum=sum+prime(i)
#     print(sum)

# scope of a variable : 
    
# 1. Local Variable : it is a variable which is declared inside the function

# 2. Global Variable : it is a variable which is declared outside the function


# String : a variable which is enclosed in the double quotes or single quotes
 
# indexing
# print(a[8])

# slicing 
# print(a[6:11])

# indexing : it is used to access the elements of the string   [] - square brackets
# slicing  : it is used to access the substring from the string  [1:8] - start:end

# length of a string : len() - built-in function

# print(len(a))

# print("mannat" not in a)


# a= " Welcome to the class mannat"    
# print(a[:8])



# 153 = 1^3 +5^3 + 3^3 = 1+125+27 = 

# perfect number : 6 = 1+2+3 = 6


# random module 

# random(start, end);

# import random
# print(random.randrange(1,10))

# 1. seed() - it is used to generate the same random number
# 2. getstate() - it is used to get the state of the random number
# 3. randint() - it is used to generate the random integer number
# 4. choice() - it is used to generate the random number from the given sequence

# requests : it is used to send the request to the server

# import requests
# x = requests.get('https://en.wikipedia.org/wiki/Sidhu_Moose_Wala')

# print(x.text)


# list : it is a collection of elements which is enclosed in the square brackets and separated by comma

# thislist = list(("apple", "banana", "cherry"))
# print(thislist)


# python collection : (Arrays)
#     => list
#     => tuple
#     => set
#     => dictionary

# thislist = ["apple", "banana", "cherry","orange","kiwi","melon","mango"]
# print(thislist[2:])

# list1 = ["apple", "banana", "cherry"]
# list1.insert(2, "orange")
# print(list1)

# extend () : it is used to add the elements of the list to the another list

# list1 = ["apple", "banana", "cherry"]
# list2 = ["orange", "mango", "grapes"]
# list2.pop(1)
# print(list2)

# list1.extend(list2)
# print(list1)

# list1 = ["apple", "banana", "cherry"]
# for i in list1:
#     print(i)

# tuples:

# import random 


# start = int(input("Enter a starting range: "))
# end = int(input("Enter a ending range: "))

# print("You have got only 5 chances to guess the number")

# n = random.randrange(start,end)
# guess = int(input("Enter a number: "))
# cnt = 0 
# for i in range(1,6):
#     cnt+=1
#     if guess == n:
#         print("Hurrah you guessed it right")
#         break
#     elif guess>n:
#         print("Your guess is too high")
#         guess = int(input("Enter a number: "))
#     elif guess<n:
#         print("Your guess is too low")
# if cnt>=5:
#     print("You have exceeded the number of chances")
#     print("The number is : ",n)


# tuples : it is a collection of elements which is enclosed in the round brackets and separated by comma - immutable

# tuple1 = ("apple", "banana", "cherry","orange","orange","kiwi","melon","mango")
# print(len(tuple1))

# # not a tuple
# tuple1 = ("apple")
# print(type(tuple1))


# # tuple
# tuple1 = ("apple",)
# print(type(tuple1))

# type casting : converting one data type to another data type

# tuple1 = ("apple", "banana", "cherry","orange","orange","kiwi","melon","mango")
# list1 = list(tuple1)

# list1.append("grapes")
# tuple1 = tuple(list1)

# print(type(tuple1))

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# for i in range(len(fruits)):
#     print(fruits[i])


# methods/functions : 

# count(): returns the number of times a specified value occurs in a tuple
# index(): searches the tuple for a specified value and returns the position of where it was found

# Python Sets: 

# set1 = {"apple", "banana", "cherry","orange","orange","kiwi","melon","mango"}
# print(set1)

# 1. set Items
# a. unchanged
# b. unordered
# c. duplicates not allowed

# in set True & 1 are considered as same

# set1= {1,2,3,4,5,6,7,8,9}
# set2 = ["apple", "banana", "cherry","orange","orange","kiwi","melon","mango"]
# set1.update(set2)

# print(set1)


# dictionary    key values

# dict1= {
#     'brand':'Mercdez',
#     'model':'C200',
#     'year':2019,
#     'color':['red','blue','black']
# }

# # get() - it is used to get the value of the specified key

# # x = dict1.get('color')

# x = dict1.keys()
# print(x)

# get() : it is used to get the value of the specified key

# dict1=dict(brand='Mercdez',model='C200',year=2019,color=['red','blue','black'])

# print(dict1)

# values() - it is used to get the values of the dictionary

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year":1964
# }
# car.clear()
# print(car)

# x = car.items()
# print(x)

# # car["color"] = "white"
# # print(x)

# update()


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year":1964
# }

# car1 = car.copy()

# for x in car.values():
#     print(x)
    
    
# nested dictionaries


# data structure 

# list/array : [1,2,3,4,5,6,7,8,9,10]

# linear search()

# 7


# def linear_Search(arr,element):
#     for i in arr:
#         if arr[i] == element:
#             return i
#     return -1

# # main function 
# arr = [1,2,3,4,5,6,7,8,9,10]
# element = int(input("Enter a number: "))
# print(linear_Search(arr,element))


# def swap1(arr):
#     arr[0],arr[-1]= arr[-1],arr[0]
#     return arr

# main function
# 4


# def binary_Search(arr,x):
#     start = 0
#     end = len(arr)-1
#     if start<=end:
#         mid = (start+end)//2
#         if arr[mid]<x:
#             start = mid+1
#         elif arr[mid]>x:
#             end = mid-1
#         else:
#             return mid
#     return -1

# # main function
# arr= [1,2,3,4,5,6,7,8,9,10]
# x = int(input("Enter a number: "))
# result = binary_Search(arr,x)
# if result!=-1:
#     print("Element is present at index",str(result))
# else:
#     print("Element is not present in the array")


# Nested Loops : 
    
# for i in range(1,6):
#     for j in range(1,6):
#         print(j)
#     print('')

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows = int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print('')
    
    

# a = 10 
# print(type(a))


# arr = [10,19,24,56,75,51]
# n = len(arr)

# sum = 0 
# for i in range(0,n):
#     sum+= arr[i] 

# print("The sum of the elements in an array is: ",sum)


# Sorting : bubble sort, insertion sort 


# bubble sorted

# def bubble_sort(arr,n):
#     for i in range(0,n-1):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]= arr[j+1],arr[j]
                
# # main function
# arr = [10,19,14,52,38,71]
# n = len(arr)
# print("Sorted array : ")
# bubble_sort(arr,n)
# for i in range(0,n):
#     print(arr[i],end=" ")


# Local Scope and Global Scope

# c = 20 # //global scope

# def add(a,b):
#     # //local scope
#     return a+b+c

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# print(add(a,b))

# local scope : inside a function
# global scope : outside a function


# Modules and Packages :
    
#     Modules : A file containing a set of functions you want to include in your application.
    
# from module1 import person1


# print(person1["nam+e"])


# import datetime

# x = datetime.datetime.now()

# print(x.month)
# print(x.strftime("%A"))


# x = min(45,15,82)
# print(x)

# abs() - returns the absolute value of a number
# pow(base, exponent) - returns the value of x to the power of y
# sqrt()-

# import math 

# x = math.pi
# print(x)

# split() - splits a string into a list


# s= "Welcome to python"
# n = s.split(" ")

# Sorting :
    
# insertion sort

# def insertion_sort(arr):
#     for i in range(1,len(arr)):      #5
#         key = arr[i]                 # key = 5
#         # sorted list
#         j = i-1                       # j = 0 
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j = j-1
#         arr[j+1]=key
        
# data = [5,9,1,4,3]
# print("Unsorted list",data)
# insertion_sort(data)
# print("Sorted list",data)



# Recursion/ Recursive Function:- 


# def greet():
    
#     print( "Welcome Mannat!")
#     greet()

# # main function
# greet()

# 1. Direct Recursion
# 2. Indirect Recursion


# def functionA():
#     print("Function A")
#     functionB() 
# def functionB():
#     print("Function B")
#     functionA()
    
# # main function
# functionA()

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n+sum(n-1)

# # main function
# n = int(input("Enter a number: ")) #n =4
# print(sum(n))

# Mannat

# tannaM

# factorial 

# def reverse(name):
#     if len(name) == 0:
#         return 
#     temp = name[0]    #TANNAM
#     reverse(name[1:])
#     print(temp,end="")

# name = input("Enter a name: ")
# reverse(name)


# def fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
               
    
# # main function
# n = int(input("Enter a number: "))
# print(fibo(n))



# classes and objects :
    
# class - blueprint of an object
# object : it is an instance of class

# a = 10
# print(type(a))


# Python is an object oriented programming language.
# A class is like an object constructor, or a "blueprint" for creating objects.


# create a class:

# keyword class:

# class Person:
#     age = 18 
#     name = "Mannat"
    
# p1 = Person()
# p2 = Person()
# print(p1.age)
# print(p2.name)



# _init_(self) 


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __str__(self):
#         return f"{self.name} {self.age}"

# p1 = Person("Mannat",18)
# p2 = Person("Weather",50)
# p3 = Person("Staingo",20)
# p4 = Person("Ture",50)

# print("Person 1")
# print(p1)

# print("Person 2")
# print(p2.name)
# print(p2.age)
# print("Person 3")

# print(p3.name)
# print(p3.age)
# print("Person 4")

# print(p4.name)
# print(p4.age)





# def display(lst,rows,cols):
#     for i in range(rows):
#         for j in range(cols):
#             print(lst[i][j],end=" ")
#         print()

# def sum_of_boundary_elements(lst, rows, cols):
#     sum = 0
#     for i in range(rows):
#         for j in range(cols):
#             if(i == 0):
#                 sum+=lst[i][j]
#             elif( i == rows-1):
#                 sum+=lst[i][j]
#             elif(j == 0):
#                 sum+=lst[i][j]
#             elif(j == cols-1):
#                 sum+=lst[i][j]
#     return sum



# lst = []
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         elem = int(input("Enter the element: "))
#         row.append(elem)
#     lst.append(row)

# display(lst,rows,cols)
# print("Sum of boundary elements: ",sum_of_boundary_elements(lst,rows,cols))




# database =  SQL database

# Structured Query Language

# mysql-connector-python - pip install mysql-connector-python


# host = "localhost",
# user = "root",
# password = "",


# import mysql.connector

# mydatabase = mysql.connector.connect(
#     host = "localhost",
#     username="root",
#     password=""
# )

# print(mydatabase)

# mycursor =  mydatabase.cursor()

# mycursor.execute("DROP DATABASE IF EXISTS login_system")
# print("Database deleted successfully")

# mycursor.execute("CREATE DATABASE login_system")
# print("Database created successfully")


# from tkinter import *

# m = Tk()
# m.title("My first GUI")
# Label(m,text="First Name").grid(row=0)
# Label(m,text="Last Name").grid(row=1)

# e1 = Entry(m)
# e2 = Entry(m)

# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)

# mainloop()

 


# m.mainloop()



# activeBackground
# activeForeground
# bg
# command
# font
# image
# width
# height


# from tkinter import *

# m = Tk()
# menu = Menu(m)

# m.config(menu=menu) 
# filemenu = Menu(menu)
# menu.add_cascade(label="File",menu=filemenu)
# filemenu.add_command(label="New text file")
# filemenu.add_command(label="New file")
# filemenu.add_command(label="New Window")
# filemenu.add_separator()
# filemenu.add_command(label="Open File")
# filemenu.add_command(label="Exit",command=m.quit)

# mainloop()

# File Handling :
    
# open()

# readme.txt

# r - read mode
# a - append mode
# w - write mode
# x - create file 

# t - text

# f = open("readme.txt","rt")
# print(f.read())




# matplot lib

# pip install matplotlib

# import matplotlib.pyplot as plt
# import numpy as np 

# x_axis = np.array([0,5])
# y_axis = np.array([0,200])

# plt.plot(x_axis,y_axis)
# plt.show()


import tkinter
import mysql.connector

# Connect to the database

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cur = conn.cursor(buffered=True)

try:
    cur.execute("use registration")
except:
    cur.execute("create database registration")
    cur.execute("use registration")

try:
    cur.execute("describe register")
except:
    cur.execute("create table register(id int primary key auto_increment, fname varchar(20), lname varchar(20), age int, email varchar(20), mobile varchar(20))")

def Registration():
    fname = e1.get()
    lname = e2.get()
    age = e3.get()
    email = e4.get()
    mobile = e5.get()
    
    query = "insert into register(fname,lname,age,email,mobile) values (%s,%s,%s,%s,%s)"
    values = (fname, lname, age, email, mobile)
    
    try:
        cur.execute(query, values)
        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", e)
        conn.rollback()

win = tkinter.Tk()
win.geometry("600x600")
win.title("Registration Form")

l1 = tkinter.Label(win, text="First Name")
l2 = tkinter.Label(win, text="Last Name")
l3 = tkinter.Label(win, text="Age")
l4 = tkinter.Label(win, text="Email")
l5 = tkinter.Label(win, text="Mobile No.")

l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=5, column=1)

e1 = tkinter.Entry(win)
e2 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e4 = tkinter.Entry(win)
e5 = tkinter.Entry(win)

e1.grid(row=1, column=2)
e2.grid(row=2, column=2)
e3.grid(row=3, column=2)
e4.grid(row=4, column=2)
e5.grid(row=5, column=2)

submit_button = tkinter.Button(win, text="Submit", command=Registration)
submit_button.grid(row=6, column=2)

win.mainloop()




# get post put delete

# CRUD


def main():
    1. Open Acc 
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance 
    5. Customer details 
    6. Close an account 


if choice == 1:
    openacc()