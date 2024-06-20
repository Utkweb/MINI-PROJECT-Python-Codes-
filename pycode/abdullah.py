# loops:-  The same thing is ging to repeat so on and on.

# 1. for loop -> It is used to repeat the same thing again and again.
# 2 while loop -> It is used to repeat the same thing again and again until the condition is true.

# print("Abdullah")
# print("Abdullah")
# print("Abdullah")
# print("Abdullah")
# print("Abdullah")
# print("Abdullah")
# print("Abdullah")
# print("Abdullah")
# print("Abdullah")

# syntax:

# for variable_name in range(start,stop,step):
#     statements

# printing your name ten times

# for i in range(5,51,5):
#     print(i,end=" ")
    
# 0 2 4 6 8 10 12 14 16 18 20
# 5 10 15 20 25 30 35 40 45 50

# print("Abdullah")
# print("Utkarsh")


# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

# 1 2 3 4 5 6 7 8 9 10 = 55

# money_bank = 0

# for i in range(1,11):
#     money_bank = money_bank+i
# print("Money in bank: ",money_bank)


# 1 - 50

# even number count = 25
# odd number count = 25


# even_count = 0
# odd_count = 0
# for i in range(1,51):
#     if i%2 ==0:
#         even_count = even_count+1
#     else:
#         odd_count = odd_count+1

# print("Even number count: ",even_count)
# print("Odd number count: ",odd_count)
    
# Write a Python program to print the multiplication table of a given number.



# HomeWork (3/4/2024):-

# 1. Write a Python program to print the multiplication table of a given number.   Done 
# 2. Write a Python program to find the sum of first 10 natural numbers.
# 3. Write a Python program to find the sum of first 50 natural numbers.
# 4. Write a python program to find the count of even and odd numbers from 1 to 100.
# 5. Write a python program to find the factorial of a given number.



# 1 - 10

# for i in range(1,11,2):
#     print(i)



# 20 - 51
# for i in range(20,52):
#     print(i)


# 5 10 15 20 25 30 35 40 45 50
# for a in range(5,51,5):
#     print(a)
    
# 10 9 8 7
# for x in range(10,0,-1):
#     print(x,end=" ")



# name = "Abdullah"
# age = 20

# print("My name is",name,"and my age is",age)

# output- My name is Abdullah and my age is 20.



# 8 X 1 = 8
# 8 X 2 = 16
# 8 X 3 = 24
# 8 X 4 = 32
# 8 X 5 = 40
# 8 X 6 = 48

# 8 X 10 = 80

# num = int(input("Enter the number of which you want the table of :"))

# for x in range(1,11):
#     print(num,"X",x,"=",num*x)

# 2. Write a Python program to find the sum of first 10 natural numbers.

# piggy_bank = 0

# for i in range(0,10):
#     piggy_bank = piggy_bank+i
    
# print("Total money in piggy bank: ",piggy_bank)


# 3. Write a Python program to find the sum of first 50 natural numbers.
# bank=0
# for x in range(0,51):
#     bank=bank+x
    
# print("Total money in bank=",bank)

# 4. Write a python program to find the count of even and odd numbers from 1 to 100.

# num = 4

# if num%2==0:
#     print("Even Number")
# else:
#     print("odd numbers"

# even_count = 0
# odd_count = 0

# for x in range(1,101):
#     if x%2==0:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1
# print("Even numbers count: ",even_count)
# print("Odd numbers count: ",odd_count)


# 5. Write a python program to find the factorial of a given number.

# 5 = 5*4*3*2*1 = 120


# num = int(input("Enter the number of whohc you want the factorial of : "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
    
    
# print("Factorial of",num,"is",fact)


# syntax:
    
    
# while condition:
#     statements

# i = 10

# while i>=1:
#     print(i,end= " ")
#     i= i -1
    
    
# 10 1


# Python Strings - Strings are sentences, name, etc.
# and they are enclosed by inverted commas

# name = "Abdullah"
# print(name)


# how we can take the input of string?

# name = str(input("Enter the name of the person  : "))
# print(name)


# multi lines strings

# sentence = '''1.
# 2.
# 3.
# 4.

# '''

# sentence = "He is called 'Johnny"

# print(sentence[-3])

# slicing :- it divides the sentence or the string in two slides according to the user.

# name = "Abdullah"

# print(name[0:4])


# b = "Hello, World!"
# print(b[5:9])

# Modifying String 

# name = "ABDULLAH"
# print(name.lower())


# sentence = "   hello my name is Utkarsh Singh   "
# print(sentence.strip())

# replace a string

# a = "Hello World!"
# print(a.replace("H","J"))


# Sure! Here are some easy coding questions related to string manipulation without directly using the predefined functions `lower`, `upper`, `replace`, and `strip`. You can solve these problems using basic string operations and loops.

# ### 1. Convert a String to Lowercase
# Write a function that converts all uppercase letters in a given string to lowercase without using the `lower()` function.

# **Example:**
# ```python
# Input: "Hello World"
# Output: "hello world"
# ```

# ### 2. Convert a String to Uppercase
# Write a function that converts all lowercase letters in a given string to uppercase without using the `upper()` function.

# **Example:**
# ```python
# Input: "Hello World"
# Output: "HELLO WORLD"
# ```

# ### 3. Replace All Occurrences of a Substring
# Write a function that replaces all occurrences of a given substring in a string with another substring without using the `replace()` function.

# **Example:**
# ```python
# Input: ("Hello World", "World", "Universe")
# Output: "Hello Universe"
# ```

# ### 4. Strip Leading and Trailing Whitespace
# Write a function that removes leading and trailing whitespace from a string without using the `strip()` function.

# **Example:**
# ```python
# Input: "   Hello World   "
# Output: "Hello World"
# ```

# ### Sample Solutions

# Here are some sample solutions for these problems:

# #### 1. Convert a String to Lowercase
# ```python
# def to_lowercase(s):
#     result = ''
#     for char in s:
#         if 'A' <= char <= 'Z':
#             result += chr(ord(char) + 32)
#         else:
#             result += char
#     return result

# # Test
# print(to_lowercase("Hello World"))  # Output: "hello world"
# ```

# #### 2. Convert a String to Uppercase
# ```python
# def to_uppercase(s):
#     result = ''
#     for char in s:
#         if 'a' <= char <= 'z':
#             result += chr(ord(char) - 32)
#         else:
#             result += char
#     return result

# # Test
# print(to_uppercase("Hello World"))  # Output: "HELLO WORLD"
# ```

# #### 3. Replace All Occurrences of a Substring
# ```python
# def replace_substring(s, old, new):
#     result = ''
#     i = 0
#     while i < len(s):
#         if s[i:i+len(old)] == old:
#             result += new
#             i += len(old)
#         else:
#             result += s[i]
#             i += 1
#     return result

# # Test
# print(replace_substring("Hello World", "World", "Universe"))  # Output: "Hello Universe"
# ```

# #### 4. Strip Leading and Trailing Whitespace
# ```python
# def strip_whitespace(s):
#     start = 0
#     end = len(s) - 1
    
#     while start <= end and s[start] == ' ':
#         start += 1
#     while end >= start and s[end] == ' ':
#         end -= 1
        
#     return s[start:end+1]

# # Test
# print(strip_whitespace("   Hello World   "))  # Output: "Hello World"
# ```

# Feel free to try these out and modify them as needed!



# concatenation 

# s1="hey"
# s2="buddy"

# print(s1+s2)

# replication 

s2="buddy"
print(s2*4)
