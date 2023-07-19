# Python: It is a programming language 
 
# Features of Python:
    
# 1. Python is a high-level language
# 2. Python is an interpreted language
# 3. Python is a general-purpose language
# # 4. Python is an object-oriented language
# # 5. Python is a dynamically typed language


# write our first python program :
    
# print("Aarush")

# Operators and operands:
    
# # Operators: +,-,*,/,%,//,**

# +: addition

# a = 10
# b = 9
# print(a+b)

# variable: It is a container which stores the value

# a = 11
# b = 5
# print(a%b)


# //
# /

# %: modulus

# a = 4
# print(a**3)

# comments: It is a statement which is not executed by the interpreter

# this is a single line comment
# print("Aarush Lakhani ")

''' this is a single line comment
this is a multi line comment
this is a multi line comment '''

# b = 10  #integer
# a = "Aarush" #string
# print(a)

# data types: It is a type of data which is stored in the variable

# 1. Integer: It is a whole number  1,2,3,4,5,6,7,8,9,10   int
# 2. Float: It is a decimal number  1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5  float
# 3. String: It is a collection of characters  "Aarush"    str
# 4. Boolean: It is a True/False or 1/0                      bool
# 5. List: It is a collection of data of different data types [1,"aarush",3.5,4,5,6,7,8,9,10]  list
# 6. Tuple: It is a collection of data of different data types (1,2,3,4,5,6,7,8,9,10)  tuple
# 7. Dictionary: It is a collection of data of different data types {1:"Aarush",2:"Lakhani"} dict   
# 8. Set: It is a collection of data of different data types {1,2,3,4,5,6,7,8,9,10} set

# keywords: It is a word which is reserved by the interpreter

# # if = 10
# f = 10

# a = True
# print(type(a))

# casting : It is a process of converting one data type into another data type


# string formatting 

# subjecta = "Maths"
# subjectb = "Science"
# subjectc = "English"

# print("My favourite subjects are",subjecta,subjectb,"&",subjectc)

# random 

# import random 

# x = random.randint(1,10)
# print("You've only 5 chances !")

# count = 0

# while count<6:
#     count=count+1
#     guess = int(input("Guess a number: "))
#     if x ==guess:
#         print("Congratulations you did it in ",count,"try")
#         break
#     elif x>guess:
#         print("You guessed too small!")
#     elif x<guess:
#         print("You guessed too high!")
# if count>=6:
#     print("Sorry you lost the game! The number is",x)


# a = 4
# b = 9
# c = 5

# print("The average of the three numbers are : ",(a+b+c)/3)


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("The addition of the two numbers are : ",a+b) 