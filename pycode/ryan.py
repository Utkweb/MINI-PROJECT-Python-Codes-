# Python - It is a high-level, interpreted, interactive and object-oriented scripting language.


# Example -
# print("Hello World")

# compiler - It is a program that converts the code written in a high-level language to a low-level language.

# Interpretor - It is a program that converts the code written in a high-level language to a low-level language line by line.


# Data Types - 

# 1. Numbers - int, float, complex
# 2. String - str
# 3. Boolean - bool True/False 0/1

# Keywords - it is a reserved word in python. It cannot be used as a variable name, function name or any other identifier.

# comments - #, ''' ''' , """ """


# # 
# print("Hello World")


# a = True

# print(type(a))

# a = 9
# b = 2

# print("The power : ",a**b)

# format String 

# /
# // - floor division

# operators:
    
#     1. Arithmetic Operators - +, -, *, /, %, //, **


# My favorite subjects are Maths, Science and English.


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print("The sum is: ",a+b)


# conditional statements - if, if-else, if-elif-else


# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print(num, "it is the multiple of 2")

# a = 9
# b =27

# if a>b:
#     print("a is greater than b")
#     if a%2 == 0:
#         print("a is even")
# elif a<b:
#     print("a is less than b")
# else:
#     print("a is equal to b")
    

# loops:- for, while

# for variable in range(1,10,2):
#     statement1


# for i in range(0,11,2):
#     print(i,end=" ")


# variable declaration 
# while condition:
#     statements
#     inc/dec

# piggy_bank = 0
# i = 0
# while i<10:
#     piggy_bank = piggy_bank + i
#     piggy_bank += i
#     i+=1
# print(piggy_bank)

# 1 - 20

# even_sum = 0
# odd_sum = 0
# for i in range(1,21):
#     if i%2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i
# print("The sum of even numbers: ",even_sum)
# print("The sum of odd numbers: ",odd_sum)    
    
# num1 =42
# num2 = 120


# num1 = 120
# num2 = 42


# num1 = int(input("Enter a number: "))  
# num2 = int(input("Enter a number: "))    

# num1  = num1 + num2     
# num2 = num1 - num2      
# num1 = num1 - num2     

# print("The value of num1: ",num1)
# print("The value of num2: ",num2)   


# 1 - 10

# piggy_bank = 0
# for i in range(1,12,2):
#     piggy_bank += i
# print("The sum of odd numbers: ",piggy_bank)


# Nested Loops:-

# Week 1:
#     Day 1:-
#     Day 2:-
#     Day 3:-
#     Day 4:-
#     Day 5:-
#     Day 6:-
#     Day 7:-
# Week 2:


# for var in range(start,end,step):
#     for var in range(start,end,step):
#         statement1
#         statement2
#         statement3
#     statement4
#     statement5
#     statement6

# for i in range(1,4):
#     for j in range(1,5):
#         print(i," ",j)
        
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()



# fibonacci series:-
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# num1 = 0    
# num2 = 1
# result = 0

# print(num1," ",num2,end=" ")
# for i in range(1,11):
#     result = num1+num2
#     print(result,end=" ")
#     num1 = num2
#     num2 = result

# 123 -->  321
# 345 -->  543

# Random generator - random module

# import math 

# print(math.sqrt(25))

# Random Module - it is a module that is used to generate random numbers.

# pip install name_of_module

# import random

# num = random.randint(1,11)
# print(num)


# randint(start, end) - it is a function that is used to generate random integer numbers.
# randrange(start, end, step) - it is a function that is used to generate random integer numbers.

# randrange(1,11,3)

# 1 4 7 10

# Random Genrator Game:- 

# import random

# # starting point
# start = int(input("Enter the lower bound: "))

# # ending point
# end = int(input("Enter the upper bound: "))

# num = random.randint(start,end)

# print("You have only 5 chances to guess the number.")

# count =0

# while count<5:
#     print("Chance: ",count+1)
#     guess = int(input("Enter your guess:"))
    
#     count+=1
    
#     if guess == num:
#         print("Congratulations! You guessed the number right.")
#     elif guess<num:
#         print("Your guess is too low.")
#     elif guess>num:
#         print("Your guess is too high.")
#     else:
#         print("Invalid Input.")


# Type casting: - it is a process of converting one data type to another data type.

# 1. implicit 
# 2. explicit
# int --> float
# float --> int
# int --> str
# str --> int
# str --> float
# float --> str

# a = 4
# print("Before the casting",type(a))  

# # type casting
# b = str(a)
    
# print("After the casting",type(b))  
# print(b)


# a = 4.5   -> str
# name = "R" ->int
# num =20 -> float

# name = "R"
# print("Before the casting",type(name))

# # type casting
# num = int(name)

# print("After the casting",type(num))
# print(num)

# type caste to integer from string 

# n = "20"
# print("Before the casting",type(n))

# # type casting
# num = int(n)

# print("After the casting",type(num))
# print(num)

# Strings - it is a sequence of characters enclosed within single quotes or double quotes or triple quotes.

# 'hello' "hello" '''hello'''

# name = "Ryan"
# print(name)

# multiline string
# sent = '''




# '''

# index - it is a position of a character in a string.
                    # -1
# name = "Ryan Joseph"
        #   012345678910

# print(name[5:])



# name = "Ryan Joseph"
# print(len(name))

# name = "Ryan Joseph"

# 123  321

# num = input("Enter a number: ")
# print(num[::-1])

# num = int(input("Enter a number : "))
# cnt = 1
# sub = (num+1)//2
# for i in range(2,sub+1):
#         if num%i == 0:
#                 cnt+=1

# if cnt == 1:
#         print("Prime")
# else:
#         print("Not Prime")
        
# Brute Force
# Optimal Approach


# 123%10 = 3


# Sum of digits of a number: -

# 123 = 1+2+3 = 6

# num = int(input("Enter a number: "))


# pseudo code:-

# 1. take input from user and store in num
# 2. initialize sum = 0
# 3. while num>0:
# 4.     rem = num%10
# 5.     sum = sum + rem
# 6.     num = num//10
# 7. print(sum)

# num = int(input("Enter a number: "))   #12
# sum = 0
# while num!=0:
#         rem = num%10    #rem =1
#         sum = sum+rem   #sum=5+1 =6
#         num = num//10   #num =1
# print(sum)              #6

# 121   121  --> palindrome
# 123   321  --> not palindrome

# 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153  --> armstrong number



# num = 123

# type casting
# num  = 123
# num1 = str(num)
# num1 = num1[::-1]
# num = int(num1)
# print(num)

# list 
# tuple
# set
# dictionary

# list : - it is a collection of elements enclosed within square brackets and separated by commas.

# list1 =["Apples",1,10.5,True,8,10.5]
# print(list1[0:3])

# ordered
# indexed
# mutable
# duplicate values
# uodation
# deletion

# len()
# print(len(list1))

# list1 = ["ryan","joseph"]
# list2 =[1,2,3,4,5,6,7,8,9,10]
# list3 = [True,False,True,False,True,False,True,False,True,False]
# list4 = [10.5,20.5,30.5,40.5,50.5,60.5,70.5,80.5,90.5,100.5]

# type()
# print(list1[2:])

# slicing :

# WAP to interchange the first and last element of a list.

# test = ["Apples",1,10.5,True,8,10.5]

# test[0],test[5] = test[5],test[0]

# print(test)

# geeksforgeeks
# gfg


# input:
# a = 5
# b = 9


# output: 
# a = 9
# b = 5

# a = 5
# b = 9

# a,b = b,a

# a = a+b
# b = a-b
# a = a-b


# if 5>2:

# test = ["Apples",1,10.5,True,8,10.5]
# if "Apples" not in test:
#     print("NO")
# else:   
#         print("YES")

        
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# if "cherry" in fruits:
#         print("Yes, 'cherry' is in the fruits list")


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# fruits[0:3] = "Guava"
# print(fruits)

# insert() - it is a  built- in function that is used to insert an element at a particular index in a list.
# append() - it is a built-in function that is used to add an element at the end of the list.
# extend() - it is a built-in function that is used to add multiple elements at the end of the list.
# remove() - it is a built-in function that is used to remove an element from the list.

# fruits.insert(1,"Guava")
# fruits.append("Guava")
# print(fruits)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# for i in fruits:
#         print(i)


# lastname = ["Singh","Kumar","Sharma","Gupta","Joseph"]
# firstname = ["Garv","Ryan","Rahul","Rohan","Raj"]

# firstname.extend(lastname)

# print(firstname)


# static 
# dynamic

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits.pop()
# print(fruits)

# python sort list