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





# 2. tuple
# 3. set
# 4. dicitonary