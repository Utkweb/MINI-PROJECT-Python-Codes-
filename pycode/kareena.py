# Variables - 

# Rules for variable names:
    
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. Variable names cannot contain spaces
# 6 Variable names should be descriptive and meaningful (a variable name like x is not descriptive)

# a = 10
# age = 20

# Data Types -

# Python has the following data types built-in by default, in these categories:

# 1. Integer(int) - Whole numbers, positive or negative, without decimals, of unlimited length.
# example : x = 1, y = 35656222554887711, z = -3255522

# 2. Float(float) - Floating point numbers, positive or negative, containing one or more decimals.
# example : x = 1.10, y = 1.0, z = -35.59

# 3. String(str) - A string in Python is a sequence of characters.
# example : x = "hello", y = 'Kareena', z = "hello"

# 4. Boolean(bool) - Boolean represents one of two values: True or False.

# print("Hey, Kareena how are you?")



# type() - # The type() function returns the data type of the specified object.

# a = False
# print(type(a))

# Operators/operands:

# a+b 

# Operands = a, b
# Operator = +

# Arithmetic Operators:

# 1. Addition (+) - Adds two operands
# 2. Subtraction (-) - Subtracts right operand from the left operand
# 3. Multiplication (*) - Multiplies two operands
# 4. Division (/) - Divides left operand by right operand
# 5. Modulus (%) - Divides left operand by right operand and returns remainder
# 6. Exponent (**) - Performs exponential (power) calculation on operators
# 7. Floor Division (//) - The division of operands where the result is the quotient in which the digits
#  after the decimal point are removed.


# a = 10
# b = 20

# print("Addition :",a+b)


# a = 10
# b = 20


# print("")

# a = 9
# b = 5

# when i print a and b then their values need to be swapped 

# a = 9 - 4 = 5

# only need to use a and b and + and -

# // and *

# a = 9
# b = 5

# a = a*b   #a = 45
# b = a//b   #b = 9
# a = a//b   #a = 5
# a,b = b,a

# print('a :',a)
# print('b :',b)

# Conditional Statements:-

# 1. if statments -checks only 1 condition at a time 

# syntax :

# if condition:
#     statements

# age = int(input("Enter the age of the person : "))

# if age>17:
#     print("you are eligible to drive car")

# 2. if else statements - checks two condition at a time 

# if condition:
#     statments
# else:
#     statements


# age = int(input("Enter the age of the person : "))

# if age>17:
#     print("you are eligible to drive car")
# else:
#     print("You are not eligible to drive the car")

# a = 8
# b = 7


# if elif else statements - it helps you to check three or more condition at a time 

# if conditons:
#     statements
# elif condition:
#     statements
# else:

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# if a>b:
#     print("a greater")
# elif a == b:
#     print("Both are equal")
# else:
#     print("b greater")


# a = 5
# b = 9

# # a needs to be greater than b or less than or equals to 5

# if a>b or a <=5:
#     print("Yes ")

# if a>b and a>c:
#     print("a is greatwe")


# strings : it stores words, sentences and characters

# name = "circumstances"

# index : it helps you to get in touch with each character of the string

# print(name[-2])

# name= "Utkarsh"

# print(name[0:3])

# Concatenation - 

# adding two things together 
# firstName = "Utkarsh "
# lastName = "Singh"


# print(firstName*4)


# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")
# print("Kareena")

# loops:

# 1. for loop

# syntax : 

# for i in range(start,end,step):
#     System.out.println("Kareena")

# for i in range(1,101):
#     print(i,".Kareena")

# 1 10

# 2. while loop


# for i in range(1,101,1):
#     print(i)

# 1 + 2+ 3+... +10  = 55

# piggy_bank = 0 
# for i in range(1,11):
#     piggy_bank = piggy_bank+i
# print("The total sum of elements are : ",piggy_bank)

# 8 X 1 = 8
# 8 X 2 = 16


# formatting up a string


# num = int(input("Enter the value : "))

# print(f"The multiplication table of {num}")

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")



# factorial = 

# 5! = 5*4*3*2*1 = 120

# num = int(input("Enter the number : "))
# piggy_bank = 1
# for i in range(1,num+1):
#     piggy_bank = piggy_bank * i

# print(f"The factorial of {num} is {piggy_bank}")


# 2. while loop

# while condition:
#     statements


# 1 - 10

# i = 10
# while i <= 51:
#     print(i)
#     i = i+1   #i =11

# 10 51


# 123 -> 321

# 3*10 = 30+2 = 32*10 = 320 +1 = 321

# num = 123

# num = int(input("Enter the number : "))
# ans = 0
# while num>=0:
#     rem = num % 10  #rem = 1
#     ans = ans*10+rem   #ans = 321
#     num = num // 10    #num = 1

# print(ans)



# make a small game today

# guess the number 


# Number guessing game 

# 1 - 50 

# targetted number - and that is not known by us, we want to guess the secret number and we have only 5 chance
# to do so.


# random module 

# import random

# num = random.randint(1,20)


# print(num)


# Number guessing game


# import random 

# print("Welcome to Number Guessing Game 🔢")
# print("Try to search up the random number between 1 - 50 and we have only 5 chances")

# secret_number = random.randint(1,50)

# attempts = 0
# max_attempts = 5

# while attempts < 5:
#     guess = int(input('Guess the random number : '))
#     attempts = attempts + 1

#     if guess == secret_number:
#         print('Congratulations you got the right number 😊 in {attempts} attempts.')
#         break
#     elif guess > secret_number:
#         print('You guess too high 😶‍🌫️')
#     else:
#         print('You guess too low 😶‍🌫️')

#     if attempts == max_attempts:
#         print(f'You have no attempts left. Game Over! 😗. The secret number is {secret_number}')


# 0 1 4 9 16 25 36 49 64 81 100\


# Strings : they are the words or sentences



# print(name[2:])

# if we need to print in the reverse order

# print(name[::-1])

# concatenation - it refers to add two string

# print(firstname+lastname)

# replication - to print multiple one thing acc. to you

# print(firstname*100)


# format string 


# firstname = "Kareena "
# lastname = 'Patel'
# age = 13
# country = 'USA'

# print("My name is ",firstname,lastname,"and I'm ",age,'years old and I live in',country,"country")

# print(f"My name is {firstname}{lastname} and I'm {age} years old and I live in this {country} country")


# membership operators 

# in - like if something is there
# not in  - the thing that you are asking is not there

# name = 'Utkarsh'

# if 'z' in name:
#     print("Yes it's there")


# name = "Utkarsh"

# for i in name:
#     print(i)

# name = 'Kareena'

# vowel = 'aeiouAEIOU'
# count = 0

# for i in name:
#     if i not in vowel:
#         count = count+1

# print(f"The count of consonant in {name} is {count}")

# in the email @,.


# email = str(input("Enter the email : "))

# abc@gmail.com

# name = "Utkarsh"
# print(name[2:5])

# print(f"")

# Python Casting : when i want to change the data type from one to another then it's called as type casting

# int
# bool
# float
# String

# num = 35.88
# print(int(num))


# 1. List
# 2. tuple
# 3. set
# 4. Dictionary

# type()


# list - it is a data type to store multiple variables in it 
# The list would look like enclsoed in [] brackets.

# cars = ["Toyato","Honda","Audi","Tesla","Jeep","Mercedez"]
# print(type(cars))


# cars = ["Toyato","Honda","Audi","Tesla","Jeep","Mercedez"]
# print(cars[::-1])



# anything[0] = "Student"

# print(anything)


# changeable
# allow duplicate values


# kareena
# aneeraK


# len() - it helps you to find the length of the list

# anything = ["Kareena",13,10.55,True,59,50.2,45,78,"Utkarsh","Mercedez","apple"]

# print(anything[-2])


# fruits = ["apple","orange","banana","watermelon","grapes","mango","pineapple","cherry","papaya","Strawberry"]

# addding the elements

# append() - it adds the elements at the last of the list
# insert() - it adds the elements at the desired position

# fruits.append("blueberries")
# fruits.insert(3,"blueberries")

# print(fruits)


# import random

# def get_user_choice():
#     print("Make the choices from below : ")
#     print("1. Rock")
#     print("2. Paper")
#     print("3. Scissors")
#     choice = (input("Enter your choice : "))

#     if choice == "Rock":
#         return 'Rock'
#     elif choice == "Paper":
#         return 'Paper'
#     elif choice == "Scissors":
#         return 'Scissors'
#     else:
#         print("Invalid Input!")

# def get_computer_choice():
#     return random.choice(['Rock','Paper','Scissors'])

# def determine_winner(user,computer):

#     if user == computer:
#         return "It's a tie"
#     elif (user == "Rock" and computer == "Scissors") or \
#     (user == "Paper" and computer == "Rock") or \
#     (user == "Scissors" and computer == "Paper"):
#         return "User Wins"
#     else:
#         return "Computer Wins"

# print("Welcome to the Rock,Paper and Scissors Game!")

# user_choice = get_user_choice()
# computer_choice = get_computer_choice()

# print("Users choice : ",user_choice)
# print("Computer Choice : ",computer_choice)

# result = determine_winner(user_choice,computer_choice)
# print(result)



# name = ["Kareena","Utkarsh","Piyush","Aaron","Eden"]
# vowels = "AEIOUaeiou"

# for i in name:

# string





# name = ["Kareena","Utkarsh","Piyush","Aaron","Eden"]
# vowels = "AEIOUaeiou"

# count = 0

# for i in name:
#     if i[0] in vowels:
#         count = count+1

# print("The count of names that are starting up with vowels are ",count)


# num = [2,4,6,8,9,5,3,7]

# sum = 0

# for i in num:
#     if i%2==0:
#         sum=sum+i

# print("The sum of only even element are : ",sum)


# number = [2,4,6,8,3,2,8]

# if 7 in number:
#     print("Exists")
# else:
#     print("Not exists")




# num = int(input("Enter the number of which you wanna check the occurenece of :"))
# count = 0
# for i in number:
#     if i == num:
#         count=count+1
# print("The number of occurences of an element",count)


# num = [1,8,9,3,5,7,4,2,6,14]

# max_num = num[0]

# for i in num:
#     if i > max_num:
#         max_num = i

# print("LArgest Element : ",max_num)


# num = [1,3,5,6,3,7,3,6]
# min_num=num[0]
# for i in num:
#     if i < min_num:
#         min_num = i
# print("Minimum element: ",min_num)


# num = [1,3,5,6,3,7,3,6]

# num1 = []

# for i in num:
#     if i not in num1:
#         num1.append(i)


# print(num1)

# Bubble Sort : it allows you to sort the elements in ascending or descending order.

# 1st pass complete

# 7 3 6 1
# 3 7 6 1
# 3 6 7 1
# 3 6 1 7


# 2nd pass

# 3 6 1 7 
# 3 1 6 7 

# 3 rd pass

# 3 1 6 7
# 1 3 6 7


# arr = [7,3,6,1]

# n = len(arr)

# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]   #swapped the numbers
# print(arr)


# arr = [7,8,5,1,4,3,6,9,4]

# n = len(arr)

# count = 0
# for i in range(n+1):
#     if i%2!=0:
#         count = count+1

# print(count)


# num = [4,6,2,8,7,23,55]

# print(num[::-1])



# [start:end:steps]

# accessing the lists with loops

# num = [4,6,2,8,7,23,55]

# for i in num:
#     print(i)


# 1.  We need to add all the elements of the list 

# num = [4,6,2,8,7,23,55]

# piggy_bank = 0
# for i in num:
#     piggy_bank = piggy_bank + i

# print(f"The sum of all elements in the list are {piggy_bank}")


# We need to know how many even numbers are there in the list


# num = [4,2,5,1,6,7]
# count = 0
# for i in num:
#     if i%2!=0:
#         count = count+1

# print(f"The count of even numbers in the list are {count}")

# We need to find the whether a number exists in the list or not 

# num = [2,3,1,6,7,4]
# target = int(input("Enter the number to search: "))
# flag = False
# for i in num:
#     if i == target:
#         flag = True
#     else:
#         flag = False

# if flag == True:
#     print("The element exist")
# else:
#     print("The elements doesn't exists")


# We need to find out the maximum and minimum number in the list


# Adding up the items in the list 

# 1. append() - It helps us to add the element at the last of the list 
# 2. insert() - It helps us to add the element at the desired location

# fruits = ["Banana","Apple","Orange","kiwi","Cantaloupe","Cherry"]
# print(fruits)

# fruits.append("Watermelon")
# print(fruits)

# fruits.insert(3,"Blueberry")
# print(fruits)


# Removing the elements of the list

# 1. remove() - It helps you to rmeove the elements

# fruits = ["Banana","Apple","Orange","kiwi","Cantaloupe","Cherry"]
# fruits.remove("Apple")
# print(fruits)

# 2. pop() -

# fruits = ["Banana","Apple","Orange","kiwi","Cantaloupe","Cherry"]
# fruits.pop(3)
# print(fruits)



# num = [1,8,9,6,7,2,5,8,6,4,1,8,3,48,1,5]

# ans = []

# for i in num:
#     if i not in ans:
#         ans.append(i)

# print(ans)


# num = [1,3,5,2,1,4,7,2,3,4,4,7]
# ans = []

# for i in num:
#     if i%2 == 0 and i not in ans:
#         ans.append(i)

# print(ans)


# tuples:

# it is ordered and unchangeable
# it is identifiable by round brackets ()

# num = (2,4,5,8,9)

# print(type(num))

# join tuples

# a = (1,2,3,4,5)
# b = (6,7,8,9,10)

# print(a+b)   #concatenation

# Replication

# a = (1,2,3)
# print(a*3)

# Type casting


# fruits = ("Banana","Apple","Orange","kiwi","Cantaloupe","Cherry")

# f = list(fruits)

# f[3]="Strawberry"

# fruits = tuple(f)

# print(fruits)

# num = (2,4,7,3,2,9,1)



# names = ["Kareena","Utkarsh","Adam","Jacob","Mark","henry","James"]
# vowels = "AEIOUaeiou"
# count = 0
# for i in names:
#     if i[0] in vowels:
#         count = count +1
# print(f"The names starting with vowels are {count}")

# how many names are starting with vowel?

# print(names)


# Kareena
# Utkarsh
# Adam
# Jacob
# Mark
# henry
# James



# Set - it helps you to store multiple elements in a single variable

# it is uncordered, unchangeable, and unindexed
# it is indentified as {}
# it doesn't allow duplicate values

# print(fruits)


# num = [1,3,6,2,1,5,3,9,8]

# ans = set(num)
# print(ans)


# fruits = {"apple","papaya","orange","Mango","cherry","cherry","orange"}
# print("orange" not in fruits)

# add the item to the sets

# fruits = {"apple","papaya","orange","Mango","cherry","cherry","orange"}

# fruits.add("pomegranate")
# print(fruits)


# add two sets

# fruits = {"apple","papaya","orange","Mango","cherry","cherry","orange"}
# vegetables = {"peppers","lettuce","tomato","potatoes","lady finger"}

# fruits.update(vegetables)

# print(fruits)

# delete an element from the sets 
# fruits = {"apple","orange","Mango","cherry","cherry","orange"}
# fruits.remove("papaya")

# print(fruits)

# discard() - to delete element

# fruits = {"apple","orange","Mango","cherry","cherry","orange"}
# x = fruits.pop()

# print(x)
# print(fruits)

# resturants = {"Burger King", "Mcdonalds", "KFC", "Sonic", "Wendy's"}
# for i in resturants:
#     print(i)

# dictionaries

# It is used to store data values in terms of key:value pairs
# it is ordered and do not allow duplicate value and they are chageable 

# cars = {
#     "brand" : "Mercedez",
#     "Model" : "GWagon",
#     "year" : 2015,
#     "year" : 2019
# }

# print(cars["year"])

# len() -  it is used to find the length of the dictionary 


# cars = {
#     "brand" : "Mercedez",
#     "Model" : "GWagon",
#     "year" : 2019,
#     "colors" : ["red","black","white","Green"]
# }

# print(cars["colors"][2])

# cars = {
#     "brand" : "Mercedez",
#     "Model" : "GWagon",
#     "year" : 2019,
#     "colors" : ["red","black","white","Green"]
# }

# if "Model" not in cars:
#     print("Present")

# Access the items 

# .get() - 

# car_name = cars.get("Model")

# print(car_name)

# print(f"All the keys {cars.keys()}")
# print(f"All the values {cars.values()}")

# items

# print(cars.items())



# cars = {
#     "brand" : "Mercedez",
#     "Model" : "GWagon",
#     "year" : 2019,
#     "colors" : ["red","black","white","Green"]
# }

# # Add a new key:value pairs

# # cars["Owner"] = "kareena"
# # cars.update({"owner":"Kareena"})
# print(cars)


# deleting

# cars = {
#     "brand" : "Mercedez",
#     "Model" : "GWagon",
#     "year" : 2019,
#     "colors" : ["red","black","white","Green"]
# }

# it deletes the specific key value pair
# cars.pop("colors")

# it deletes the last key:value pairs
# cars.popitem()

# it deletes the dictionary completely
# del cars

# it clears up the dictionary and shows up the empty dictionary 
# cars.clear()

# print(cars)


cars = {
    "brand" : "Mercedez",
    "Model" : "GWagon",
    "year" : 2019,
    "colors" : ["red","black","white","Green"]
}

# for i in cars:
#     print(f"{i} : {cars[i]}")

# for i in cars.keys():
#     print(i)

# for i in cars.values():
#     print(i)

# for i in cars.items():
#     print(i)

# family = {
#     "child1" : {"name" : "Kareena", "Year":2011},
#     "child2" : {"name" : "XYZ", "year":2099},
#     "child3" : {"name" : "XYZ1", "year":2079},

# }

# print(family["child1"]["name"])