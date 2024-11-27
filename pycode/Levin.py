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


# Python Nested Loops :


# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# Type casting : It changes the data type from one to another.

# a = "10"

# n = int(a)
# print(type(n))

# Arrays : 

# 1. List

# -> It is collection of items,which is ordered and changeable. Allow duplicate values.It is mutable
# -> It is represented by square brackets []

# l1 = [10,20,30,40,50] (int)
# l2 = ["Anvi","Nidhi","Levin","Arnav"](str)
# l3 = [10.587]
# l4 = [10,20,30,"Utkarsh",51.058,True]

# l1 = [10,20,30,40,50]

# print(l1[2])

# slicing : It is used to extract a part of the list


# l1 = [10,20,30,40,50]
# print(l1[:3])

# l2 = ['a', 'b', 'c', 'd', 'e']
# print(l2[2:])


# What will be the output of the code?



# **Options:**

# a) ['a', 'b', 'c']  
# b) ['a', 'b', 'c', 'd']  
# c) ['c', 'd', 'e']  
# d) ['d', 'e']  

# ---

# **Answer:**

# The correct answer is **c) ['c', 'd', 'e']**.

# l4 = [5, 10, 15, 20, 25, 30]
# print(l4[2:5])

# how to change the elements or update it 

# cars = ["Ford","Toyato","BMW","Mercedes"]

# cars[1] = "Audi"

# print(cars)

# cars = ["Ford","Toyato","BMW","Mercedes"]

# l1 = [1,2,3,4,5]

# names = ["Anvi","Levin","Nidhi","Arnav","Utkarsh"]

# 2. tuple
# 3. set
# 4. Dictionaries



# names = ["Anvi","Levin","Nidhi","Arnav","Utkarsh"]
# count = 0
# for name in names:
#     vowels = "aeiouAEIOU"
#     if name[0] in vowels:
#         count +=1

# print(f"The number of names starting with vowels are: {count}")


# add item to the list

# append() - It is used to add an element to the end of the list.
# insert() - It is used to add an element at a specific index.

# name = ["Anvi","Levin","Nidhi","Arnav","Utkarsh"]
# name.append("Ture")

# name.insert(2,"Apoorv")

# print(name)


# remove item from the list

# remove() - It is used to remove the first occurrence of the element from the list.
# pop() - It is used to remove the element from the specified index.

# cars = ["Ford","Toyato","BMW","Mercedes"]
# cars.remove("Toyato")

# cars.pop()

# print("The updated list is: ",cars)

# loop lists 

# cars = ["Ford","Toyato","BMW","Mercedes"]

# for i in cars:
#     print(i)

# how to sort the list

# sort() - It is used to sort the list in ascending order.

# cars = ["Ford","Toyato","BMW","Mercedes"]

# cars.sort()

# print("The sorted list is: ",cars)



# cars = ["Ford","Toyato","BMW","Mercedes"]

# cars.sort(reverse = True)

# print("The sorted list is: ",cars)


# name = "Levin"
# print(name[::-1])

# cars = ["Ford","Toyato","BMW","Mercedes"]
# trucks = cars.copy()

# print(trucks)

# l1 = [10,20,30,40,50]
# l2 = [60,70,80,90,100]

# print(l1+l2)

# 2. Tuples : - It is collection of items,which is ordered and unchangeable. Allow duplicate values.It is immutable

# It is represented by round brackets ()

# t1 = (10,20,30,40,50)
# print(t1)

# bikes = ("Honda","Yamaha","Suzuki","Kawasaki")

# # type casting
# l1 = list(bikes)

# l1[-1] = "Ducati"

# bikes = tuple(l1)

# print(bikes)


# Sets : - It is collection of items,which is unordered and unindexed. It does not allow duplicate values.

# It is represented by curly brackets {}

# s1 = {10,20,30,40,50}
# s2 = {"Anvi","Levin","Nidhi","Arnav","Utkarsh"}
# s3 = {10,20,30,40,50,10,20,30,40,50}

# print(s3)

# cars = {"Ford","Toyato","BMW","Mercedes"}

# print("BMW" not in cars)


# fruits = {"apple","banana","cherry","orange","kiwi"}

# fruits.add("mango")

# print(fruits)

# fruits = {"apple","banana","cherry","orange","kiwi"}
# fruits2 = {"mango","papaya","grapes","orange","kiwi"}

# fruits.update(fruits2)

# print(fruits)

# fruits = {"apple","banana","cherry","orange","kiwi"}

# fruits.remove("cherry")

# print(fruits)


# join sets 

# 1. union() - It is used to join two sets.

# set1 = {1,2,3,4,5,'a'}
# set2 = {'a','b','c','d','e',5}

# set3 = set1.union(set2)

# print(set3)


# 2. intersection() - It is used to get the common elements from two sets.


# set1 = {1,2,3,4,5,'a'}
# set2 = {'a','b','c','d','e',5}


# set3 = set1.intersection(set2)
# print(set3)

# & - joining two sets


# dictionaries - 

# example :

# student = {
#     "Name" : "Levin",
#     "Age" : 15,
#     "Class" : 10,
#     "School" : "St. Mary's School",
#     "Age" : 16
# }


# print(student["Name"])

# x = student.get("Age")
# print(x)

# k = student.keys()
# v = student.values()

# print(k)
# print(v)



# student = {
#     "Name" : "Levin",
#     "Age" : 15,
#     "Class" : 10,
#     "School" : "St. Mary's School",
#     "Age" : 16
# }


# student["RollNo"] = 101

# print(student)


# x = student.items()
# print(x)


# student.pop("Class")

# print(student)



# t1 = (5, 3, 8, 1, 2)
# l1 = list(t1)

# n = len(l1)

# for i in range(n):
#     for j in range(0,n-i-1):
#         if l1[j] > l1[j+1]:
#             l1[j],l1[j+1] = l1[j+1],l1[j]

# t1 = tuple(l1)

# print("The sorted tuple is: ",t1)

# t1 = (5, 3, 8, 1, 2)
# print("The sorted tuple is : ",tuple(sorted(t1)))



# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# print("The original list is: ",lst)

# n = len(lst)


# for i in range(n):
#     for j in range(0,n-i-1):
#         if lst[j] > lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]

# print("The sorted list is: ",lst)

# class - It is a blueprint for creating objects. A class defines the attributes and methods that an object will have.

# object - It is an instance of a class. An object is created using the constructor of the class.


# create a class

# class Class1:
#     age = 15

# # create an object

# obj1 = Class1()
# print(obj1.age)

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def print(self):
#         return f"{self.name} is {self.age} years old"
    
# class test(Student):
#     def __init__(self,name,age,rollno):
#         super().__init__(name,age)
#         self.rollno = rollno

#     def print(self):
#         return f"{self.name} is {self.age} years old and his roll no is {self.rollno}"
    
# s1 = Student("Levin",15)
# s2 = test("Anvi",15,101)

# print(s1.print())
# print(s2.print())



# Python polymorphism - 


# class Car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model

#     def move(self):
#         print("Drive")

# class Boat:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model

#     def move(self):
#         print("Sail")
# class Plane:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model

#     def move(self):
#         print("Fly")

# car1 = Car("Ford",2021)
# boat1 = Boat("Yamaha",2021)
# plane1 = Plane("Boeing",2021)


# for i in (car1,boat1,plane1):
#     i.move()

        

# class dog:
#     def __init__(self, sound):
#         self.sound = sound
#     def sound(self):
#         print(self.sound)
# class cat:
#     def __init__(self, sound):
#         self.sound = sound
#     def sound(self):
#         print(self.sound)
# class mouse:
#     def __init__(self, sound):
#         self.sound = sound
#     def sound(self):
#         print(self.sound)

# dog1 = dog("bark")
# cat1 = cat("meow")
# mouse1 = mouse("squeak")
# for i in (dog1, cat1, mouse1):
#     i.sound()

# import math


# class Shape:
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2


# def print_area(shape):
#     print(f"Area: {shape.area()}")


# rect = Rectangle(4, 5)
# circ = Circle(3)

# print_area(rect)  

# import tkinter as tk

# def click():
#     global counter
#     counter +=1
#     label.config(text=f"Clicks : {counter}")


# counter = 0

# root = tk.Tk()
# root.title("Click Counter")
# root.geometry('400x300')

# root.configure(bg='blue')

# label = tk.Label(root,text="Clicks : 0")
# label.grid(row = 0,column=1)

# button = tk.Button(root,text="Click Me!",command = click)
# button.grid(row =0 ,column=2)

# root.mainloop()


# import tkinter as tk
# import math

# expression = ""

# def press(num):
#     global expression
#     expression +=str(num)
#     equation.set(expression)

# def equal():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression = ""
#     except:
#         equation.set("Error")
#         expression = ""

# def delete():
#     global expression
#     expression = expression[:-1]
#     equation.set()


# def clear():
#     global expression
#     expression = ""
#     equation.set("")

# root = tk.Tk()
# root.geometry("190x150")

# equation = tk.StringVar()
# expression_field = tk.Entry(root,textvariable=equation)
# expression_field.grid(columnspan=4,ipadx=10)

# e = tk.Label(root,text="")
# e.grid(row=1, column=1)
# b1 = tk.Button(root, text="1",command = lambda : press(1))
# b1.grid(row=2, column=1)
# b2 = tk.Button(root, text="2",command = lambda : press(2))
# b2.grid(row=2, column=2)
# b3 = tk.Button(root, text="3",command = lambda : press(3))
# b3.grid(row=2, column=3)
# bp = tk.Button(root, text="+",command = lambda : press("+"))
# bp.grid(row=2, column=4)
# b4 = tk.Button(root, text="4",command = lambda : press(4))
# b4.grid(row=3, column=1)
# b5 = tk.Button(root, text="5",command = lambda : press(5))
# b5.grid(row=3, column=2)
# b6 = tk.Button(root, text="6",command = lambda : press(6))
# b6.grid(row=3, column=3)
# bm = tk.Button(root, text="-",command = lambda : press("-"))
# bm.grid(row=3, column=4)
# b7 = tk.Button(root, text="7",command = lambda : press(7))
# b7.grid(row=4, column=1)
# b8 = tk.Button(root, text="8",command = lambda : press(8))
# b8.grid(row=4, column=2)
# b9 = tk.Button(root, text="9",command = lambda : press(9))
# b9.grid(row=4, column=3)
# bt = tk.Button(root, text="*",command = lambda : press("*"))
# bt.grid(row=4, column=4)
# b0 = tk.Button(root, text="0",command = lambda : press(0))
# b0.grid(row=5, column=1)
# bc = tk.Button(root, text="C",command = clear)
# bc.grid(row=5, column=2)
# bb = tk.Button(root, text="<-",command = delete)
# bb.grid(row=5, column=3)
# bd = tk.Button(root, text="/",command = lambda : press("/"))
# bd.grid(row=5, column=4)
# equal1 = tk.Button(root, text='=', fg="black", bg="white", command=equal, height=1, width=7)
# equal1.grid(row=5, column=2)

# root.mainloop()





# from tkinter import*
# from PIL import Image, ImageTk # type: ignore
  
  
# root = Tk()
# root.title("TKINDER BANK")
# root.configure(bg=('#FFFFFF'))
# root.geometry('400x1000')



# image = Image.open("Ohsama-Sentai-King-Ohger")
# bg_image = ImageTk.PhotoImage(image)










# name_label = Label(root,text="name",fg='black')
# name_label.pack(pady=10)
# name_entry = Entry(root)
# name_entry.pack(pady=10)
# email_label = Label(root,text='email',fg='black')
# email_label.pack(pady=10)
# email_entry = Entry(root)
# email_entry.pack(pady=10)
# phonenumber_label = Label(root,text="phone number",fg='black')
# phonenumber_label.pack(pady=10)
# phonenumber_entry = Entry(root)
# phonenumber_entry.pack(pady=10)
# root.mainloop()




# for i in range(1,11):
#     print("Danish")




# CRUD - 

# Create 
# Read
# Update
# Delete



# import mysql.connector


# mydb = mysql.connector.connect(
#     host="localhost",
#     root="user",
#     password="",
#     database = ""
# )

# if mydb.is_connected():
#     print("Database is connected")


# from tkinter import *

# def center_window(root, width=300, height=200):
    
#     root.geometry(f"{width}x{height}")
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     x = (screen_width // 2) - (width // 2)
#     y = (screen_height // 2) - (height // 2)
#     root.geometry(f"{width}x{height}+{x}+{y}")

# root = Tk()
# root.title("Sign Up form")


# center_window(root, 800, 500) 

# l1 = Label(root,text="Name")
# l1.pack()

# e1 = Entry(root)
# e1.pack()

# l2 = Label(root,text="Email")
# l2.pack()

# e2 = Entry(root)
# e2.pack()

# l3 = Label(root,text="Email")
# l3.pack()

# e3 = Entry(root)
# e3.pack()

# b1 = Button(root,text="Submit",fg="white",bg="green")
# b1.pack()

# root.mainloop()



from tkinter import *

def center_window(root, width=300, height=200):
    root.geometry(f"{width}x{height}")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

root = Tk()
root.title("Prove your identity")
center_window(root, 800, 500)
root.configure(bg="black")

items = []

items.append(Label(root, text="Hello", font=("RubikIso-Regular", 50), fg="cyan", bg="black"))
items.append(Label(root, text="This is an application used for checking your identity", font=("RubikIso-Regular", 20), fg="lime", bg="black"))
items.append(Label(root, text="***For parents only***", font=("RubikIso-Regular", 20), fg="yellow", bg="black"))
items.append(Label(root, text="You can create an identity for your child here", font=("RubikIso-Regular", 30), fg="orange", bg="black"))
items.append(Button(root, text="Sign up", font=("RubikIso-Regular", 20), fg="red", bg="black"))
items.append(Label(root, text="You can prove you really exist here", font=("RubikIso-Regular", 30), fg="orange", bg="black"))
items.append(Button(root, text="Log in", font=("RubikIso-Regular", 20), fg="red", bg="black"))

for i in items:
    i.pack()

root.mainloop()
