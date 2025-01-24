# def solution(A):
#     department_count = {}

#     for department in A:
#         if department in department_count:
#             department_count[department] += 1
#         else:
#             department_count[department] = 1

#     max_count = max(department_count.values())
#     return max_count











# # def solution(S):
# #     stack = []

# #     for token in S.split():
# #         if token.isdigit():
# #             stack.append(int(token))
# #         elif token == "DUP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.append(stack[-1])
# #         elif token == "POP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.pop()
# #         elif token == "+":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() + stack.pop()
# #             stack.append(result)
# #         elif token == "-":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() - stack.pop()
# #             stack.append(result)

# #     if len(stack) == 0:
# #         return -1  # Error: Stack is empty

# #     return stack[-1]





# # def solution(S):
# #     stack = []

# #     for token in S.split():
# #         if token.isdigit():
# #             stack.append(int(token))
# #         elif token == "DUP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.append(stack[-1])
# #         elif token == "POP":
# #             if len(stack) < 1:
# #                 return -1  # Error: Not enough elements in the stack
# #             stack.pop()
# #         elif token == "+":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() + stack.pop()
# #             if result >= 2**20:
# #                 return -1  # Error: Overflow
# #             stack.append(result)
# #         elif token == "-":
# #             if len(stack) < 2:
# #                 return -1  # Error: Not enough elements in the stack
# #             result = stack.pop() - stack.pop()
# #             if result < 0:
# #                 return -1  # Error: Underflow
# #             stack.append(result)

# #     if len(stack) == 0:
# #         return -1  # Error: Stack is empty

# #     return stack[-1]

# # def main():
    
# #     # Call the solution function
# #     result = solution(S)


# a = 7
# b = 9


# print(a+b)

# a+b 

# operands 

# operators


# a = 7
# b = 9

# a = a+b  # a=16
# b = a-b  #b =7
# a = a-b  #a =9

# # a,b = b,a

# print(a,b)


# a = 9
# b = 7

# String formatting 

# name = "Ryan"

# print("Hello, How are you?", name)







# def add():
#     print("Hello, How are you?")
#     print("Hello, How are you?") 


# # main function
# add()


# a+b

# operators and operands

# print("Anvi")


# Type casting :-


# a = 10.5
# print(type(a))

# Data types: - 

# 1. int   # 1,2,3,4,5,6,7,8,9,10
# 2. float  # 1.2, 2.3, 3.4, 4.5
# 3. str      # "Anvi", "Shiven", "Rahul"
# 4. bool     # True, False
# 5. list
# 6. tuple
# 7. dict
# 8. set


# isGreet = True
# if isGreet == False:
#     print("Hello, How are you?")
# else:
#     print("Bye, Take care")
    


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(a[3:7])

# a = 9
# b = 3
# print(a%b)

# // # floor division
# % # modulus



# type casting : - 

# a = 10
# b = str(a)

# print(b)
# print(type(b))


# print(type(a))

# num = 321 # 123
# print(num%10)

# for i in range(1,11,2):
#     print(i)

# operators and operands

# a = int(input("Enter a number: "))  2
# b = int(input("Enter a number: "))   3

# if a+b > 10:
#     print("TO high")
# else:
#     print("Too low")

# Pseudo code:- 

# 1. two variables a and b
# 2. take input from user and store in a and so in b
# 3. check if a+b is greater than 10
# 4. if yes, print "Too high"
# 5. else, print "Too low"

# truth table of AND operator: -

# a   b   not(a or b)
# 0   0     1
# 0   1     0
# 1   0     0
# 1   1     0



# a = 10
# print(type(a))

# int 
# float
# string
# boolean

# list 
# tuples
# dictionary
# set

# list1 =["Apples",1,10.5,True]
# list1.insert(1,"Mangoes")
# print(list1)


# for i in range(1,11,2):
#     print(i,end=" ")

# age = int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible for driving the car")
# else:
#     print("You are not eligible for driving the car")


# 189

# print(189%10)



# a = "141"
# b = "Nidhi"
# print(b*3)





# a = 10
# b = 5
# print('''
#       1. Addition
#       2. Subtraction
#       3. Multiplication
#       4. Division
#         ''')
# num = int(input("Enter your choice: "))

# if num ==1:
#     print(a+b)
# elif num ==2:
#     print(a-b)
# elif num ==3:
#     print(a*b)
# elif num ==4:
#     print(a//b)
# else:
#     print("Invalid choice")





# a = 9
# b = 10

# print(a/b)

# % # modulus


# 5%2 = 1



# a  = True/False   #boolean   -> bool
# a = 10.2      #float
# a = "Anvi"    #string
# a = 10        #int

# a = False

# print(type(a))


# 1 2 3 4 5 6 7 8 9 10

# loops: - for, while

# for i in range(1,11):
#     print(i,end=" ")






# firstname = True/1
# surname = False/0

# print(firstname+surname)




# Boolean Table  of Or operator: -

# a   b   a or b

# 0   0     0
# 0   1     1
# 1   0     1
# 1   1     1







# main function


# print(5%2)

# a = 1204889
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")
    




# Python-

# print("Hello Devan, How are you?")

# java-

# class Devan{
#     public static void main(String args[]){
#         System.out.println("Hello Devan, How are you?");
#     }
# }

# a = 10
# b = >10
# print(a<b)



# 1 2 3 4 5 6 7 8 9 10

# for i in range(1,11,2):
#     print(i,end =" ")


# if else statement - /

# age = int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible for driving the car")
# else:
#     print("You are not eligible for driving the car")



# a = 10
# b = 7

# # string formatting
# print("The multiplication of two numbers are : ",a*b)


# print(10+5)




# print("Hello, how r u ?", end=" ")
# print("Welcome to the world of python")




# variables:
    
# a = "Abdullah"

# integers  -infinity to +infinity
# String   - "Abdullah"


# a = 9

# print(a)

# a+b


# operators: - +
# operands: -a,b


# a = 9
# b = 10

# print(a+b)





# fname = "Aamir"
# lname = "Rana"
# print(fname,lname)


# int
# long
# float
# double

# print(15+19)


# any number - int
# any number with decimal - float
# any word or sentence - string


# name = "Eshaal"

# print(name)

# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Create a line plot
# plt.plot(x, y, label='Sample Line')

# # Add labels and title
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Line Plot')

# # Add a legend
# plt.legend()

# # Display the plot
# plt.show()





# num = "7"
# num1 = 16.4

# # we are checking the type of num variable
# print(type(num))
# print(type(num1))

# type() -> int, float, str, bool


# python data types:-
# Integer -> any values in numbers without decimals 
# Float -> 1.2,10.5, 11.6
# String -> "Anvi", "Shiven", "Rahul"







# print("Welcome to the class of Python, Ahana Iyer!!!")


# print(156*8795)

# a = 10
# b = 20
# print(a+b)


# a = 10
# print(type(a))

# type() - > int, float, str, bool


# data types :- 

# 1. int -> (-ve numbers to +ve numbers)
# 2. float -> decimal numbers(10.5, 11.6)
# 3. string -> "Anvi", "Shiven", "Rahul"
# 4. boolean -> True, False 0,1


# //
# /



# 25/3 = 8.333333333333333

# 25//3 = 8


# 1 2 3 4 5 6 7 8 9 10

# for x in range(10):
#     print(x)

# syntax:
    
# for variable in range(start,stop,step):
#     statements

# for x in range(1,11):
#     print(x,end = " ")


# a = 10
# print(type(a))


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# arr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# dictionalry 


# tuples i can't change the values -> type casting

# type casting -> changing the data type of a variable

# 1) implicit type casting
# 2) explicit type casting

# order -> int -> float -> string -> boolean



# a = 10.5
# b = int(a)
# print(b)

# input 

# a = 10
# b = 20

# output

# a = 20
# b = 10


# print("Welcome to the class Stephen!!!!!!")






# Python :

# 1. Python is a high-level, interpreted, interactive and object-oriented scripting language.


# print("Welcome to the class of Python")

# Data types : 

# 1. Integer(int) -> It stores whole numbers, 1,2,3,4,5
# 2. Float(float) -> it stores decimal values, 10.5, 11.6
# 3. String(str) -> "Anvi", "Shiven", "Rahul","Welcome to the class",'a','b'
# 4. Boolean(bool) -> True, False, 0,1
# 5. List 
# 6. Tuple
# 7. Dictionary
# 8. Set

# Desktop Application 
# Web Application
# Mobile Application
# Data Science
# Machine Learning
# Artificial Intelligence
# Moules or libaries in python:- OpenCV
# Django framework - web development 



# a = 10
# b = 20

# print(a+b)

# s = "Nipun"
# print(s[::-1])

# array : 

# 1. list
# 2. tuple
# 3. dictionary
# 4. set



# l1 = ('tom', 'jerry', 'micky', 'minnie')

# print(l1)

# t1 = list(l1)

# t1[0] = 'donald'

# l1 = tuple(t1)

# print(l1)


# s1 = {1,2,3,4,2,3,2,32,1}
# print(s1[0])




# type casting = changing the data type of a variable

# OOPS = Object Oriented Programming System

# four pillars :

# 1. Inheritance - 
# 2. Polymorphism 
# 3. Encapsulation
# 4. Abstraction





# in the variable we can store numbers, alphabets,words,special characters and many more

# a = 7
# b = 9
# name = "Kareena"

# c = 7.0258
# flag = True

# Data types :

# 1. int -> 1,2,3,4,5,6,7,8,9,10
# 2. float -> 1.2, 2.3, 3.4, 4.5
# 3. str -> "Anvi", "Shiven", "Rahul"
# 4. bool -> True, False

# opencv




# print("Welcome to the demo class of Python Programming")

# a = 7
# b = 5

# print(a+b)

# data types:

# 1. Integer : 

# examples: 7,5,9,12,etc.

# 2. Float: it stores the values that is having decimals in it
# examples:4.37,3.14,etc

# 3. String : It stores characters,words and even sentences.

# example: "Pratik","Python Programming",etc




# We can solve problems 
# We can make desktop application,web application


# print("Harman")



# Desktop Application
# Machine Learning / AI
# Web Application



# print("Welcome to the Python Classes Ninad!")

# Variables : 

# num = 15

# data types:

# 1. Integer: 






# print("Aditya")

# a = 9
# name = "Aditya"
# pi = 3.14
# flag = True

# Data types:

# 1. Integers (int) : You can suppose all the values that doesn't have decimals 
# 2. Float (float) : It contains the number with decimals in it
# 3. String (str) : It contains characters,words and even sentences 
# 4. Boolean (bool) : It contains the value as True or False



# import numpy 

# marks = [94,86,42,68,98,22,56,28]

# x = numpy.mode(marks)

# print(x)





# print("Nihal")
# print("Nihira")



# modules : numpy,pandas

# print(8+9)


# a = 8
# b = 9

# print(a-b)


# -1,2,5,8,3,4,-5,-9,-147,,etc

# +,-,*,/,//,%,**

# a = 21
# b = 5

# print(a/b)
# print(a//b)
# print(a%b)


# base = 4
# power = 3

# print(base**power)





# Code and solve problems 
# Application development 
# Web Development 
# ML/AI
# Data Science 


# variables/

# a = 8

# age = 17

# Data types : 

# Integers (int) : -ve infinity to +ve infinity (without the decimals)
# Float (float) : 4.18.3.14,etc 
# Strings (str) : It stores words,characters and sentences . name = "Welcome to the class of Python"
# Boolean (bool) : It stores the value in terms of true or false


# a = 9.025
# print(type(a))






# print("Hello How are you?")

# loops :   They are being used to make the code more efficient and less time consuming and also you can multiple times


# 1. for loop - 

# Syntax : 
# for variable_name in range(start,stop,steps):
    #statements

# for i in range(1,11):
#     print(i,"Kush")

# 2. while loop - 

# syntax:

# while condition:
    # statements

# num = 10

# while num!=0:
#     print(num,end=" ")
#     num = num - 1


# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()


# num = [1,5,7,6,2,9,3,5,8]

# print(num[2])


