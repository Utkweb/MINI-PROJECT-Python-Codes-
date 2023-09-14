# a = int(input("Enter a number: "))
# print("The square of the number is: ", a**2)


# name = "Shiven"
# age = 18



# # String formatting

# print("My name is: ",name, "and my age is: ", age)

# a = True
# print(type(a))

# Operators and operands:-

# Operators are special symbols in python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.


# a+b

# operators: +
# operands: a,b

# Arithmetic operators:-

# 1. Addition: +
# 2. Subtraction: -
# 3. Multiplication: *
# 4. Division: /
# 5. Modulus: %
# 6. Exponentiation: **              
# 7. Floor division: //
# 8. Assignment: =

# Comparison operators:-
# 1. Equal to: ==    
# 2. Not equal to: != 
# 3. Greater than: >
# 4. Less than: <
# 5. Greater than or equal to: >=
# 6. Less than or equal to: <=


# in & not in operators:-
# 1. in: Returns True if a sequence with the specified value is present in the object
# 2. not in: Returns True if a sequence with the specified value is not present in the 
# object.

# Identity operators:-
# 1. is: Returns true if both variables are the same object
# 2. is not: Returns true if both variables are not the same object

# Logical operators:-
# 1. and: Returns True if both statements are true
# 2. or: Returns True if one of the statements is true
# 3. not: Reverse the result, returns False if the result is true
# 4. xor: Returns True if one of the statements is true but not both
# 5. nand: Returns False if both statements are true
# 6. nor: Returns False if both statements are false
# 7. xnor: Returns True if both statements are true or both statements are false
# 8. xand: Returns True if both statements are false or both statements are true


# if statements
# if else statements
# if elif elif ..... else statements


# if statements:

# if condition:
#     statement

# num = int(input("Enter a number: "))
# if num >10:
#     print("The number is greater than 10")
# else:
#     print("The number is less than 10")

# a = 10
# b = 3
# print(a//b)

# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:

# age = int(input("enter the number between 1 to 7 "))
# if age>18:
#     print("You are eligible to vote")
# elif age==18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")   


# 1. Sunday
# 2. Monday
# 3. Tuesday
# 4. Wednesday 


# loops : for loop, while loop

# for loop: 
    
# syntax:
    
# for i in range(start, stop, step):
#     statement


# Shiven 

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30


# piggy_bank = 0
# for i in range(0,11):
#     print(i) 

    
    
# 2 to 30
# 1 to 27 



# 2x1 = 2
# 2x2 = 4
# 2x3 = 6
# 2x4 = 8
# 2x5 = 10
# 2x6 = 12
# 2x7 = 14
# 2x8 = 16
# 2x9 = 18
# 2x10 = 20



# num = int(input("Enter a number of which you want the table of ?: "))

# print("The table of ",num,"is: ")
# print(" \n")
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)
#           8  X 1 = 8

# while loop

# for i in range(start,end,step):
    
    
# intialization
# while condition:
#     statement
#     increment/decrement


    
# while condition:
#     statement
#     increment/decrement

# i = 1
# while i<=10:
#     print(i)
#     i = i+1



# num = int(input("Enter the number you wanna reverse : "))   
# sum = 0
# while num!=0:
    
#     rem = num%10              
#     sum = sum*10 +rem         
#     num = num//10             
    
# print("The reverse of the number is: ",sum)





# print(3//10)




# num = int(input("Enter the number to check whether a number is palindrome or not: "))
# temp = num
# sum = 0
# while num!=0:
#     rem = num%10
#     sum = sum*10 + rem
#     num = num//10

# if sum == temp:
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")

# Nested Loops : 
    
for i in range(1,6):
    for j in range(1,i+1): 
        print("*",end=" ")
    print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# *
# **
# ***
# ****
# *****

