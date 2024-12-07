# Variables :  We can sore values in it

# int a = 9;

# a = True

# Data types : 

# 1. Integer(int) 
# 2. FLoat(float) 
# 3. String(str) 
# 4. Boolean(bool) 

# print("Welcome to the class of Python Diva!")

# a = 9
# b = 8

# print(a+b)

# Operators 

# 1. Addition +
# 2. Subtraction -
# 3. Multiply *
# 4. Division /
# 5. Floor Division //
# 6. Modulus %
# 7. Exponential **

# base ** power

# base = 2
# power = 4

# print(base ** power)

# how we take the input from the users

# a = float(input("Enter the number : "))

# print(type(a))

# type() - It helps you to check the variable is of which data type


# 1. if statement

# syntax:

# if condition:
#     statements

# num = int(input("Enter the number  : "))
# if num>10:
#     print("The number is greater than 10")
# elif num == 10:
#     print("the number is equal to 10 ")
# else:
#     print("The number is not greater than 10")

# if else:

# if elif else


# num = int(input("Enter a number:"))
# if num%2 == 0:
#     print("This number is even.")
# else:
#     print("This number is odd.")


# check between two numbers which one is greater and check if they are equal as well 

# num1 = int(input("Enter a number."))
# num2 = int(input("Enter another number."))

# if num1 > num2:
#     print("num1 is greater than num2")
# elif num2 > num1:
#     print("num2 is greater than num1.")
# else:
#     print(" num1 and num2 are equal.")
    

# loops:

# 1. for loop

# syntax:

# for variable_name in range(start,end,steps):
#     statements

# for i in range(1,11,2):
#     print(i)


# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 5 10 15 20 25 30 35 40 45 50
# 1 4 9 16 25 36 49 64 81 100
# 10 9 8 7 6 5 4 3 2 1

# 2. While loop

# syntax:

# initailization
# while condition:
#     statements


# i = 1
# while i<11:
#     print(i)
#     i = i+1


# 1234%10 = 4*10 = 40 +3 = 43*10 =430+2 = 432*10 = 4320+1 = 4321
# 123%10 = 3
# 12%10 = 2
# 1%10 = 1


# num = int(input("Enter the number to make it reverse : "))  #num = 456
# ans = 0
# while num!=0:
#     rem = num % 10   #rem = 4
#     ans = ans * 10 + rem   # ans = 654
#     num = num // 10   #num = 0

# print(ans)


# num = int(input("Enter a number to give the sum of its digits: "))
# sum = 0
# while num != 0:
#     rem = num % 10 
#     sum = sum + rem
#     num = num // 10

# print(sum)


# 0 1 1 2 3 5 8 13 21

# prev = 0
# current = 1
# print(prev,current,end=" ")
# for i in range(2,11):
#     next = prev+current
#     print(next,end=" ")
#     prev = current
#     current = next





# 369 

# 3 + 6 + 9 = 18


# Array :

# 1. List

# It is changeable/mutable
# It is being identified by []
# It allow duplicate element 

# num = [1,4,8,9,4,5,6,8,0]
# cars = ["Mercedez","Audi","toyato","Honda"]
# mix = ["Utkarsh",21,12.5,True]

# fruits = ["Cherries","blueberry","Apple","banana","Orange"]

# How to get the length of the function
# len() 

# print(len(fruits))


# Indexing - to access the values 

# 1. positive indexing - it starts from left to right from 0 to n-1
# 2. Negative indexing - it starts from right to left -1 to -n

# print(fruits[4])
# print(fruits[-1])

# Slicing 

# print(fruits[1:3])

# [start:end:steps]

# accessing the list with loops 

# fruits = ["Cherries","blueberry","Apple","banana","Orange"]

# for i in range(0,len(fruits)):
#     print(fruits[i])

# for i in fruits:
#     print(i)


# cars = ["Audi", "Mercedes", "Vauxwagon", "Ford"]
# num = str(input("Enter a car name: "))
# for i in range(0, len(cars)):
#     if cars[i] == num:
#         print(i)

# membership operators 

# 1. in 
# 2. not in

# cars = ["Audi", "Mercedes", "Vauxwagon", "Ford"]
# num = str(input("Enter a car name: "))
# if num in cars:
#     print("present")


# num = [1,8,9,6,7,3,5]
# sum = 0
# for i in num:
#     sum +=i
# print(f"Sum of all numbers : {sum}")


# num = [1,8,9,6,7,3,5]
# sum_even = 0
# sum_odd = 0
# for i in num:
#     if i %2 == 0:
#         sum_even += 1
#     else:
#         sum_odd += 1
# print (f"Sum of even numbers : {sum_even}")
# print (f"Sum of odd numbers : {sum_odd}")


# Adding the element in the list 

# 1. append() - It helps us to add the element the end of the list

# cars = ["Audi", "Mercedes", "Vauxwagon", "Ford"]
# cars.append("Lamborghini")

# print(cars)


# 2. insert() -  it helps to add the element at the desired position

# cars = ["Audi", "Mercedes", "Vauxwagon", "Ford"]
# cars.insert(1,"Lamborghini")

# print(cars)


# Removing the element 

# 1. remove() - It helps you to delete the element you need to write the element in the brackets 


# cars = ["Audi", "Mercedes", "Vauxwagon", "Ford"]
# cars.remove("Vauxwagon")

# print(cars)

# 2. pop() - It helps you to remove the element 


# cars = ["Audi", "Mercedes", "Vauxwagon", "Ford"]
# cars.pop(0)

# print(cars)


# num = [1,5,9,7,5,3,6,4,8,2,1,4,5,9,78,6,3,0,47,1]
# ans = []
# for i in num:
#     if i not in ans:
#         ans.append(i)

# print(ans)


# 2. tuple - It is ordered and unchangeable / immutable
# It allow duplicate element 
# It is represented by ()

# num = (1,2,7,3,4,5,6)

# num = (1,)
# print(type(num))

# Type casting - changing the data type from one to another 

# 1. implicit type conversion - 

# 2. Explicit type conversion


# num = (1,2,7,3,4,5,6)

# num1 = list(num)

# num1[-2] = 11

# num = tuple(num1)

# print(num)

# join tuples

# concatenation

# num = (1,2,3,4,5)
# num1 = (7,8,9,10)

# print(num+num1)

# replication 

# num = (1,2,3)
# print(num*3)


# 3. set

# Unordered, unchangeable /immutable and unindexed.
# You are allowed to add or delete the elements
# {} curly brackets 

# names = {"David","James","James","James","James","Jessica","Vamsi","Creg","Creg"}

# for i in names:
#     print(i)

# add the items to the set

# add() - 

# haloween = {"Autum","Ambrose","Draco"}
# haloween.add("Dexter")

# print(haloween)

# update() - 

# haloween = {"Autum","Ambrose","Draco"}
# names = {"David","James","James","James","James","Jessica","Vamsi","Creg","Creg"}

# haloween.update(names)

# print(haloween)

# .remove() - 

# haloween = {"Autum","Ambrose","Draco"}
# haloween.remove("Ambrose")

# print(haloween)

# Join Sets 

# union() -  

# set1 = {1,2,3}
# set2 = {"a","b","c"}
# set3 = {"e","f","r"}
# set4 = {"o","m","l"}

# # set3 = set1.union(set2)
# set = set1 | set2 | set3 | set4

# print(set)

# Intersection  - 

# seta = {"Diva","James","George"}
# setb = {"Utkarsh","George","lewis"}

# # set3 = seta.intersection(setb)
# set3 =  seta & setb
# print(set3)

# seta = {"Diva","James","George"}
# setb = {"Utkarsh","George","lewis"}

# seta.intersection_update(setb)
# print(seta)

# difference 


# seta = {"Diva","James","George"}
# setb = {"Utkarsh","George","lewis"}

# # print(seta.difference(setb))
# print(seta - setb)


# Unique Elements from a List

# Write a function get_unique_elements(lst) that takes a list of integers and returns a set of unique elements in the list.


# l1 = [1,5,9,7,8,6,3,2,4,1,5,9,8,7,5,3,6,4,2,1]

# s1 = set(l1)
# print(s1)

# Hello world hello 
# set = str(input("Enter a sentence:"))
# for i in set:
    
# set1 = str(input("Enter a sentence:")).lower()

# words = set1.split()
# unique = set(words)

# print(len(unique))




# 4. dicitonary

# key : value 
# mutable 

# dict1 = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964,
#     "year" : 2100,
#     "colors" : ["Red","Yellow","black","White"]
# }

# print(type(dict1))

# dict1 = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964,
#     "colors" : ["Red","Yellow","black","White"]
# }

# print(dict1["model"])
# get() -  

# x = dict1.get("model")
# print(x)

# to get all values and keys 

# print(dict1.keys())
# print(dict1.values())

# accessing the values inside the dictionary
# print(dict1["colors"][2])

# updation
# dict1["year"] = 2100

# print(dict1)


# dict1 = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964,
#     "colors" : ["Red","Yellow","black","White"]
# }

# # items() - 

# print(dict1.items())

# dict1 = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964
# }

# dict1["colors"] = "red"
# print(dict1)


# dict1 = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964,
#     "colors" : ["Red","Yellow","black","White"]
# }



# pop()

# dict1.pop()

# .clear()

# dict1.clear()
# print(dict1)

# dict1 = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year" : 1964,
#     "colors" : ["Red","Yellow","black","White"]
# }

# for i in dict1:
#     print(dict1[i])

# for i,j in dict1.items():
#     print(f"{i} -> {j}")


# family ={
#     "Child 1" : {
#         "name" : "John",
#         "year" : 2001
#     },
#     "Child 2" : {
#         "name" : "Sophie",
#         "year" : 1999
#     },
#     "child 3" : {
#         "name" : "Rebecca",
#         "year" : 2004
#     }
# }

# print(family["Child 2"]["name"])

# 0 1 1 2 3 5 8 13 21 34 

# num1 = 0
# num2= 1

# print(num1,num2,end=" ")
# for i in range(2,11):
#     num3 = num1 + num2 
#     print(num3,end=" ")
#     num1 = num2 
#     num2 = num3


# functions() -  It is used to make 

# defining a function
# def name_of_function(arguments):
    #statements

# calling a function

# name_of_function(parameters)


# def add(a,b):
#     return a+b

# print(add(4,9))

# recursion - calling the function istelf

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*fact(n-1)

# print(fact(5))



# Numpy is a Python Library 
# Numpy is used for working with arrays
# Numpy is short for "Numerical Python"

# how to install the library
# pip install numpy

# import numpy as n 

# arr = n.array([1,2,3,4,5])

# print(arr)
# print(type(arr))

# 0-d arrays 

# import numpy as np 

# arr = np.array(42)
# print(arr)
# 1-d arrays

# import numpy as np 

# arr = np.array([42,54,6,3,6,2,8])
# print(arr)

# 2-d arrays

# import numpy as np 

# arr = np.array([[4,8,1],[6,9,0]])
# print(arr)

# 3-d arrays

# import numpy as np 

# arr = np.array([[[4,8,1],[6,9,0],[4,8,6]]])
# print(arr)

# import numpy as np 


# arr = np.array([[4,8,1],[6,9,0],[4,8,6]])
# print(arr.ndim)

# import numpy as np

# arr = np.array([1,2,3,4,5], ndmin=5)

# print(arr)




# import numpy as np

# arr = np.array([[[1,2,3,4,5],[6,7,8,9,10],[5,3,7,1,5],[1,7,9,6,5]]])
# print(arr[1,1,1])


# import numpy as np 

# arr = np.array([[42,54,6],[6,2,8]])


# print(arr.shape)

# import numpy as np



# # arr = np.array(l)
# arr = np.array([[12,34,56],[87,54,63],[85,92,14]])
# print(arr[0:,0:2])


# import numpy as np




# arr = np.array([[12,34,56],[87,54,63],[85,92,14]])

# for x in arr:
#     for y in x:
#         print(y,end=" ")
#     print()

# Note : We get multiple functions like multiple 

# Join 
# concatenate () - 


# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)


# import numpy as np

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))

# print(arr)



# import numpy as np

# arr = np.array([[12,34,56],[87,54,63],[85,92,14]])

# x = np.where(arr == 63)

# print(x)


# import numpy as np

# arr = np.array([101,20,384,49,554])


# print(np.sort(arr))



# import numpy as np
# import matplotlib.pyplot as plt

# ypoints = np.array([3,5,2,7,3,6,5])

# plt.plot(ypoints,'o-.')
# plt.show()

# syntax:
# pointsline_namecolor_symbol


# '-' = solid line
# ':' = dotted line
# '--' = dashed line 
# '-.' = dashed / dotted line 


# import numpy as np
# import matplotlib.pyplot as plt

# xpoints = np.array([1,10])
# ypoints = np.array([0,5])

# plt.plot(xpoints, ypoints,linestyle="dashed")

# f1 = {'family':'serif','color':'green','size':15}

# plt.title("Anything Graph",fontdict=f1)
# plt.xlabel("x-axis",fontdict=f1)
# plt.ylabel("y-axis",fontdict=f1)

# plt.grid(color='blue',linestyle='dotted',linewidth=1)

# plt.show()


# import matplotlib.pyplot as plt 
# import numpy as np

# #plot 1:
# x = np.array([1,3,4,5])
# y = np.array([8,9,10,13])

# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.title('Plot1')

# #plot 2:
# x = np.array([0,4,7,6])
# y = np.array([1,6,9,3])

# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.title('Plot2')


# plt.suptitle("My Plots")



# plt.show()


# import matplotlib.pyplot as plt 
# import numpy as np

# x = np.array(['A','B','C','D'])
# y = np.array([5,7,9,10])

# plt.bar(x,y,color='#000000',width=0.25)
# plt.show()


# default height = 0.8
# default width = 1



# import matplotlib.pyplot as plt 
# import numpy as np

# x = np.array([24,65,32,22])
# labels1 = ["Apples","Strawberry","Banana","Orange"]
# myexplode = [0,0,0,0.2]
# mycolors = ["Red","hotpink","yellow","orange"]


# plt.pie(x,labels = labels1,explode=myexplode,colors=mycolors)
# plt.legend(title="Four Fruits : ")
# plt.show()


# import matplotlib.pyplot as plt 
# import numpy as np

# x = np.random.normal(160,10,250)

# plt.hist(x)
# plt.show()


# error handling :

# try 
# except 
# else
# finally


# try:
#     print(x)
# except:
#     print("X is not there")

# # print(x)










# print(x)
# x = 8
# try:
#     print(x)
# except:
#     print("x is not defined")

# names = ["Diva","Agarwal","Edin","David","James"]

# try:
#     print(names[4])
# except:
#     print("Out of range")

# x = 7

# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else is wrong")



# try:
#     num = int(input("Enter 1st number : "))
#     num1 = int(input("Enter 2nd number : "))

#     result = num/num1
#     print(result)

# except ValueError:
#     print("Error : Invalid Inputs")
# except ZeroDivisionError:
#     print("Error : Division by 0 is undefined")
# else:
#     print("No errors occured ")
# finally:
#     print("Execution Completed")




# File Handling :

# open() - to open the file 
# two parameters for open() - filename and mode


# "r" = read
# "a" = append
# "w" = write
# "x" = create

# f = open("F:\\diva\hey.txt","r")
# print(f.readline())
# print(f.readline())
# f.close()

f = open("test.txt","a")
f.write("I'm adding a new line in it. It has more content now.")
f.close()

f = open("test.txt","r")
print(f.read())