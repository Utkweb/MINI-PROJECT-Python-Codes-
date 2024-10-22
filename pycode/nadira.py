# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")
# print("Nadira")


# for i in range(1,11):
#     print("Nadira")


# created a function
# def add(a,b):
#     print(a+b)
#     add(2,6)

# calling function 



# recursion - calling the function itself


# 1 2 3 4 5 6 7 8 9 10 
# sum = 0
# for i in range(1,11):
#     sum += i

# print(sum)

# operator and operand

# loops

# for loop

# for variable_name in range(start,end,steps):
#     statements

# for i in range(1,11):
#     print(i)


# 10 9 8 7 6 5 4 3 2 1


# for i in range(10,0,-1):
#     print(i)


# while condition:
#     statements

# i = 1
# while i <= 10:
#     print(i)
#     i = i+1

# 1 2 3 4 5 67 8 9 10

# piggy_bank = 0
# for i in range(1,11):
#     piggy_bank = piggy_bank + i
# print(piggy_bank)


# List: it can store multiple items.

# It allows store duplicate values
# The list is enclosed by [] brackets 
# These are mutable 

# initialize the list 

# num = [3,5,8,3,5,6,3,2,1,4,5]
# names = ["Nadira","James","David","Debjit"]
# num1 = [10.5,84.25]

# person1 = ["Nadira",16,46.6,True]


# cars = ["Mercedez,","Audi","Toyato","Honda"]

# print(cars[-1])

# indexing
# 1. positive indexing - it starts from left to right and 0 to n-1.
# 2. negative indexing -  it starts from right to left -1 to -n

# Slicing 

# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]
# print(fruits[0:4:2])

# fruits[start_index:end_index:steps]

# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]
# fruits[2] = "Orange"

# print(fruits)

# How to check the length of the list

# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]
# print(len(fruits))


# loops with list

# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]
# for i in range(0,len(fruits)-1):
#     print(fruits[i])

# Just print 

# 1. Apple
# 2. banana



# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]
# for i in fruits:
#     print(i)



# name = "Nadira"
# age = 16

# print(name," : ",age)


# Nadira : 16 

num = [77,5,8,3,4,96,12,48,43,51,22,79]
even_count = 0
odd_count = 0
for i in num:
    if i%2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
        # odd_count +=1

print("The total even numbers in the list are : ",even_count)
print("The total odd numbers in the list are : ",odd_count)

