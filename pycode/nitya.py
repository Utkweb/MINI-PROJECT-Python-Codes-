# a=3

# b=6
# print(b%a)


# (2<a)  (a<8)

# Type casting 

# a = (3)
# print(a)  


# a=int(input("Enter the number : "))
# if(90<a<100):
#     print("A+")
# elif(80<a<90):
#     print("B")
# elif(70<a<80):
#     print("c")
# elif(60<a<70):
#     print("D")
# elif(50<a<60):
#     print("E")
# else:
#     print("Apoorv pass hogya !")


# radius = float(input("Enter the radius of the sphere : "))
# vol = (4/3)*3.14*(radius**3)
# print(vol)


# import math

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# c = int(input("Enter the number : "))
# x=b*b-4*a*c
# z=x**0.5
# y=(-b+z)/(2*a )                       
# n=(-b-z)/(2*a)
# print("the y roots of given eq. is",y)
# print("the n roots of given eq. is",n)

# count=0
# for i in range(1,11):
#     count=count+i
# print(count)


# sum_even=0

# for i in range(15,21,2):
#     print("Cube of ",i,"is :",i**3)


# num=int(    input("Enter the number : "))
# for i in range(11,1,-1):
#     print(i)


# wh
#1ile loop :

# count=0
# n=int(input("Enter the number : ")) 
# if n==1:
#     print("Number is not prime!")
# else:
#     for i in range(2,n+1):
#         if n%i==0:
#             count=count+1
#     if count==1:
#         print("Number is prime!")
#     else:
#         print("Number is not prime!")
            
            
# dict={
#     "book":"It ends with us",
#     "author":"helen",
#     "price":250
# }

# new_list=["brownie","choco chip","latte","capuccino"]
# new_list[1]="donut"
# print(new_list)

# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#     print(i)
    
# for i in range(1,11):
#     print(i)


# a=4
# b=5
# cnt=0
# while a>0:
#     cnt=cnt+b
#     a=a-1
# print(cnt)


# one_day=24*60*60
# ans=0
# for i in range(1,366):
#     ans=ans+one_day
# print(ans)

# num1=int(input("Enter the number : "))
# num2=int(input("Enter the number : "))

# if(num1%num2==0):
#     print("num1 is divisible by num2")
# else:
#     print("num1 is not divisible by num2")

# dayNames = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# dayNum = int(input("Enter day number: "))
# firstDay = input("First day of year: ")

# if dayNum < 2 or dayNum > 365:
#     print("Invalid Input")
# else:
#     startDayIdx = dayNames.index(str.upper(firstDay))
#     currDayIdx = dayNum % 7 + startDayIdx - 1

#     if currDayIdx >= 7:
#         currDayIdx = currDayIdx - 7

#     print("Day on day number", dayNum, ":", dayNames[currDayIdx])


# t1=input("Enter first time : ")
# t2=input("Enter second time : ")

# fmins=int(t1[:2])*60+ int(t1[2:])
# smins=int(t2[:2])*60+ int(t2[2:])

# diff=smins-fmins

# hrs=diff//60
# mins=diff%60 

# print(hrs,"hours",mins,"minutes")

# reverse string 
# str1="Python"
# print(str1[::-1])


# str1="Programming"
# cnt=0
# for i in str1:
#     print(i,"-",end=" ")
#     if(i=='m'):
#         cnt+=1
# print(cnt)

# + concatenation of two strings
# * replication of string


# fname="Nitya"
# lname="diva"

# print(fname*2)
# print(lname*3)

# print(chr(78))


# List :
    
# title = list(input("Enter the list : ")) 
# print("Entered List :",title) 

# l=['p','y','t','h','o','n']
# print(l*10)


# str1="Programming"
# cnt=0
# for i in str1:
#     cnt+=1
# print(cnt)


# t=3,
# print(type(t))


# t1= tuple(input("enter a tuple :"))

# List:- 


# L=['a','b','c','d','e']  


# updating the list 
# L[2]='i'
# print(L)

# append function 
# L.append('f')
# print(L)

# inserting the elements with the help of insert function

# L.insert(2,'f')
# print(L)


# traverse the dictionary

# dict1={"dimple":"computer","karan":"sociology","sabah":"maths"}
# dict1['dimple']="kuch bhi"
# print(dict1)


# students=int(input("Enter the number of students : "))
# cwinners={}

# for i in range(students):
#     name=input("Enter the name of the student : ")
#     winners=int(input("Enter the number of wins : "))
#     cwinners[name]=winners

# print(cwinners)


# Bubble Sort:


# l=[16,19,11,15,10,12,14]
# n=len(l)
# for i in range(0,n):
#     flag=0
#     for j in range(0,n-i-1):
#         if(l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
#             flag=1
#     if(flag==0):
#         break
# print(l)



# Insertion Sort:

# l=[16,19,11,15,10,12,14]
# n=len(l)
# for i in range(1,n):
#     temp=l[i]   //temp = 19
#     j=i-1
#     while(j>=0 and l[j]>temp):
#         l[j+1]=l[j]
#         j=j-1
#     l[j+1]=temp

# print(l)


# def factorial(n):
#     count=1
#     for i in range(1,n+1):
#         count=count*i  
#     return count 
# n=int(input("Enter the number : "))
# print(factorial(n))


# def sinterest(p,r,t):
#     s=(p*r*t)/100
#     return s
# p=int(input("Enter the principle amount : "))
# r=int(input("Enter the rate of interest : "))
# t=int(input("Enter the time period : "))

# print(sinterest(p,r,t))
    
# number = int(input("Enter a number  :"))
# cnt=1
# for i in range(2,number+1):
#     if(number%i==0):
#         cnt=cnt+1
# if(cnt==2):
#     print("Number is prime!")
# else:
#     print("Number is not prime!")


# num = int(input("Enter a number : "))
# ans =0
# while num > 0:
#     rem = num % 10
#     ans = (ans*10)+ rem 
#     num=num//10
    
# print(ans)

# list1=[]
# for i in range(1,101):
#     if i%3==0 or i%5==0:
#         list1.append(i)
# print(list1)

# 0 1 1 2 3 5 8 13 21

# non -void function
# def converted(n):
#     A=(n*82.30)
#     return A

# # main function
# n=int(input("Enter the number of dollars : "))
# print(converted(n))

# void function
# def converted(n):
#     A=(n*82.30)
#     print(A)

# # main function
# n=int(input("Enter the number of dollars : "))
# # calling function
# converted(n)

# def one_digit_first(a):
#     return a%10        
# num1= int(input("Enter the 1st character : "))
# num2= int(input("Enter the 2nd character : "))

# ans1 = one_digit_first(num1)
# ans2 = one_digit_first(num2)

# if ans1>ans2:
#     print("The minimum number is :",num2)
# else:
#     print("The minimum number is :",num1)

# def bubble_sort(dictionary):
#     values = list(dictionary.values())
#     n = len(values)

#     # Perform bubble sort
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if values[j] > values[j + 1]:
#                 values[j], values[j + 1] = values[j + 1], values[j]

#     return values


# # Example usage
# my_dict = {'a': 5, 'b': 2, 'c': 10, 'd': 1}
# sorted_values = bubble_sort(my_dict)
# print(sorted_values)



# SQL - Structured Query Language 

# 1. Access the database
# 2. manipulate the database
# 3. Sql is a query language
# 4. Sql is a standard language 
# of the American National Standards Institute (ANSI)   


# Sql can do following things:

# 1. Create new databases
# 2. Create new tables in a database
# 3. Insert records in a database
# 4. Update records in a database
# 5. Delete records from a database
# 6. Retrieve data from a database
# # 7. Create stored procedures in a database
# 8. Create views in a database
# # 9. Set permissions on tables, procedures, and views

# RDBMS - Relational Database Management System

# It is the basis of sql and for all modern database systems such as
# MS Sql Server, IBM DB2, Oracle, MySQL, and Microsoft Access.

# the data in RDBMS is stored in database objects called tables.

# table is a collection of data entries consisting of rows and columns.




# MySql, SqlServer, Oracle, Sqlite, PostgreSql, DB2, MariaDB, Sybase, MS Access, Teradata, Informix, etc.

# Some of the most important SQL commands:
    
    
# SELECT - extracts data from a database
# UPDATE - updates data in a database
# DELETE - deletes data from a database
# INSERT INTO - inserts new data into a database
# CRAETE DATABASE - creates a new database
# ALTER DATABASE - modifies a database
# CREATE TABLE - creates a new table
# ALTER TABLE - modifies a table
# DROP TABLE - deletes a table
# CREATE INDEX - creates an index (search key)
# DROP INDEX - deletes an index

# WHERE - filters records based on specified conditions

# AND Syntax:

# SELECT column1, column2, ... 
# FROM table_name
# WHERE condition1 AND condition2 AND condition3 ...;

# OR Syntax:
    
# SELECT column1, column2, ...
# FROM table_name
# WHERE condition1 OR condition2 OR condition3 ...;

# NOT Syntax:
    
# SELECT column1, column2, ...
# FROM table_name
# WHERE NOT condition;

# data types in sql:
    
# numeric data types:
    
# 1. int: 4 bytes  -2,147,483,648 to 2,147,483,647
# 2. tinyint: 1 byte 0 to 255
# 3. smallint: 2 bytes -32,768 to 32,767
# 4. mediumint: 3 bytes -8,388,608 to 8,388,607
# 5. bigint: 8 bytes -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
# 6. float: 4 bytes -3.402823466E+38 to -1.175494351E-38, 0, and 1.175494351E-38 to 3.402823466E+38
# 7. double: 8 bytes -1.7976931348623157E+308 to -2.2250738585072014E-308, 0, and 2.2250738585072014E-308 to 1.7976931348623157E+308

# Date and Time Data Types:

# 1. DATE - format YYYY-MM-DD
# 2. DATETIME - format: YYYY-MM-DD HH:MI:SS
# 3. TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
# 4. YEAR - format YYYY or YY
# 5. TIME - format: HH:MI:SS

# String Data Types:

# 1. char(size) - Fixed-length string between 1 and 255 characters in length.
# 2. varchar(size) - Variable-length string between 1 and 255 characters in length.
# 3. TEXT or BLOB - A field with a maximum length of 65,535 characters.



# import random

# a = random.randrange(101)
# print(a)




# import random

# student1=random.randint(1,100)
# student2=random.randint(1,100)
# student3=random.randint(1,100)

# print("3 student chosen are",student1,student2,student3)

# Linear Search:-

# def linearSearch(arr, key):
#     for i in range(len(arr)):
#         if arr[i]==key:
#             return i
#     return False
# arr = list(map(int, input("Enter the array: ").split()))
# key = int(input("Enter the key to be searched: "))
# index = linearSearch(arr, key)
# print("The key is found at index: ",index)

# Magic number :
    
# def magicNumber(n):
    

# def sum_of_digits(num):
#     sum, rem = 0, 0
#     while(num!=0):
#         rem = num%10
#         sum = sum+rem
#         num=num//10
#     return sum 

# print(sum_of_digits(1234))


# def rev_num(n):
#     rem,sum=0,0
#     temp  = n
#     while n!=0:
#         rem = n%10
#         sum = sum+rem**3
#         # sum = sum*10+rem
#         n = n//10
#     if sum == temp:
#         return True
#     return False

# # main function 
# n = int(input("Enter the number: "))
# print("The armstrong of the number is: ",rev_num(n))

# a=(1,2,3,4,5,6)
# b=list(a)
# b.insert(3,8)
# a=tuple(b)
# print(a)

# a[2]


# def linear_search(arr,key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             return i
#     return 0

# #main_function
# arr=list(map(int,input("Enter the array: ").split()))
# key = int(input("Enter the key to be searched: "))
# index = linear_search(arr,key)
# print("The key is found at index: ",index)



# def binary_Search(arr,key):
#     start = 0
#     end =len(arr)-1
#     while start<=end:
#         mid = (start+end)//2
#         if arr[mid]==key:
#             return mid
#         elif key>arr[mid]:
#             start = mid+1
#         else:
#             end = mid-1
#     return False

# # main function 

# # N = int(input("Enter the size of array:"))
# print("Enter the elements of array in ascending order :")
# arr=list(map(int,input("Enter the array: ").split()))
# key = int(input("Enter the key to be searched: "))
# index = binary_Search(arr,key)
# if index:
#     print("The key is found at index: ",index)
# else:
#     print("The key is not found in the array")


# a = [10,23,56,[78,10]]
# b = list(a)
# a[3][0] +=17
# print(b)

# lst1 = "hello"
# lst2 = list((x.upper(),len(x)) for x in lst1)
# print(lst2)

# def duplicates(arr):
#     n = len(arr)
#     repeat = []
#     for i in range(n):
#         k = i+1
#         for j in range(k,n):
#             if arr[i]==arr[j] and arr[i] not in repeat:
#                 repeat.append(arr[i])
#     return repeat


# list1=list(map(int,input("Enter the array: ").split()))
# print(duplicates(list1))
                

# def freq(A, element):
#     cnt = A.count(element)
#     return cnt

# # main function 
# A = list(map(int,input("Enter the array: ").split()))
# element = int(input("Enter the element to be searched: "))
# print("The frequency of the element is: ",freq(A,element))



# def K_min(l,k):
#     l1=sorted(l)
#     return l1[k-1]
# def k_max(l,k):
#     n = len(l)
#     l1=sorted(l)
#     return l1[n-k]
# # main function
# l = list(map(int,input("Enter the array: ").split()))
# k = int(input("Enter the value of k: "))
# print("The maximum kth element is: ",k_max(l,k))
# print("The minimum kth element is: ",K_min(l,k))

# def K_min(l, k):
#     sorted_l = sorted(l)
#     return sorted_l[k - 1]

# def k_max(l, k):
#     sorted_l = sorted(l)
#     return sorted_l[-k]

# # main function
# l = list(map(int, input("Enter the array: ").split()))
# k = int(input("Enter the value of k: "))
# print("The maximum kth element is: ", k_max(l, k))
# print("The minimum kth element is: ", K_min(l, k))


# def FindPos(AR, item):
#     size = len(AR)
#     if item < AR[0]:
#         return 0
#     else:
#         pos = -1
#     for i in range(size - 1):
#         if item >= AR[i] and item < AR[i + 1]:
#             pos = i + 1
#             break  
#     if pos == -1 and i<=size -1:
#         pos = size
#     return pos
# def Shift(AR, pos):
#     AR.append(None)
#     size = len(AR)
#     print(size)
    
#     i = size - 1
#     while i >= pos:
#         AR[i] = AR[i - 1]
#         i = i - 1

# myList = [10, 20, 30, 40, 50]
# print("Before Insertion: ", myList)
# ITEM = int(input("Enter the item to be inserted: "))
# position = FindPos(myList, ITEM)
# Shift(myList, position)
# myList[position] = ITEM
# print("After Insertion: ", myList)

# # import bisect

# # mylist = [10, 20, 30, 40, 50]
# # print("Before Insertion: ", mylist)
# # item = int(input("Enter the item to be inserted: "))
# # ind = bisect.bisect(mylist, item)
# # bisect.insort(mylist, item)

# # print("The item has to be inserted at index",ind)
# # print(mylist)



# # def bi_search(arr,key,n):
# #     start=0
# #     end=n-1
# #     while start<=end:
# #         mid=(start+end)//2
# #         if key==arr[mid]:
# #             return mid
# #         elif key>arr[mid]:
# #             start=mid+1
# #         elif key<arr[mid]:
# #             end=mid-1
# #     return False

# # #main_function
# # mylist=[10,20,30,40,50]
# # n = len(mylist)
# # print("the list in sorted order is: ",mylist)
# # item=int(input("Enter the item to be searched: "))
# # posi=bi_search(mylist,item,n)

# # if posi:
# #     del mylist[posi]
# #     print("The item is deleted from the list: ",mylist) 
# # else:
# #     print("Sorry! The item is not found in the list")

# # import bisect

# # mylist = [10, 20, 30, 40, 50]
# # print("Before deletion: ", mylist)
# # item = int(input("Enter the item to be deleted: "))
# # ind = bisect.bisect(mylist, item)

# # if ind:
# #     del mylist[ind]
# #     print("The item is deleted from the list: ",mylist) 
# # else:
# #     print("Sorry! The item is not found in the list")

# # import bisect

# # mylist = [10, 20, 30, 40, 50]
# # print("Before deletion: ", mylist)
# # item = int(input("Enter the item to be deleted: "))
# # ind = bisect.bisect_left(mylist, item)

# # if ind < len(mylist) and mylist[ind] == item:
# #     del mylist[ind]
# #     print("The item is deleted from the list: ", mylist)
# # else:
# #     print("Sorry! The item is not found in the list")


# mylist = [10, 20, 30, 40, 50]
# n = len(mylist)
# for i in range(0,n):
#     print("Element",i+1,"is at index",mylist[i])


# def display(lst,r,c):
#     for i in range(r):
#         for j in range(c):
#             print(lst[i][j],end=" ")




# lst = []
# r = int(input("Enter the number of rows: "))
# c = int(input("Enter the number of columns: "))
# for i in range(r):
#     row = []
#     for j in range(c):
#         elem = int(input("Element"+str(i)+","+str(j)+":"))  
#         row.append(elem)
#     lst.append(row)
# print("List craeted is : ",lst)

# display(lst,r,c)

# print(lst[2))

# Indirect Recursion: A function calling another function and that function calling the first function is called Indirect Recursion.

# def A():
#     B()
# def B():
#     A()

# Direct Recursion: A function calling itself is called Direct Recursion.

# def A():
#     A()


# def functA():
#     print("I am in functA")
#     functA()
# def functB():
#     print   ("I am in functB")
#     functA()

# functA()

#  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
 

# first = 0
# second = 1
# nextnum = first + second   # 5

# first = second  # 2
# second = nextnum  # 3


# def fibo(n):
#     first = 0
#     second = 1
#     print(first,second,end=" ")
#     for i in range(n-2):
#         nextnum = first + second
#         print(nextnum,end=" ")
#         first = second
#         second = nextnum
# # main function
# n = int(input("Enter the number of terms: "))
# fibo(n)


# def sum(n):
#     if n ==1:
#         return 1
#     else:
#         return n +sum(n-1)

# # main function
# n = int(input("Enter the number of terms: "))
# print("The sum of first",n,"natural numbers is",sum(n))


# def is_prime(n, i=2):
#     if n <= 2:
#         return True 
#     if n % i == 0:
#         return False
#     if i * i > n:
#         return True
#     return is_prime(n, i + 1)

# n = int(input("Enter the number: "))
# if is_prime(n):
#     print("The number is prime")
# else:
#     print("The number is not prime")


# def multiply(x, y):
#     if x == 0 or y == 0:
#         return 0
    
#     if y > 0:
#         return x + multiply(x, y - 1)
#     else:
#         return -x + multiply(x, y + 1)
    
# # main function 

# x = int(input("Enter the first number: "))
# y = int(input("Enter the second number: "))
# print("The product of",x,"and",y,"is",multiply(x, y))


# def isempty(stk):
#     if stk ==[]:
#         return True
#     else:
#         return False

# def Push(stk,item):
#     stk.append(item)
#     top=len(stk)-1
    

        
 
# def Peek(stk):
#     if isempty(stk):
#         return "Underflow"
#     else:
#         top = len(stk) -1 
#         return stk[top]

# def display(stk):
#     if isempty(stk):
#         print("Stack Empty!")
#     else:
#         top = len(stk)-1
#         print(stk[top],"<-top")
#         for i in range(top-1,-1,-1):
#             print(stk[i])
            
# stack = []
# top = None
# while True :
#     print("Stack operations ")
#     print("1. Push")
#     print("2. Pop")
#     print("3. Peek")
#     print("4. Display")
#     print("5. Exit")
    
#     ch = int(input("Enter your choice (1-5)"))
#     if ch == 1:
#         item = input("Enter Item : ")
#         Push(stack,item)
#     elif ch == 2:
#         item = Pop(stack)
#         if item == "Underflow":
#             print("Empty")
#         else:
#             print("Popped item : ",str(item)*2)
#     elif ch == 3:    
#         item = Peek(stack)
#         if item == "Underflow":
#             print("Empty")
#         else:
#             print("Topmost item",item)
#     elif ch == 4:
#         display(stack)
#     elif ch == 5:
#         break
#     else:
#         print("Please make the correct choice !")
    
        
        
# print("\n"*100)


# def isHappyNumber(num):    
#     rem = sum = 0;    
        
#     #Calculates the sum of squares of digits    
#     while(num > 0):    
#         rem = num%10;    
#         sum = sum + (rem*rem);    
#         num = num//10;    
#     return sum;    
        
# num = 82;    
# result = num;    
     
# while(result != 1 and result != 4):    
#     result = isHappyNumber(result);    
     
# #Happy number always ends with 1    
# if(result == 1):    
#     print(str(num) + " is a happy number");    
# #Unhappy number ends in a cycle of repeating numbers which contain 4    
# elif(result == 4):    
#     print(str(num) + " is not a happy number");   


# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# # main function
# n = int(input("Enter the number of terms: "))
# print("The fibonacci series is: ")
# for i in range(n):
#     print(fibo(i))


# def rev(sq,n):
#     if n > 0:
#         k = len(sq)-n
#         rev(sq,n-1)
#         print(sq[k],end=" ")
#     elif n == 0:
#         return
    
# main function




# def Pop(stk):
#         item = stk.pop()
#         if len(stk) == 0:
#             top =None
#         else:
#             top = len(stk)-1
            
#             return item
# stack = ['a','b','c','d','e']
# item = Pop(stack)
# print("Popped item : ",item)



# def prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count == 2:
#         print("It is a prime number")
#     else:
#         print("It's not a prime number ")
    
# # main function2
# num = int(input("Enter a number : "))
# prime(num)


# def fibonacci(ran):
#     f1 = 0
#     f2 = 1
#     print(f1,f2,end=" ")
    
#     for i in range(0,ran-2):
#         result = f1+f2
#         print(result, end =" ")
#         f1 = f2
#         f2 = result
# # main function 

# ran = int(input("How many fibonacci no. you have to print?"))
# fibonacci(ran)

# def palin(num):
#     rev =0
#     while num!=0:
#         rem = num%10
#         rev = rev*10+rem
#         num = num//10
#     return rev

# # main function
# num = int(input("Enter a number to check whther a number is a palindrome or not  :"))

# if num == palin(num):
#     print("It is a palindrome number")
# else:
#     print("it's not a plaindrome number")


# def armstrong(num):
#     rev =0
#     while num!=0:
#         rem = num%10
#         rev = rev+rem**3
#         num = num//10
#     return rev

# # main function
# num = int(input("Enter a number to check whther a number is a palindrome or not  :"))

# if num == armstrong(num):
#     print("It is a armstrong number")
# else:
#     print("it's not a armstrong number")

# def sum_of_digits(num):
#     sum =0
#     while num!=0:
#         rem = num%10
#         sum = sum+rem
#         num = num//10
#     return sum

# # main function
# num = int(input("Enter a number to check whther a number is a palindrome or not  :"))

# print(sum_of_digits(num))


# Create database db_name;

# create database if not exists db_name;


# use db_name;

# show database;


# Python 

# data types:

# 1. numeric
# 2. string
# 3. Boolean
# 4. list
# 5. tuple
# 6. set
# 7. dictionary

# arithmeitc operator: +,-,*,/,%,//,**


# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number : "))
# sum = 0

# for i in range(1,b+1):
    
#     sum = sum+a
#     if(sum == 9):
#         continue
    
# print(sum)  

# for i in range(1, 11):
#     if i == 9:
#         continue  
#     print(i)


# for i in range(1,6):
#     for j in range(1,6):
#         print(i," | ",j)
#     print()


# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end= "\t")
#     print()

# c = 0
# for x in range(10):
#     for y in range(5):
#         c+=1
# print(c)

# word ="lamp"

# print(word[::-1])



# word = input("Enter the word : ")

# result = word[-1]+word[1:-1]+word[0]

# print(result)



# cnt,cnt1=0,0
# str1 = input("Enter the string : ")
# for i in str1:
#     if i in ('a','e','i','o','u'):
#         cnt = cnt+1
#     else:
#         cnt1 = cnt1+1

# print("The number of vowels in the string is : ",cnt)
# print("The number of consonants in the string is : ",cnt1)

# 12252019

# date = input("Enter the date in the format mmddyyyy : ")

# month = int(date[:2])
# day   = date[2:4]
# year  = date[4:]

# list1 = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# result = list1[month-1]+" "+day+", "+year

# print(result)


# ph = [1,2,3,4,5,6,7,8,9,0]

# ph.insert(3,'-')
# ph.insert(6,'-')

# for i in ph:
#     print(i,end="")


# l = [3,1,4]
# M = [1,5,9]

# for i in range(len(l)):
#     N = l[i]+M[i]
#     print(N)

# list1 = []

# a,b=0,1

# for i in range(10):
#     list1.append(a)
#     a = a+b
#     a,b = b,a
    
# print(tuple(list1))
    

# word = ["working","with","functions"]

# max_word = len(word[0])

# for i in word[1:]:
#     if len(i)>max_word:
#         max_word = i

# print(max_word)

# n = 8

# def pri():
#     n = 9
#     return n

# print(pri())



# def length(str1):
#     count = 0
    
#     for i in str1:
#         count+=1
#     return count

# #main function
# str1 = "Python"
# print(length(str1))


# def nthroot(x,n=2):
#     return 1/(x**n)

# x = int(input("Enter the value of x : "))
# print("The value of 1/x^n is : ",nthroot(x))

# def buuble_sort(arr):
    
#     n = len(arr)
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
    
#     return arr

# l1 = [64, 34, 25, 12, 22, 11, 90]
# print(buuble_sort(l1))
    
    
# def insertion_sort(arr):
#     n = len(arr)
    
#     for i in range(1,n):
#         key = arr[i]
        
#         j = i-1
        
#         if j>=0 and key<arr:
#             arr[j+1]=arr[j]
#             j = j-1
#         else:
#             arr[j+1]=key
#     return arr

# arr=

# f = open("nitya.txt",'r')

# for x in f:
#     print(x)



# f = open("nitya.txt",'r')
# print(f.readlines())

# # f.write("Nitya aaj aayi hai !!")

# f.close()

# # f = open("nitya.txt",'r')

# # for x in f:
# #     print(x)

# import os 

# os.remove("nitya.txt")

# import os
# if os.path.exists("nitya.txt"):
#   os.remove("nitya.txt")
# else:
#   print("The file does not exist")


# def print(n):
#     print()


# def sum(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n*sum(n-1)
    
# n = int(input("Enter the number : "))

# print("The factorial of first",n,"natural numbers is : ",sum(n))


# arr = [10, 15, 19, 28, 57]
# key = int(input("Enter a number: "))
# found = False  # Variable to keep track of whether the key is found

# for i in range(len(arr)):
#     if arr[i] == key:
#         print("Found")
#         found = True
#         break  # Exit the loop once the key is found

# if not found:
#     print("Not found")


# lst = [i*2 for i in range(1,6)]

# print(lst)


# lst = []
# for i in range(1,6):
#     lst.append(i)
    
# print(lst)


# import bisect

# lst =[10,20,30,40,50,60,70]

# item = int(input("Enter a number  : "))

# ind = bisect.bisect(lst,item)
# bisect.insort(lst,item)



# print(ind)
# print(lst)

# lst = [[1,2],[9,8],[3,4]]

# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end = " ")
#     print()