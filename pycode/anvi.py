# variables:- 

# num,a,b

# data types:-

# int -> 
# float -> 1.5,10.5,20.5
# string -> "Anvi","Nidhi","Riya"
# boolean -> True/False 0/1

# type() -> to check the data type of a variable

# num = "7.5"
# print(type(num))


# num = 7
# num1 = 15
# print(num+num1)

# operators and operands 

# operator -> +,-,*,/,//,%,**

# print(20%3)

# firstname ="Anvi"
# surname = " Chugh"

# print(firstname+surname)

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print("1. Addition",a+b)


# Conitional :-

# if statement
# if else statement
# if elif else statement


# if condition:
#     statements


# age = int(input("Enter your age: "))

# if age>=18:
#     print("you're an adult")
# if age<18:
#     print("you're a child")


# age = int(input("Enter your age: "))

# if age>18:
#     print("you're an adult")
# elif age == 18:
#     print("you're a teenager")
# else:
#     print("you're a child")


# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement


# a = 9
# b = 8
# ab = int(input("input a number: "))
# cd = int(input("input a  number 2: "))
   
    
# if ab>cd:
#     print("ab is greater")
# elif ab == cd:
#     print("both are equal")
# else:
#     print("cd is greater")

# %-> modulus operator -> remainder

# // -> floor division -> whole number
# / -> division -> decimal



# ** -> power operator

# oe= int(input("enter a number: "))
# if oe%2==0:
#     print("even")
# else:
#     print("odd")

# le= int(input("enter a year: "))

# if le%4 ==0:
#     print("leap year")
# else:
#     print( "not a leap year")



# base ** power = 4 ** 2 = 16

# loops:-

# 1. for loop : used to iterate over a sequence (that can be a list, tuple, dictionary, string or range) with a specific step value.

# syntax:

# for variable_name in range(start,end,step):
#     statements

# for a in range(1,21,2):
#     print(a)



# 2. while loop : used to execute a block of statements repeatedly until a given condition is satisfied.



# 0 2 4 6 8 10 12 14 16 18 20

# 0 5 10 15 20 25 30 35 40 45 50

# 10 9 8 7 6 5 4 3 2 1

# 1 2 3 4 5 6 7 8 9 10 = 55

# piggy_bank = 1

# for i in range(1,21):
#     piggy_bank = piggy_bank*i
    
# print(piggy_bank)


# 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 = 260



# random numbers-

# import random

# v = random.randint(1,10) # generates a random integer between 1 and 10

# print(v)


# 1 50

# break - to stop the loop



# Number guessing game:-

# random module - > randint() -> generates a random number between the given range

# import random

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# secret_number = random.randint(1, 100)
# attempts = 0

# while attempts < 10:
#     guess = int(input("Make a guess: "))
#     attempts = attempts + 1
    
#     if guess == secret_number:
#         print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
#         break
#     elif guess < secret_number:
#         print("Too low.")
#     else:
#         print("Too high.")

# if attempts > 10:
#     print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")



# strings:- it is a sequence of characters enclosed in single or double quotes.


# example:
    
# name = "Utkarsh Singh"
# print(name[-1])


# how we can find the length of a string?

# name = "Welcome to the class of python we are studying string in today's class"
# print(len(name))


# slicing :

# name = "Welcome to the class of python we are studying string in today's class"
# print(name[0:7])

# Modifying a string

# name = "ANVI"
# print(name.lower())


# replace method

# message = "I like to play football"
# print(message.replace("I","You"))

# concatenation

# firstname = "Anvi"
# lastname = "Chugh"

# print(firstname+lastname)


# replication

# name = "Anvi"

# print(name*3)

# formatting a string 

# age = 20
# name = "Anvi"

# print("My name is",name,"and I am",age,"years old.")
# print(f"My name is {name} and I am {age} years old.")


# Python List

# List is a collection of items which is ordered and changeable. Allows duplicate members.

# myList = ["apple","banana","cherry","apple","banana","cherry"]

# mylist1-[4,"apple",False,3.5]

# print(len(myList))


# myList = ["apple","banana","cherry","apple","banana","cherry"]

# print(myList[-4])

# myList = ["apple","banana","cherry","apple","banana","cherry"]

# # print(myList[1:4x``])


# myList = ["banana","cherry","banana","cherry"]

# if "apple" not in myList:
#     print("Yes it's present")
# else:
#     print("No it's not present")

# .lower() -> it converts the string into lowercase    ANVI.lower() = anvi




# name = "Anvi"
# print(name)

# name = "Anvi"
# print(name[::-1])


# .append()-> It adds up the elements/item at the last of the list.
# .insert()-> It adds up the elements/item at the required position of user.

# l2 = ["Audi","Mercedes","Toyota","Honda"]
# l2.insert(2,"BMW")


# print(l2)


# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# array :

# a = 14
# b = 15
# c = 16
# d = 17
# e = 18
# f = 19
# g = 20
# h = 21
# i = 22
# j = 23

# arr = [14,15,16,17,18,19,20,21,22,23]

# print(arr)


# we are going to learn about the Data type:-

# 1. List : It is a collection of items which is ordered and changeable. Allows duplicate members.

# myList = ["apple","banana","cherry","apple","banana","cherry"]

# l1 = [10,20,30,40,50]
# print(max(l1))


# 2. Tuples : It is a collection of items which is ordered and unchangeable. Allows duplicate members.
# -> it is represented by round brackets ()

# example :

# t1 = ('apple', 'banana', 'cherry', 'watermelon')
# print(t1[-1])

# slicing

# t1 = ('apple', 'banana', 'cherry', 'watermelon')
# print(t1[1:])

# input

# l4=[1,1,1,2,2,3,3,4,5,6,7,6,8,0,6,4,2,1,1,1,0,0,0,0,3,3,3,2,4,]

# ouput 

# l4 = [1,2,3,4,5,6,7,8,0]

# names = ['anvi','utkarsh','Joe','Bob','Johnson','David','Aanya','zuckerburg']


# functions:-


# it increases the functionality
# code-reusability


# num = 8
# if num%2==0:
#     print(num)

# def function_name():
#     #statements

#     return something


# def is_even(num):
#     if num%2==0:
#         print(num)

# # main function
# is_even(8)
# is_even(15)

# import tkinter as tk 

# def cel_to_fah():
#     try :
#         celsius = float(entry.get())
#         fahrenheit = (celsius * 9/5) + 32
        
#         result.config(text=f"Temperature in Fahrenheit: {fahrenheit}")
#     except ValueError:
#         result.config(text="Please enter a valid number.")

# def fah_to_cel():
#     try:
#         fahrenheit = float(entry.get())
#         celsius = (fahrenheit - 32) * 5/9
        
#         result.config(text=f"Temperature in Celsius: {celsius}")
#     except ValueError:
#         result.config(text="Please enter a valid number.")



# root = tk.Tk()

# root.title("Temperature Converter")

# l1 = tk.Label(root,text="Temperature Converter",font=("Arial",20))
# l1.grid(row=0,columnspan=3,padx=20,pady=20)

# l1 = tk.Label(root,text="Enter the temperature in Celsius/fahrenhiet:",font=("Arial",15))
# l1.grid(row=1,column=0,padx=20,pady=20)

# entry = tk.Entry(root,font=("Arial",15))
# entry.grid(row=1,column=1,padx=20,pady=20)

# b1 = tk.Button(root,text="Convert to celsius :",font=("Arial",15),fg="white",bg="blue",command=cel_to_fah)
# b1.grid(row=2,column=0,padx=20,pady=20)

# b2 = tk.Button(root,text="Convert to fahrenhiet :",font=("Arial",15),fg="white",bg="blue",command=fah_to_cel)
# b2.grid(row=2,column=1,padx=20,pady=20)

# result_frame = tk.Frame(root,bd=2,relief=tk.GROOVE)
# result_frame.grid(row=3,columnspan=2,padx=20,pady=20)

# result = tk.Label(result_frame,text="Result",font=("Arial",15))
# result.grid(padx=20,pady=20)

# root.mainloop()


# functions - > it increases the functionality of the code and also helps in code reusability.

# syntax:

# def function_name(arguments):
#     # statements
#     # return 

# # main function
# function_name(parameters)

# def add(a,b):
#     print(f"The addition of two numbers is {a+b}")

# main function

# add(10,20)


# 1. Subtract
# 2. Multiply
# 3. Divide
# 4. Modulus
# 5. Exponent
# 6. Floor Division


# tkinter - It is a module that helps to make the desktop application

# from tkinter import *


# root = Tk()
# root.title("Calculator")
# root.geometry('300x400')

# label = Label(root,text="Sign Up ",font=("Arial",20))
# label.pack(pady=20)

# firstname = Label(root,text="First Name",font=("Arial",15))
# firstname.pack(pady=10)

# entry = Entry(root,font=("Arial",15))
# entry.pack(pady=10)

# lastname = Label(root,text="Last Name",font=("Arial",15))
# lastname.pack(pady=10)

# entry1 = Entry(root,font=("Arial",15))
# entry1.pack(pady=10)

# button = Button(root,text="Submit",font=("Arial",15),bg="blue",fg="white")
# button.pack(pady=10)

# root.mainloop()




# from tkinter import *
# root = Tk()
# root.title("calculator")
# root.geometry('300x400')
# label=Label(root,text="calculator",font=("caveat",20))
# label.pack(pady=20)

# firstname = Label(root,text="First Name",font=("caveat",15))
# firstname.pack(pady=10)
# entry1 = Entry(root,font=("caveat",15))
# entry1.pack(pady=10)
# lastname = Label(root,text="last Name",font=("caveat",15))
# lastname.pack(pady=10)
# entry2 = Entry(root,font=("caveat",15))
# entry2.pack(pady=10)
# email = Label(root,text="email",font=("caveat",15))
# email.pack(pady=10)
# entry3 = Entry(root,font=("caveat",15))
# entry3.pack(pady=10)
# phone = Label(root,text="phone")
# city= Label(root,text="city",font=("caveat",15))
# city.pack(pady=10)
# entry4 = Entry(root,font=("caveat",15))
# entry4.pack(pady=10)
# password = Label(root,text="password",font=("caveat",15))
# password.pack(pady=10)
# entry5 = Entry(root,font=("caveat",15))
# entry5.pack(pady=10)
# confirmpassword  = Label(root,text="confirm password",font=("caveat",15))
# confirmpassword.pack(pady=10)
# entry6 = Entry(root,font=("caveat",15))
# entry6.pack(pady=10)

# b1 = Button(root,text="Submit",fg="white",bg="green")
# b1.pack(pady = 10)
# root.mainloop()

# counter - if we are clicking the button it will increase the count by 1 

# from tkinter import *

# def click():
#     global counter
#     counter=counter+1
#     label.config(text=f"Clicks :{counter}")
    
# counter = 0

# root = Tk()
# root.title('Counter')
# root.geometry('400x300')
# root.configure(bg='green')

# label = Label(root,text="Clicks: 0")
# label.pack()

# button = Button(root,text="Click me!",command=click)
# button.pack()

# root.mainloop()


# you need to make the counter and increase by 5 everytime
# and put the clear button as well for clearing up the fields

# 1. firstname
# 2. lastname
# 3. email
# 4. Phone
# 5. Address
# 6. City
# 7. Password
# 8. Confirm Password


# l1 = [14,89,65,71,23,45,63]

# max = l1[0]

# for i in range(0,len(l1)):
#     if l1[i] >max:
#         max = l1[i]


# print(max)







# from tkinter import *

# root = Tk()

# root.title('Counter')
# root.geometry('200x300')


# l1 = Label(root,text="Utkarsh Singh")
# l1.pack()

# b1 = Button(root,text="Click me!")
# b1.pack()


# root.mainloop()



from tkinter import *

root = Tk()
root.title("Signup Page")
root.geometry('400x400')

l1 = Label(root,text="Email")
l1.pack()

e1 = Entry(root)
e1.pack()

l2 = Label(root,text="Password")
l2.pack()

e2 = Entry(root,show='*')
e2.pack()

b1 = Button(root,text="Submit",fg="white",bg="green")
b1.pack()

root.mainloop()



# Just create a signup page with the below entries

# Username
# Email
# contact
# address
# password
# confirm password 


# submit button 

