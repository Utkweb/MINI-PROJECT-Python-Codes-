# Functions :-

# def name_of_the_function():
#     #statements


# initializing a function
# def add(a,b):   # a,b are parameters
#     print(a+b)

# # calling a function

# # main function
# add(7,8)   # 7,8 are arguments


# defining the function 

# def swap(a,b):
#     a = a+b
#     b=a-b
#     a=a-b
#     print(a,b)

# calling a function
# swap(4,5)


# def add_sum():
#     sum = 0
#     for i in range(1,11):
#         sum = sum+i
#     print(sum)

# # main-function 
# add_sum()
        

# def check(a,b,c):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")


# # calling function
# n = int(input("enter a number: "))
# check()
    

# Average of three numbers using functions in python


# Print the series 1 to n using functions in python

# def print_series(n):
#     for i in range(1,n+1):
    

# Modules : 

# import moduletest

# moduletest.greet("Ayra")

# 1 2 3 4 5 6 7 8 9 10
# if i %2 ==0:
#     sum+=i

def even_sum(n):
    sum = 0
    for i in range(1,n+1):
        if i %2 ==0:
            sum+=i
    print(sum)

# main function
n = int(input("enter a number till where you want the sum of even numbers : ")) 
even_sum(n)