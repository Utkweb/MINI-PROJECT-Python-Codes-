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