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


# Buble Sort:

l=[16,19,11,15,10,12,14]
n=len(l)
for i in l:
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            
print(l)