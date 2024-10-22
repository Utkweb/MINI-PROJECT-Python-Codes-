# the first program of every programmer is to print a Hello World program


# print("Welcome to the world of Python Programming")

# variables : container to store the data

# x = 11    
# a-z, age , num , num1,num2,etc

# comments : # single line comment


'''


lti line comment
'''


# data types :

# 1. int : 1,2,3,4,5,6,7,8,9,10
# 2. float : 1.2,3.4,5.6,7.8,9.0
# 3. str : "Hello World", "Python Programming"
# 4. bool : True, False


# operators : 

# 1. Arithmetic operators : 

# a. Addition : +
# b. Subtraction : -
# c. Multiplication : *
# d. Division : /
# e. Modulus : %
# f. Exponentiation : **
# g. Floor division : //

# a =" 10.587"
# print(type(a))


# a = 19
# b = 10

# print("Addition of a & b is :",a+b)

# Conditional Statements : They are used to check the condition


# 1. if statements 

# if conditons:
#     statements

# age = 15
# if age > 18:
#     print("You are eligible to drive")
# if age < 18:
#     print("You are not eligible to drive")


# 2. if else statements

# if conditons:
#     statements
# else:
#     statements


# a = 9
# b = 15

# if a > b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# 3. if elif else statements

# if conditons:
#     statements

# elif conditions:
#     statements

# else:
#     statements


# a = 10
# b = 9

# if a>b:
#     print("a is greater than b")

# elif a<b:
#     print("b is greater than a")

# else:
#     print("a is equal to b")

# loops :

# 1. for loop

# for variable_name in range(start,end,step):
#     statements

# for i in range(1,101,1):
#     print(i)

# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")
# print("Aarohi")




# 2. while loop

# while condition:
#     statements

#     increment/decrement

# 1 2 3 4 5 6 7 8 9 10

# i = 1
# while i<=10:
#     print(i)
#     i = i+1

# 1. Try to print the number in reverse order from 10 to 1 using while loop
# 2. Try to print the even numbers from 1 to 100 using while loop
# 3. Try to print the odd numbers from 1 to 100 using while loop
# 4. Try to print the sum of the numbers from 1 to 100 using while loop
# 5. Try to print the sum of the even numbers from 1 to 100 using while loop



# num = int(input("Enter the value :"))

# print(num)


# random module -

# import random

# num = random.randint(1,10)

# print(num)


# Number guessing game

# import random

# print("Welcome to the Number Guessing Game 🔢")
# print("You are gonna guess the number between 1 to 20. You have only 5 chances.")

# secret_number = random.randint(1,20)

# max_attempts = 5
# attempts = 0

# while attempts < 5:

#     guess = int(input("Guess the number : "))
#     attempts = attempts + 1    # attempts = 5

#     if guess == secret_number:
#         print("Congratulations You've won the game in ",attempts,"attempts!!!")
#         break
#     elif guess > secret_number:
#         print("Your guess is to high!!!")
#     else:
#         print("Your guess is too low!!!")

# if attempts == max_attempts:
#     print("You ran out of chances. Game Over !!!")


# list 

# rock , paper , scissor game!!!

# rock paper
# paper scissor
# scissor rock


# name = "Aarohi"
# age = 11

# print("My name is",name,"and I'm ", age,"old")

# formatting string

# print(f"My name is {name} and I'm {age} years old")

# My name is Aarohi and I'm 11 years old

# name = "Aarohi"

# name = str(input("Enter the name : "))
# age = int(input("Enter the age : "))

# print(name)


# name = "circumstances"

# print(name[-1])

# Slicing
# name = "circumstances"

# print(name[7:-3])

# index -> it helps you to access the characters


# positiving inndexing - # It starts from 0 as always and go ahead
# Negative indexing - it starts from -1 at the last character of the variable 

# word = "Stats"

# print(word[::-1])


# name = "circumstances"

# print(f"The length of the {name} is {len(name)}")


# name = "Aarohi"
# age = 11

# print("My name is",name,"and I'm",age,"years old")



# print(f"My name is {name} and I'm {age} years old")


# name = "Aarohi"

# for i in name:
#     print(i)



# Membership Operators

# in - including 
# not in - excluding 


# name = str(input("Enter the name : "))
# vowel='AEIOUaeiou'
# count = 0
# for i in name:
#     if i in vowel:
#         count = count + 1

# print(f"My name consist of {count} vowels.")


# name = "Utkarsh"
# print(len(name))


# name = "Alexander"
# print(name[-8:-3])


# using the loops with strings

name = "Alexander"
count = 0

for i in name:
    if i == 'e':
        count = count+1

print(count)
    