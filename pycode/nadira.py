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












class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def isFull(self):
        return len(self.queue) == self.size

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if not self.isFull():
            self.queue.append(item)
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

q = Queue(3)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.isFull())
q.dequeue()
q.enqueue(40)
print(q.queue)


a) True, [20, 30, 40]
b) False, [10, 20, 30]
c) True, [10, 40, 30]
d) False, [20, 30, 40]