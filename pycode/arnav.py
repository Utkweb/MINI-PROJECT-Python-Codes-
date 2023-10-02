# name = "Arnav"
# age = 10
# print("My name is ", name,"and I'm", age, "years old.")

# # My name is Arnav and I'm 10 years old.

# My favorite color are red, blue, and green.

# Data Types: 
    
# 1. integers - int       
# 2. float - float    10.2, 1.3, 1.4
# 3. string - str     "Arnav"   "Welcome to Python"
# 4. boolean - bool    True/False  1/0


# name = str(input("What's your name ? "))
# print("My name is ", name)

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print(a+b)



# import random 

# a = random.randint(1,10)
# print(a)


# area of square = side * side

# side = int(input("Enter side of sqaure:"))
# print(side**2)

# perimeter of sqaure = 4*side


# Area of rectangle = length * breadth

# length = 9
# breadth = 5

# print(length*breadth)

# Perimeter of rectangle = 2*(length + breadth)

# length = 9
# breadth = 6
# print("Perimeter of Rectangle :",2*(length+breadth))





# if condition:
#     statement1
#     statement2
    
# a = 10 
# b = 20 


# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# person_age = 19
# if person_age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# if elif else statements
# if condition:
#     statement1
# elif condition:
#     statement2
# elif condition:
#     statement3
# else:
#     statement4

# num = int(input("Enter a number:"))
# if num>0:
#     print("The number is positive")
# elif num<0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# loops:- for loop, while loop 

# for variable_name in range(start,end,step):
#     statements
    
# for i in range(1,11,2):
#     print(i)


# 0 2 4 6 8 10 12 14 16 18 20

num = int(input("Enter a number:"))

if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
