# Python - To solve the problems and for making the projects as well.

# 8th grade

# Variable : 

# a = 15,"Pratik"

# Data types:

# We are having four data types:

# 1. Integer (int) : It stores without decimals.
# example: a = 5, num = 98,etc.

# 2. Float (float) : It stores numbers with decimals 
# ex: pi = 3.14,etc.

# 3. String (str) : It stores characters,sentences and even words.
# ex: name = "Pratik", word = "Python",etc

# 4. Boolean (bool) : It stores two values either True or False
# ex: flag = True,flag = False,etc.

# type() : It helps you to identify the data is of which type

# a = True
# print(type(a))

# a+b 

# Operands = a,b
# and operators = +


# Operators : 

# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Exponential (**)
# 6. Floor Division (//)
# 7. Modulus (%)

# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))

# print("The sum of two numbers is : ",a+b)


# base = int(input("Enter the base : "))
# power = int(input("Enter the power : "))

# print(base**power)

# a  = 9 
# b = 2

# print(a%b)

# Input

# a = 9
# b = 4

# output:

# a = 4
# b = 9


# a = int(input("Enter the value of a : "))  #9
# b = int(input("Enter the value of b : "))  #2

# a = a+b  #11
# b = a-b  #9
# a = a-b  #2

# print("a : ",a)
# print("b : ",b)

# You need to use * and // 

# Conditional statements

# 1. If statement : It helps you to check one condition at a time

# syntax:

# if condition:
    # statements

# age = int(input("Enter your age for license verification : "))

# if age > 18:
#     print("You are allowed to drive the car")

# 2. If-else statements - It helps you to check two condition at a time

# syntax:

# if condition:
    # statements
# else:
#     statements

# age = int(input("Enter your age for license verification : "))

# if age > 18:
#     print("You are allowed to drive the car")
# else:
#     print("You are not allowed to drive the car")

# 3. If-elif-else: It helps you to check multiple condition at a time

# syntax:

# if condition:
#     statements
# elif condition:
#     statements
# else:
#     statements

# age = int(input("Enter your age for license verification : "))

# if age > 18:
#     print("You are allowed to drive the car")
# elif age == 18:
#     print("You just got eligible for driving the car")
# else:
#     print("You are not allowed to drive the car")

# you need to take two values from user and needs to check which value is the greater one


# Loops : for loops and while loop


# for loops

# syntax:

# for variable_name in range(start,end,steps):
#     statements

# for i in range(1,11,5):
#     print(i)


# 1 3 5 7 9 11 13 15 17 19 21

# 0 2 4 6 8 10 12 14 16 18 20

# 5 10 15 20 20 25 30 35 40 45 50

# 10 9 8 7 6 5 4 3 2 1 0

# 1 4 9 16 25 36 49 64 81 100

# 8 X 1 = 8

# num = int(input("Enter the number of which you want the multiplication number of :"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# while loop : 

# initialization 
# while condition:
#     statements

# 1 - 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1


# 1 - 10 = 55

# piggy_bank = 0
# for i in range(1,11):
#     piggy_bank = piggy_bank + i

# print("The sum of all elements in the list : ",piggy_bank)


# 567% = 7*10 = 70+6=76*10=760+5=765
# 56%10 = 6

# 5%10 = 5

# 765


# num = int(input("Enter the number to make it reverse : "))  #num = 123
# ans = 0
# while num != 0:
#     rem = num % 10    # rem = 1% 10 = 1
#     ans = ans * 10 + rem   #ans = 321
#     num = num // 10   #num = 1

# print(f"The reverse : {ans}")


# 854 = 8+5+4 =     


# == : used for comparing 
# != : not equals to 


# 0 1 1 2 3 5 8 13 21 34 55

# prev = 0
# current = 1

# print(prev,current,end= " ")

# for i in range(2,101):
#     next = prev + current 
#     print(next,end= " ")
#     prev = current    #prev = 1
#     current = next   #current = 2

# 0 1 1 2 3 5 8

# import random 

# print("Welcome to number guessing game!!!")

# max_chances = 5

# chances = 0

# secret_number = random.randint(1,30)

# while chances < max_chances:
    
#     guess = int(input("Guess the number : "))
#     chances = chances + 1

#     if guess == secret_number:
#         print("COngrats")
#         break
#     elif guess > secret_number:
#         print("Guess to high")
#     else:
#         print("Guess too low")

# if chances == max_chances:
#     print("You ran out of chances")




# num = int(input("Enter the number : "))

# count = 0

# for i in range(2,(num//2+1)):
#     if num % i == 0:
#         count = count + 1


# if count == 0:
#     print("The number is prime")
# else:
#     print("The number is not prime")



# Strings : Any characters ,words or sentences are said to be as strings 

# name = "Utkarsh Singh"

# index :

# 1. positive indexing - it starts from left to right from 0 to n-1
# 2. Negative indexing - It starts from right to left from -1 to -n


# print(name[-1])

# Slicing 

# print(name[::2])

# printing in reverse order
# print(name[::-1])

# [:end:steps]

# len() - it helps you to find the length of the string 

# name = "Pratik Karki"
# print(f"The length of {name} is {len(name)}")

# count = 0 

# for i in name:
#     count = count + 1

# print(f"The length of {name} is {count}")


# Arrays: It stores mutliples elements in it 

# 1. List - It allow duplicate elements to store 
# It is mutable
# It is being identified as or enclosed by []

# num = [7,8,9,5,3,4,1,2,6,9,8]
# names = ["Pratik","Utkarsh","David","Jessica","Julia"]
# radius = [47.8,85.3,9.04,55.63,77.49]
# flag = [True,False,False,False,True]

# student_info = ["Pratik",14,75.2,"Fairfes",True]


# names = ["Pratik","Utkarsh","David","Jessica","Julia"]
# # print(names[2])
# print(names[1:4])


# num = [7,8,9,5,3,4,1,2,6,9,8]
# for i in num:
#     print(i)

# num = [7,8,9,5,3,4,1,2,6,9,8]
# sum = 0 
# for i in num:
#     sum = sum + i 
# print(f"The sum of all element in a list are {sum}")


# Write a program to identify how many even and odd numbers are there in the list 

# 2. Tuple
# 3. Set
# 4. Dictionary 


# 5 = 5*4*3*2*1



# num = [7,8,9,5,3,4,1,2,6,9,8]

# max = num[0]

# for i in num:
#     if max < i:
#         max = i

# print(f"The maximum number in the list is : {max}")


# names = ["Pratik, Utkrash, David, Ryan, Emily, Matthew, Laith, Brandon"]
# v_count = 0
# vowels = "aeiouAEIOU"
# for i in names:
#     if i[0] in vowels:
#         v_count = v_count + 1
# print(f"The ammount of names starting up with vowels are {v_count}")


# Remove item 

# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# fruits.remove("Kiwi")

# print(fruits)


# remove element from specified index 

# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# fruits.pop()

# print(fruits)


# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# del fruits[2]

# print(fruits)



# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# for i in fruits:
#     print(i,end=" ")


# Sort()- 

# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# fruits.sort()        #ascending order 

# print(fruits)


# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# fruits.sort(reverse=True)    #descending order

# print(fruits)


# fruits = ["Mango","Orange","Kiwi","Pineapple"]
# fruits.reverse()
# print(fruits)

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = ["a","b","c","d","e","f"]

# print(list1+list2)

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = ["a","b","c","d","e","f"]

# for x in list2:
#     list1.append(x)

# print(list1)


# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = ["a","b","c","d","e","f"]

# list1.extend(list2)
# print(list1)

# Tuples: It is another way of storing multiple elements
# Tuples is immutable 
# It allows duplicate values 
# it is being identified by ()

# cars = ("Tesla","Ford","BMW","Lamborghini","Mercedez")

# print(cars)

# access elements - the way we have access in list the same way we need to access over here 


# cars = ("Tesla","Ford","BMW","Lamborghini","Mercedez")

# print(cars[-1])


# Type casting - It changes the data type of variable to another data type 

# cars = ("Tesla","Ford","BMW","Lamborghini","Mercedez")

# ans = list(cars)

# ans[1] = "Mustang"

# cars = tuple(ans)

# print(cars)

# Concatenation  - adding the tuples 

# replication 

# fruits = ("mango","Orange","Kiwi")
# print(fruits*2)

# Python Sets - used to store multiple variable in a single variable 

# a set of collection which is unordered,unchangeable,and unindexed.
# A set is being identified by {}
# Set doesn't allow duplicate values

# names = {"Pratik","David","Henry","Mark","Jessica","Jessica","David"}

# print(names)


# num = [1,5,8,7,4,9,1,5,6,3,4,2,6,2,6,3,5,8,9,2]

# # type casting 
# ans = set(num)

# num = list(ans)

# print(num)

# if you need find the length of the set 

# names = {"Pratik","David","Henry","Mark","Jessica","Jessica","David"}
# print(len(names))

# with the loops we can access 

# names = {"Pratik","David","Henry","Mark","Jessica","Jessica","David"}
# for i in names:
#     print(i)

# names = {"Pratik","David","Henry","Mark","Jessica","Jessica","David"}
# print("Utkarsh" not in names)

# in, not in are said to be as membership operators


# fruits = {"Banana","Orange","mango","Pineapple","berries"}
# fruits.add("Papaya")

# print(fruits)


# add the sets together 

# num = {1,2,3,4,5}
# char = {'a','b','c','d','e'}

# char.update(num)

# print(char)

# remove() and discrad() - used to remove element from the set
# pop() - it is going to remove random element 
# clear() - it clears up the set 
# del it deletes the set completely 


# union() & update() - it joins up all the items from both sets 
# intersection() - it keeps only the duplicate values from both sets 
# difference() - it keeps the item from the first set that are not in the other set(s)
# symmetric_difference()- it keeps all the items except the duplicates 

# set1 = {'a','b','c'}
# set2 = {1,2,3}

# set3 = set1.union(set2)
# print(set3)

# num1 = {1,2,3,5}
# num2 = {5,4,6,9}

# set3 = num1.difference(num2)
# print(set3)


# Python Dictionaries 

# Key,value

# car_info = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1954,
#     "year" : 1974
# }

# print(car_info)

# changeable
# duplicates not allowed 


# car_info = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1974
# }

# x = car_info["model"]

# that works with the help of get() 

# x = car_info.get("model")
# print(x)

# to get the keys will use keys()

# print(car_info.keys())    #before the change

# car_info["colors"] = ["Yellow","Red","Blue"]

# print(car_info.keys())    #after the change
# print(car_info.values())


# car_info = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1974
# }

# print(car_info.items())

# if "model1" in car_info:
#     print("Yes it's present!")
# else:
#     print("No it's not present!")

# change or update values

# car_info["year"] = 1954

# car_info.update({"colors":["Red","Blue"]})    #another way of updating the items 

# print(car_info)



# car_info = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1974
# }

# car_info.popitem()

# del car_info  it totally deletes the dictionary 
# car_info.clear() #it deletes up all the items from the dict

# print(car_info)


# pop() - it remove the items what key you mention to it 
# popitem() - it removes the last item of the dictionary 

# loops in dictioanries 

# car_info = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1974
# }

# for i in car_info:
#     print(i)

# for i in car_info:
#     print(car_info[i])

# for i in car_info.values():
#     print(i)

# for i in car_info.keys():
#     print(i)

# for x,y in car_info.items():
#     print(f"{x} : {y}")

# Nested Dictionaries

# myfamily = {
#     "child1": {
#         "name":"Prateek",
#         "year":2010
#     },
#     "child2": {
#         "name":"henry",
#         "year":2011
#     },
#     "child3": {
#         "name":"David",
#         "year":2009
#     }
# }

# child1 = {
#         "name":"Prateek",
#         "year":2010
#     }

# child2 = {
#         "name":"henry",
#         "year":2011
#     }

# child3 = {
#         "name":"David",
#         "year":2009
#     }

# myfamily = {
#     "child1": child1,
#     "child2": child2,    
#     "child3": child3
# }

# print(myfamily["child2"]["name"])



# import random 

# print("Welcome to Rock,Paper, Scissor Game!!!")
# choices = ['Rock','Paper','Scissors']

# while True:
#     user_choice = input("Enter your choice (rock,paper, scissors or quit to exit)")
#     if user_choice == "quit":
#         print("Thanks for playing the game!!!")
#         break

#     if user_choice not in choices:
#         print("Invalid Choice. Please choose Rock,Paper, Scissors")
#         continue

#     computer_choice = random.choice(choices)

#     print(f"You choose : {user_choice}")
#     print(f"Computer choose : {computer_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie")

#     elif (user_choice == "Rock" and computer_choice == "Scissors") or \
#    (user_choice == "Scissors" and computer_choice == "Paper") or \
#     (user_choice == "Paper" and computer_choice == "Rock"):
#         print("You WIN!!!")
#     else:
#         print("Computer Win")
    
#     print("-"*30)
    

# functions 


# creating a function 
# def function_name(parameters):
#     statements
#     return 

# # calling a function
# function_name(arguments)


# def p():
#     print("Pratik")

# p()

# def add(a,b):
#     return a+b

# num = int(input("Enter the 1st number :"))
# num1 = int(input("Enter the 2nd number :"))
# print(f"The summation of two numbers is : {add(num,num1)}")

# is_prime() - to check whether a number is a prime number or not 

# def is_prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count = count+1
#     if count == 2:
#         print("It's a prime number")
#     else:
#         print("It's composite number")

# num = int(input("Enter the number to check whether it's prime or not : "))
# is_prime(num)

# def find_gcd(a,b):
#     while b!=0:
#         a,b = b,a%b   #a = 15, b = 3
#     return a

# result = find_gcd(12,15)
# print("The GCD",result)

# from tkinter import * 

# root = Tk()   #adding things to the screen
# root.title("Pratik's Application")
# root.geometry('450x300')

# heading = Label(root,text="Login Form",font=('Arial',20,"bold"),fg= "Red",bg="Black")
# heading.pack(pady=10)

# email_label = Label(root,text="Email")
# email_label.pack(pady = 5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# email_input = Entry(root)
# email_input.pack(pady = 5)

# root.mainloop()


from tkinter import *

root = Tk()
root.title("Calci")
root.geometry('300x400')
root.resizable(False,False)

entry = Entry(root,font=('Arial',14))
entry.grid(row=0,column=0,columnspan=4,pady=10)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('C',4,1),('=',4,2),('+',4,3)
]

for (text,row,col) in buttons:
    if text == 'C':
        Button(root,text=text,padx = 20,pady=20,font=('Arial',14)).grid(row=row,column=col,sticky=N+S+E+W)
    elif text == '=':
        Button(root,text=text,padx = 20,pady=20,font=('Arial',14)).grid(row=row,column=col,sticky=N+S+E+W)
    else:
        Button(root,text=text,padx = 20,pady=20,font=('Arial',14)).grid(row=row,column=col,sticky=N+S+E+W)


for i in range(5):
    root.grid_rowconfigure(i,weight=1)
    root.grid_columnconfigure(i,weight=1)

root.mainloop()