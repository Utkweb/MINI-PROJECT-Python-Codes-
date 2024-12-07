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

# num = [77,5,8,3,4,96,12,48,43,51,22,79]
# even_count = 0
# odd_count = 0
# for i in num:
#     if i%2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count = odd_count + 1
#         # odd_count +=1

# print("The total even numbers in the list are : ",even_count)
# print("The total odd numbers in the list are : ",odd_count)


# # Add list items 

# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]

# # 1. append()- it adds up the element in the end of the list 

# fruits.append("orange")

# print(fruits)

# # 2. insert()- it adds the element at the desired place

# fruits.insert(4,"kiwi")

# print(fruits)

# remove list items 

# fruits = ["Apple","Banana","Pineapple","Cherries","Strawberry","Watermelon"]

# 1. remove()- 

# fruits.remove("Pineapple")
# print(fruits)

# 2. pop()-


# fruits.pop(3)
# print(fruits)

# in - 
# not in - 

# num = [5,7,9,5,6,2,8,2,1,0,6,3]

# ans = []  #empty list

# for i in num:
#     if i not in ans:
#         ans.append(i)
# print(ans)

# 2. tuple

# it is ordered and unchangeable 
# they are written in round brackets 

# num = (1,2,3,4,5,8)

# len()

# cars = ("Ferrari","Mercedez","BMW","Audi","Range rover")

# num = list(cars)

# num[1]="Toyato"

# cars = tuple(num)
# print(cars)

# 2d array

# names = [
#     [2,5,9],
#     [4,9,2],
#     [8,6,4]
# ]

# for row in names:
#     for element in row:
#         print(element,end= " ")
#     print()
    
# names = [
#     [2,5,9],
#     [4,9,2],
#     [8,6,4]
# ]

# first of all find the row index and then the column index


# num = [1,8,6,7,3,9]

# Linear queue
# class queue:

#     def __init__(self):
#         self.queue = []
    
#     def isEmpty(self):
#         return len(self.queue) == 0

#     def enqueue(self,item):
#         self.queue.append(item)
#         print(f"Enqueued :{item}")
    
#     def dequeue(self):
#         if self.isEmpty():
#             print("queue empty not able to dequeue element")
#             return None
#         item = self.queue.pop(0)
#         print(f"Dequeued : {item}")
#         return item
#     def display(self):
#         if self.isEmpty():
#             print("queue empty ")
#         else:
#             print(f"Queue Elements : {self.queue}")

# q1 = queue()
# q1.enqueue(2)
# q1.enqueue(6)
# q1.enqueue(7)
# q1.enqueue(1)

# q1.display()

# q1.dequeue()
# q1.display()



# Constructor

# class Queue:
#     def __init__(self, size):
#         self.queue = []
#         self.size = size

#     def isFull(self):
#         return len(self.queue) == self.size

#     def isEmpty(self):
#         return len(self.queue) == 0

#     def enqueue(self, item):
#         if not self.isFull():
#             self.queue.append(item)
#         else:
#             print("Queue is full")

#     def dequeue(self):
#         if not self.isEmpty():
#             return self.queue.pop(0)
#         else:
#             print("Queue is empty")

# q = Queue(3)
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print(q.isFull())
# q.dequeue()
# q.enqueue(40)
# print(q.queue)


# a) True, [20, 30, 40]
# b) False, [10, 20, 30]
# c) True, [10, 40, 30]
# d) False, [20, 30, 40]



# list  

# it allow duplicate elements , mutable, changeable

# names = ["James","David","John","Jessica","Bellard"]
# print(len(names))

# print(names[4])
# print(names[-1])

# indexing :

# 1. positive indexing - it starts from left to right from 0 to n-1
# 2. negative indexing - it starts from right tot left from -1 to -n

# slicing

# names = ["James","David","John","Jessica","Bellard"]
# print(names[::-1])


# adding the element in the list 

# 1. append() -  It adds the element at the last of the list

# cars = ["Toyato","Mercedez","Audi","Lamborghini"]
# cars.append("Honda")

# print(cars)

# 2. insert() - it adds the element at the desired location of user


# cars = ["Toyato","Mercedez","Audi","Lamborghini"]
# cars.insert(2,"Honda")

# print(cars)


# how to delete the element as well in the list 

# 1. remove()-

# cars = ["Toyato","Mercedez","Audi","Lamborghini","Honda"]
# cars.remove("Toyato")
# print(cars)


# 2. pop()-


# cars = ["Toyato","Mercedez","Audi","Lamborghini","Honda"]
# cars.pop(2)
# print(cars)


# fruits = ["Cherry","banana","Apple","Orange","blueberry"]

# for i in range(0,len(fruits)):
#     print(fruits[i])

# for i in fruits:
#     print(i)

# num = [1,4,8,9,6,3,2,7,7,8,9,2,4,4]

# odd_count = 0
# even_count = 0 

# for i in num:
#     if i%2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count +=1

# print(f"The even count is : {even_count}")
# print(f"The odd count is : {odd_count}")

# num = [1,4,8,9,6,3,2,7,7,8,9,2,4,4]

# ans = []

# for i in num:
#     if i not in ans:
#         ans.append(i)

# print(f"Unique element list : {ans}")


# names = ["Utkarsh","Nadira","Mario","Dave","Sarah","Angela"]

# vowels = "AEIOUaeiou"
# count = 0

# for i in names:
#     if i[0] in vowels:
#         count = count + 1

# print(f"The total names that are starting with the vowels are : {count}")

# In an array 

# deletion of an element is difficult 
# addition of an element is difficult

# due to contiguous memory allocation 

# Linked list 


# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_at_beginning(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete_node(self,key):
#         if self.head is None:
#             print("list is empty!")
        
#         if self.head.data == key:
#             self.head = self.head.next
#             return 
        
#         current = self.head
#         while current.next is not None:
#             if current.next.data == key:
#                 current.next = current.next.next
#                 return 
#             current= current.next
#         print("Node with data ",key,"not found")

    
#     def print_list(self):                                                 
#         current = self.head
#         while current:
#             print(current.data,end = "->")
#             current = current.next
        
#         print("None")

# l1 = LinkedList()
# l1.insert_at_beginning(5)
# l1.insert_at_beginning(15)
# l1.insert_at_beginning(25)
# l1.insert_at_beginning(35)

# l1.print_list()

# l1.delete_node(25)
# l1.print_list()


# push() - It helps you to add the element 
# pop() - IT HELPS TO REMOVE THE ELEMENT 
# PEEK() - IT HELPS YOU TO GET THE TOP ELEMENT 
# ISFULL() - TO CHECK WHETHER THE LIST IF FULL OR NOT 
# ISEMPTY() - TO CHECK WHETHER THE LIST IS EMPTY OR NOT 
 
# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def push(self,item):
#         self.stack.append(item)
#         print(f"Pushed {item} onto the stack")
    
#     def pop(self):
#         if self.is_empty():
#             print("Stack is empty cannot take out an element.(Underflow)")
#             return None 
#         item = self.stack.pop()
#         print(f"popped {item} from the stack ")
#         return item 

#     def peek(self):
#         if self.is_empty():
#             print("Stack is empty no top element")
#             return None
#         return self.stack[-1]
    
#     def display(self):
#         print(f"Stack : {self.stack}")


# s = Stack()
# s.push(5)
# s.push(15)
# s.push(25)
# s.push(35)
# s.push(45)
# s.push(55)

# s.display()


# Write a program to find the maximum number in a list


# l1 = [12,34,65,11,9,88,54]

# min = l1[0]

# for i in l1:
#     if i < min:
#         min = i

# print(f"The minimum number in the list is : {min}")

# import math

# num = int(input("Enter the number : "))

# print(math.sqrt(num))

# num = int(input("Enter the number : "))
# print(num**0.5)



# Is easy to learn and use as well
# Web application and desktop application as well
# You can make graph,drawing and game also \



# print("Hassan")

# print(9+11)

# a = 99
# b = 11

# print(a//b)

# num = 920

# print(num**2)


# A hash table is a dta structure that provides an efficient way to store and retrieve  data using keys.


# Key features of Hash Tables:

# 1. Fast lookups: Average time complexity for insertions,deletions and lookup is O(1).
# 2. collision handling: Python uses separate chaining or open addressing to handle key collisions.
# 3. Dynamic Resizing: Python's dictionary resizes itself to maintain the performnce.


# lst = [1,4,8,7,5,9,6,5,4,8,2,4,2,3,5,4,8,9,6,3,2,5,1]
# freq = {}
# for i in lst:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i]=1


# print(f"The count of each element in the list is : {freq}")



# create a dictionary

# hash_table = {}

# # adding key value pair 

# hash_table['name'] = "Nadira"
# hash_table['age'] = 18
# hash_table['city'] = "United Kingdom"

# # Access a value 

# print(hash_table['name'])

# # updating a value 

# hash_table['age']= 19

# print(hash_table)

# # deleting a value 

# del hash_table['age']

# if 'age' in hash_table:
#     print("key age exists in the hash tables")
# else:
#     print("key age doesn't exists in the hash tables")


# hash_table={}
# hash_table['job']="teacher"
# hash_table['city']="London"
# hash_table['name']="'Nadira"
# hash_table['age']="21"

# print(hash_table['job'])

# print(f"Hash Table : {hash_table}")

# del hash_table['city']

# print(f"After deletion : {hash_table}")

# if 'city' in hash_table:
#     print("The key city is in the hash table")
# else:
#     print("The key city doesnt exist in the hash table")


# SHA-256

# import hashlib

# # original message 
# message = "Welcome to the class of Python"

# # creating up a new SHA-256 hash object
# sha256_hash = hashlib.sha256()

# # Encode the data to bytes and update the hash object 
# sha256_hash.update(message.encode('utf-8'))

# # get the hexadecimal representation of the hash
# hash_value = sha256_hash.hexdigest()

# print(f"Original value : {message}")
# print(f"Hashed Value : {hash_value}")


# ASCII - it is the American Standard Code for Information Interchange

# A-Z : 65-90
# a-z:97 -122   


# adjancency List - 

# graph = {
#     'A' : ['B','C'],
#     'B' : ['A','D'],
#     'C' : ['A','D'],
#     'D' : ['B','C'],
# }

# # add an edge (A->B)

# graph['A'].append('E')
# graph['E'] = ['A']

# print(graph)

# adjacency matrix:

# vertex = 1 to vertex 3 


# graph = [
#     [0,1,1,0],
#     [1,0,0,1],
#     [1,0,0,1],
#     [0,1,1,0]
# ]


# from collections import deque

# def bfs(graph,start):
#     visited = set()
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node,end=" ")
#             visited.add(node)
#             queue.extend(graph[node])

# graph = {
#     'A':['B',"C"],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':[],
#     'F':[]
# }

# bfs(graph,'C')


# def dfs(graph,start,visited=None):
#     if visited is None:
#         visited =set() #to track visited nodes

#     print(start,end= " ") # process the node
#     visited.add(start) # mark as visited

#     for neighbor in graph[start]: # explore nighbours
#         if neighbor not in visited:
#             dfs(graph,neighbor,visited)
# graph = {
#     'A':['B',"C"],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':[],
#     'F':[]
# }

# dfs(graph,'A')


# 15,56,48,27,30

# O(1)
# num = [1,2,3,4,5]

# print(num[4])


# O(n)
# num = [1,2,3,4,5]

# for i in num:
#     print(i)


# O(n log n)


# O(n^2)


# for i in range(n):
#     for j in range(n):
#         print(i,j)

# O(2^n)

# def fibo(n):
#     if n<=1:
#         return n
#     return fibo(n-1)+fibo(n-2)

# O(2n)


# for i in range(n):
#     print(i)

# for j in range(n):
#     print(j)

# dijikstra algorithm 




# data types: 

# 1. Integer - It stores positive numbers and b=negative numbers as well.

# a = 8,b = -8,etc

# 2. Float: It stores the number with decimal point in it .

# a = .14,5.089,etc

# 3. String : It stores sentences or words .

# name = "Nadira","Welcome to the programming language"

# 4. Boolean: It stores the values in terms of True or False.

# 5. Character: It stores a single character at a time .


# decimal = 8
# binary = 1000

# decimal = 6
# binary = 0110