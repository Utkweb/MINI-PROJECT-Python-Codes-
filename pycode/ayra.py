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

# def even_sum(n):
#     sum = 0
#     for i in range(1,n+1):
#         if i %2 ==0:
#             sum+=i
#     print(sum)

# # main function
# n = int(input("enter a number till where you want the sum of even numbers : ")) 
# even_sum(n)


# list, tuple, set, dictionary

# 1. list - mutable, ordered, duplicates allowed []

# list1 = [1, 2,3 ,4, 5, 6, 7, 8, 9, 10]

# print(list1[2:7])

# list1 = [1,2.5, "Ayra", True, 54,88]
# list1.append("Humza")
# print(list1)

# list1 = [1,4,9]

# add

# 8
# 7
# 6
# 5

# append() - adds an element at the end of the list

# insert()- adds an element at a specific index


# list1 = [4,9,5,8,7,3]
# list1.insert(2,8)

# print(list1)

# remove() - removes the specified element
# pop() - removes the specified index

# del () - deletes the list

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(2)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#     print(i)
# print(len())

# sorting - ascending, descending

# 1 5 4 9 8 7 6 3 2

# thislist = [1,5,4,9,8,7,6,3,2]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

# if "apple" in thislist:
#     print("True")
# else:
#     print("False")

# updating a list

# list1 = ["apple", "banana", "cherry"]

# for x in list1:
#     print(x)

# join a list

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# list3 = list1+list2

# print(list3)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# print(fruits[4])

# Tuple

# it is immutable, ordered, duplicates allowed
# tuple are writtend in ()

# tuple1 = (1,2,3,4,5,6,7,8,9,10)

# tuple1=("apple",)
# print(type(tuple1))

# tuple1 = (1,2,3,4,5,6,7,8,9,10)

# print(tuple1[3:7])

# updating a tuple

# x = ("apple", "banana", "cherry")


# y = list(x)

# y[1] = "kiwi"

# x = tuple(y)
# print(x)


# find the length of the tuple
# x = ("mango", "banana", "cherry")
# print(len(x))

# x = ("apple", "banana", "cherry")
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# tuple2 = (True, False, False)



# tuple1  = ("apple", "banana", "cherry")

# y = list(tuple1)
# y.remove("banana")

# tuple1 = tuple(y)

# print(tuple1)

# 341 -->  143

# num = int(input("enter a number: "))   341
# sum = 0

# while num!=0:
#     rem = num%10          
#     sum = sum*10 + rem    
#     num = num//10        
    
# print(sum)


# 155 = 1+5+5 =11


# num = int(input("enter a number: "))
# sum = 0
# while(num!=0):
#     rem = num%10   #rem =1%10 = 1
#     sum = sum+(rem**3)    #sum = 0+27 = 27 +125 =152+1 = 153
#     num = num//10      #num =15

# if (sum == num):
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# 153%10 = 3

# 153//10 = 15

# 15//10=1

# 153 = 1^3+5^3+3^3 = 1 + 125 + 27 = 153

# 121 = 1^3+2^3+1^3 = 1+8+1 = 10

# 0,1,153,370,371,407


# tuples : it is immutable



# tuple1 = (1,2,"Ayra",True, 5.5, 1,2,3,4,5,6,7,8,9,10)
# print(len(tuple1))


# factorial program 

# num = int(input("enter a number: "))    #num =7
# result = 1

# for i in range(1,num+1):
#     result = result * i
# print(result)

# num = 6

# 6*5*4*3*2*1 = 720

# Prime Number

# 5 - 1,5
# 11 - 1,11


# num = int(input("enter a number: "))    #num =11
# count = 0
# for i in range(1,num+1):
#     if num%i ==0:
#         count= count+1
        
# if count ==2:
#     print("Prime number")
# else:
#     print("Not a prime number")
    


# 1,2,3,4,5,6,7,8,9,10,11


# sum = 0

# for i in range(1,21):
#     if i%2==0:
#         sum=sum+i
# print(sum)

    
# num = int(input("enter a number: "))
# for i in range(1,11):
#     print(num*i)


# set 


# a =[1,2,3,4,5,6,7,8,9,10]

# target = 6


# a = [14,15,18,19,50,44]

# for i in range(0,len(a)):
#     if a[i] == 50:
#         print("Our value is at : ",i)
#         break


# a = [14,15,18,19,50,44,18,19,78,56,22,34,100]


# a[0],a[len(a)-1]=a[len(a)-1],a[0]

# print(a)





# 10 11 12 13 14 15 16 17 18 19 20


# x = 16



# import random

# lower_limit = int(input("Enter the lower limit: "))

# upper_limit = int(input("Enter the upper limit: "))

# x = random.randint(lower_limit,upper_limit)

# print("You've only 8 chances to guess the number")

# count = 0

# while count<8:
#     count= count+1
#     guess = int(input("Guess the number :"))
    
#     if x == guess:
#         print("Congratulations you did it in ",count," try")
#         break
#     elif x>guess:
#         print("You guessed too small")
#     elif x<guess:
#         print("You guessed too high")

# if count>=8:
#     print("Game Over !")


# OOPS - Object Oriented Programming

# class myclass:
#     no_of_students = 9
#     standard = 6
#     board_colours = "black and white"

# p1 = myclass()
# print(p1.no_of_students)
# print(p1.standard)
# print(p1.board_colours)


# __init__() - constructor

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# p1 = Person("Ayra", 20)
# p2 = Person("Humza", 18)
# print(p1.name)
# print(p1.age)

# print(p2.name)
# print(p2.age)


# if 

# if else

# if elif else

# syntax og if elif else

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# else:
#     statement


# choice = int(input('''
                   
#                    1. Addition
#                      2. Subtraction
#                         3. Multiplication
#                             4. Division
#                             5. Exit
                            
#                             Enter your choice : '''))
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# if choice == 1:
#     print(a)
# elif choice == 2:
#     print(a-b)
# elif choice == 3:
#     print(a*b)
# elif choice == 4:
#     print(a//b)
# else:
#     print("Invalid Choice")



# rotate an array

# no. of rotations = 3

# input :
# 1 2 3 4 5
# no. of rotations = 3

# output:
# 3 4 5 1 2


# array = [1,2,3,4,5]
# no_of_rotations = 3

# n = len(array) //5
# no_of_rotations = no_of_rotations % n
# rotate_array = array[-no_of_rotations:]+array[:-no_of_rotations]

# print(rotate_array)


# print(3%5)


# 12321 = 12321

# palindrome

# num = int(input("enter a number: "))   #num = 12321
# sum = 0
# temp = num
# while num!=0:
#     rem = num%10
#     sum = sum*10 + rem
#     num = num//10
# if temp == sum:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


# fibonacci series

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# num = int(input("enter a number: "))   #num = 10
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(2,num):
#     c = a+b
#     print(c)
    
#     a = b
#     b = c

# num = int(input("enter first number: "))
# num1 = int(input("enter second number: "))
# num2 = int(input("enter third number: "))

# if(a>b and a>c):
#     print("a is the largest number")
# elif(b>a and b>c):
#     print("b is the largest number")
# else:
#     print("c is the largest number")


# remove duplicates from a list

# list1 = [1, 2, 3, 4, 2, 3, 5]
# list2 = [1,2,3,4]

# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)


# [4,9,8,7,5,6]

# grading system

# student_score = int(input("enter the score of the student: "))
# if student_score>=95:
#     print("A+")
# elif student_score>=90:
#     print("A")
# elif student_score>=80:
#     print("B")
# elif student_score>=70:
#     print("C")
# elif student_score>=60:
#     print("D")
# else:
#     print("F")


# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# start = int(input("enter the start number: "))
# end = int(input("enter the end number: "))

# sum = 0

# for i in range(start,end+1):
#     if prime(i):
#         sum = sum+i
        
# print("Sum of prime numbers:",sum)
        
    


# tkinter -> it is a standard python interface to the Tk GUI toolkit. 
# It allows developers to create graphical user interfaces

# import tkinter as tk

# root = tk.Tk()

# b1 = tk.Button(root,text="click me",fg="blue")
# b1.pack()

# root.mainloop()




# len(name_of)


# from tkinter import *

# expression =""


# def press(num):
#     global expression
    
#     expression = expression + str(num)
#     equation.set(expression)
    
# def equalpress():
#     try:
#         global expression
#         total = str(eval(expression))
#         equation.set(total)
#         expression = ""
#     except:
#         equation.set("error")
#         expression = ""

        
# def clear():
#     global expression
#     expression=""
#     equation.set("")
    
# if __name__ =="__main__":
#     gui = Tk()
    
#     gui.title("Simple Calculator")
#     gui.geometry("270x150")
#     equation = StringVar()
    
#     # 6+4
#     expression_field = Entry(gui,textvariable = equation)
    
#     expression_field.grid(columnspan = 4,ipadx = 70)
    
#     b1 = Button(gui,text='1',fg = 'white',bg='green',command= lambda: press(1),height=1,width=7)
#     b1.grid(row=2,column=0)
#     b2 = Button(gui,text='2',fg = 'white',bg='green',command= lambda: press(2),height=1,width=7)
#     b2.grid(row=2,column=1)
#     b3 = Button(gui,text='3',fg = 'white',bg='green',command= lambda: press(3),height=1,width=7)
#     b3.grid(row=2,column=2)
#     b4 = Button(gui,text='4',fg = 'white',bg='green',command= lambda: press(4),height=1,width=7)
#     b4.grid(row=3,column=0)
#     b5 = Button(gui,text='5',fg = 'white',bg='green',command= lambda: press(5),height=1,width=7)
#     b5.grid(row=3,column=1)
#     b6 = Button(gui,text='6',fg = 'white',bg='green',command= lambda: press(6),height=1,width=7)
#     b6.grid(row=3,column=2)
#     b7 = Button(gui,text='7',fg = 'white',bg='green',command= lambda: press(7),height=1,width=7)
#     b7.grid(row=4,column=0)
#     b8 = Button(gui,text='8',fg = 'white',bg='green',command= lambda: press(8),height=1,width=7)
#     b8.grid(row=4,column=1)
#     b9 = Button(gui,text='9',fg = 'white',bg='green',command= lambda: press(9),height=1,width=7)
#     b9.grid(row=4,column=2)
#     b0 = Button(gui,text='0',fg = 'white',bg='green',command= lambda: press(0),height=1,width=7)
#     b0.grid(row=5,column=0)
    
#     plus = Button(gui,text='+',fg = 'white',bg='green',command= lambda: press('+'),height=1,width=7)
#     plus.grid(row=2,column=3)
    
#     minus = Button(gui,text='-',fg = 'white',bg='green',command= lambda: press('-'),height=1,width=7)
#     minus.grid(row=3,column=3)
    
#     multiply = Button(gui,text='*',fg = 'white',bg='green',command= lambda: press('*'),height=1,width=7)
#     multiply.grid(row=4,column=3)
    
#     divide = Button(gui,text='/',fg = 'white',bg='green',command= lambda: press('/'),height=1,width=7)
#     divide.grid(row=5,column=3)
    
#     equal = Button(gui,text='=',fg = 'white',bg='green',command=equalpress,height=1,width=7)
#     equal.grid(row=5,column=2)
    
#     clear = Button(gui,text='C',fg = 'white',bg='green',command= clear,height=1,width=7)
#     clear.grid(row=5,column=1)
    
#     decimal = Button(gui,text='.',fg = 'white',bg='green',command= lambda: press('.'),height=1,width=7)
#     decimal.grid(row=6,column=0)
    
    
    
    
#     gui.mainloop()
    
    
    
# lambda : it is a keyword in python which is used to make an anonymous function

# x = lambda a:a+10

# x(5)



# import tkinter as tk 

# def ctof():
#     try:
#         celsius = float(e1.get())
#         fahrenheit = (celsius*9/5)+32
#         result.config(text=f"Answer : {fahrenheit} °F")
#     except ValueError:
#         result.config(text="Enter a valid number")
    
# def ftoc():
#     try:
#         fahrenheit = float(e1.get())
#         celsius = (fahrenheit-32)*5/9
#         result.config(text=f"Answer : {celsius} °C")
#     except ValueError:
#         result.config(text="Enter a valid number")
        


# root = tk.Tk()
# root.title("Temperature Convertor")

# l1 = tk.Label(root,text="Temperature Conversion App")
# l1.grid(row=0,columnspan = 3,padx=20,pady =20)

# #input field
# e1 = tk.Entry(root,width = 20)
# e1.grid(row=1,column =0,padx=20,pady=20)

# b1 = tk.Button(root,text = "Convert to Fahrenheit",fg = "white",bg="green",command=ctof)
# b1.grid(row=1,column=1,padx=20,pady=20)

# b2 = tk.Button(root,text="Convert to Celsius",fg="white",bg="green",command=ftoc)
# b2.grid(row=1,column =2,padx=20,pady=20)


# result_frame = tk.Frame(root, bd=4, relief=tk.GROOVE)
# result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# # display our result
# result = tk.Label(result_frame,text="",borderwidth=20,font=("Comic Sans MS", 20,"bold"))
# result.grid(padx=20,pady=20)






# root.mainloop()


# import tkinter
# import random 

# timeleft = 30
# points = 0
# colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
# current_color_index = 0
# def startgame(event = None):
#     if timeleft == 30:
#         countdown()

# def nextColor():
#     global timeleft
#     global points
#     global current_color_index
#     if timeleft>0:
#         e.focus_set()
#         if e.get().lower() == colors[current_color_index].lower():
#             points = points + 1
#             feedback.config(text="Correct!",fg='green')
        
    
# def countdown():
#     global timeleft
#     if timeleft>0:
#         timeleft = timeleft-1
#         time.config(text= "Time left : "+str(timeleft))
#         time.after(1000,countdown)
#     else:
#         label.config(text="Time's Up!!!!!",font=('Georgia',40))
#         feedback.config(text="Final Score : "+str(points),font=('Georgia',20))
    
    

# # create a gui window
# root = tkinter.Tk()

# root.title("Color Game")
# root.geometry('375x200')

# l1 = tkinter.Label(root,text="Type the color of the words not the word text!",font=('Georgia',20))
# l1.pack()

# score = tkinter.Label(root,text="Press enter to start",font=('Georgia',20))
# score.pack()

# time = tkinter.Label(root,text="Time left : " +str(timeleft),font=('Arial',15),fg='red',bg='yellow')
# time.pack()

# label = tkinter.Label(root)
# label.pack()

# feedback = tkinter.Label(root,text="",fg= "black")
# feedback.pack()

# e = tkinter.Entry(root)
# e.pack()

# e.bind('<Return>',startgame)
# e.focus_set()
# root.mainloop()


# data types:

# 1. int
# 2. float
# 3. str
# 4. bool
5 # 5. list
# 6. tuple
# 7. set
# 8. dictionary

# list: it is a collection of items. It is mutable, ordered, duplicates allowed

# Some list examples:

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = [1,2.5,"Ayra",True,54,88]
# list3 = [1,4,9]

# cars = ["Ford", "Volvo", "BMW", "Audi", "Mercedes", "Toyota", "Honda", "Hyundai", "Kia", "Maruti"]
 
# cars[-1]= "Acura"
# print(cars)

# concatenation

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

# print(list1+list2)

# replication

# name = "Ayra "
# print(name*10)

# adding up the element in the list:

# 1. append() - adds an element at the end of the list


# 2. insert() - adds an element at a specific index


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits.append("Orange")
# fruits.insert(2,"Orange")

# print(fruits)


# names = ["Ayra","Humza","Anvi","Nidhi","Riya"]

# you need to count the number of names starting with a vowel


# List : Collections of item 

# 1. Mutable  - we can change ,modify, update the elements
# 2. Ordered - it maintains the order of the elements
# 3. Duplicates allowed - it allows the duplicates
# 4. It is represented in []

# example of list :

# list1 = [1,2,3,4,5,6,7,8,9,10] (we can store integers)
# list2 = [1,2.5,"Ayra",True,54,88] (we can store different data types)
# list3 = ["apple", "banana", "cherry", "kiwi", "mango"] (we can store strings)


# l1 = ["apple", "banana", "cherry", "kiwi", "mango"]
# print(l1)

# if i wanna access the element in the list 

# l1 = ["apple", "banana", "cherry", "kiwi", "mango"]
# print(l1[-1])

# slicing - breaking the list into pieces

# l1 = ["apple", "banana", "cherry", "kiwi", "mango"]
# print(l1[::-1])  # reverse the list


# s1 = "Humza"
# print(s1[::-1])  # reverse the string

# append() - it adds an element at the end of the list
# adds an element at the particular 

# l1 = ["apple", "banana", "cherry", "kiwi", "mango"]
# # l1.append("raspberry")
# l1.insert(3,"raspberry")

# print(l1)

# remove() - removes the specified element
# pop() - removes the specified index

# l1 = ["apple", "banana", "cherry", "kiwi", "mango"]
# l1.remove("apple")
# l1.pop()

# print(l1)

# del - deletes the list

# l1 = ["apple", "banana", "cherry", "kiwi", "mango"]
# del l1

# print(l1)

# will access the elements of the list using for loop

# cars = ["Ford", "Volvo", "BMW", "Audi", "Mercedes", "Toyota"]

# for i in range(0,len(cars)):
#     print(i+1,".",cars[i])

# apps = ["Facebook", "Instagram", "Whatsapp", "Snapchat", "Linkedin", "Telegram", "Pinterest"]

# for i in apps:
#     print(i)

# Tuples : It is a collection of items. That ae immutable,ordered, allow duplicate values
# 
# It is represented by ().

# t1 = ("apple", "banana", "cherry", "kiwi", "mango")


# # type casting
# l1 = list(t1)
# l1[2] = "orange"
# t1 = tuple(l1)
# print(l1)

# t1 = ("apple", "banana", "cherry", "kiwi", "mango")
# print("banana" not in t1)


# Memebership operators : in, not in

# joining tuples

# t1 = (1,2,3,4,5)
# t2 = ('a','b','c','d','e')

# print(t1+t2)

# replication

# t1 = (1,2,3,4,5)
# print(t1*2)

# t1 = (78,89,57,29,96,55)

# we need to find largest element in the tuple
# we need to find smallest element in the tuple
# we need to swap the first and last element in the tuple

# t = (78,89,57,29,96,55)

# t1 = list(t)

# temp = t1[0]
# t1[0] = t1[-1]
# t1[-1] = temp

# print(t1)


# social_apps = ["FacebooF", "InstI", "W", "Snapchat", "Linkedin", "TelegraT", "P"]
# ans = []

# for x in social_apps:
#     if len(x) >= 2 and x[0] == x[-1]:
#         ans.append(x)

# print(ans)


# Sets: It is a collection of items. It is unordered, unindexed, no duplicates allowed
# -> It is represented by {}


# s1 = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'apple', 'banana', 'cherry', 'kiwi', 'mango']
# print(set(s1))

# how you can access the elements if the it doens't allow to do so with index - loops

# s1 = {'apple', 'cherry', 'kiwi', 'mango'}

# adding a item 

# s1 = {'apple', 'cherry', 'kiwi', 'mango'}
# s1.add("banana")

# print(s1)



# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)


# for removing item from the set = remove(), discard(), pop(), clear(), del()


# Join sets - union(), update(), intersection_update(), symmetric_difference_update(), difference_update()


# dictionaries - it is a collection of items. It is unordered, mutable, indexed, no duplicates allowed

# -> It is represented by {}

# d1 = {
#     'name' : 'Ayra',
#     'age' : 20,
#     'city' : 'Delhi',
#     'country' : 'India',
#     'country' : 'USA'
# }

# print(d1['name'])


# key -> It is the name of the item
# value -> It is the value of the item

# Coding Problems related to dictionaries

# 1. Write a Python program to sum all the items in a dictionary.

# d1 = {
#     'a' : 100,
#     'b' : 200,
#     'c' : 300,
#     'd' : 400
# }

# sum = 0

# for i in d1.values():
#     sum = sum+i

# print(f'Sum of all the items in the dictionary is : {sum}')

# 2. Write a Python program to multiply all the items in a dictionary.

# 3. Write a Python program to remove a key from a dictionary.

# d1 = {
#     'a' : 100,
#     'b' : 200,
#     'c' : 300,
#     'd' : 400
# }


# def count_characters(name):
#     char_count = {}

#     for char in name:
#         if char in char_count:
#             char_count[char] +=1
#         else:
#             char_count[char] = 1
    
#     return char_count


# name = "utkarsh"
# print(f"Count of characters in the name {name} is : {count_characters(name)}")


# mississippi

# word = str(input("Enter the word: "))

# m = 0
# i = 1,4,7,10
# s = 2,3,5,6
# p = 8,9


# def character_position(s):
#     position_dict = {}
#     for index,char in enumerate(s):
#         if char in position_dict:
#             position_dict[char].append(index)
#         else:
#             position_dict[char] = [index]
#     return position_dict

# word = 'mississippi'
# ans = character_position(word)
# print(ans)


# Desktop Application 

# Web Application - 

# tkinter module helps us to build a desktop application


# from tkinter import *

# root = Tk()   #to achieve a screen
# root.title("Ayra's Application")

# root.geometry('400x300')



# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Counter Application")
# root.geometry('400x300')
# # root.configure(bg="#FF11FF")

# label1 = Label(root,text="First Name",font=("Times New Roman",10),fg="green")
# label1.pack()

# e1 = Entry(root,fg='blue')
# e1.pack()

# root.mainloop()



# Firstname
# Last Name
# Email 
# Contact


# from tkinter import*

# def countdown(time_left):
#     if time_left > 0:
#         label2.config()
        


# def click():
#     global counter
#     counter = counter+1
#     label1.config(text=f"Click counter: {counter}")

# counter = 0


# root=Tk()
# root.title("click counter")
# root.geometry('200x200')
# root.configure(bg="#BC544B")
# label = Label(root,text="Click Counter",font=("Arial",15))
# label.pack(pady=20)
# label1=Label(root,text="Click counter: 0",font=("Arial"),bg=x"black",fg="white")
# label1.pack()
# label2 = Label(root,text="Time left : 30 sec ",font=("Arial"))
# label2.pack()
# b1 = Button(root,text="Click ME",fg="black",bg="dark red",width=15,command=click)
# b1.pack()
# root.mainloop()



# Password Genenator


# from tkinter import * 
# from tkinter import messagebox
# import random 
# import string

# def gen_pwd():
#     length = pwdslider.get()
#     include_uppercase = uppercase_var.get()
#     include_lowercase = lowercase_var.get()
#     include_numbers = numbers_var.get()
#     include_symbols = symbols_var.get()

#     if not (include_uppercase or include_lowercase or include_numbers or include_symbols):
#         messagebox.showerror("Selection Error","Select at least one option!.")
#         return 
    
#     character = ""
#     if include_uppercase:
#         character+= string.ascii_uppercase
#     if include_lowercase:
#         character+= string.ascii_lowercase
#     if include_numbers:
#         character+= string.digits
#     if include_symbols:
#         character+= string.punctuation

#     password = ''.join(random.choice(character) for _ in range(length))
#     output.delete(0,END)
#     output.insert(0,password)

# def copy_password():
#     password = output.get()
#     if password:
#         root.clipboard_clear()   #clear the clipboard
#         root.clipboard_append(password)
#         messagebox.showinfo("Copied","Password copied to Clipboard")
#     else:
#         messagebox.showerror("Error","No password to copy!")




# root = Tk()
# root.title("PAssword Generator")
# root.geometry('400x300')

# Label(root,text="Password Length : ").pack()
# pwdslider = Scale(root,from_=8,to_=32,orient="horizontal")
# pwdslider.pack()

# uppercase_var = BooleanVar()
# lowercase_var = BooleanVar()
# numbers_var = BooleanVar()
# symbols_var = BooleanVar()

# Checkbutton(root,text="Include Upercases",variable=uppercase_var).pack()
# Checkbutton(root,text="Include Lowercasse",variable=lowercase_var).pack()
# Checkbutton(root,text="Include Numbers",variable=numbers_var).pack()
# Checkbutton(root,text="Include Symbols",variable=symbols_var).pack()


# b1 = Button(root,text="Generate Password",command=gen_pwd)
# b1.pack(pady=10)


# output = Entry(root,width=40)
# output.pack(pady=10)

# b2 = Button(root,text="Copy Password",command=copy_password)
# b2.pack()

# root.mainloop()

# USD
# Japanese yen 
# EUR
# INR
# Dhirahms
# Korean 1


# Humza:


# yen -> USD,EUR,INR,DIR,WON
# EUR -> USD,YEN,INR,DIR,WON



# from tkinter import *

# from tkinter import ttk


# exchange_rates = {
#     "USD": {"EUR": 0.95, "YEN": 156.56, "INR": 84.45, "DIR": 3.67, "WON": 1405.53},
#     "EUR": {"USD": 1.05, "YEN": 165.32, "INR": 88.89, "DIR": 3.86, "WON": 1479.5},
#     "YEN": {"USD": 0.0064, "EUR": 0.0060, "INR": 0.54, "DIR": 0.023, "WON": 8.95},
#     "INR": {"USD": 0.0118, "EUR": 0.0113, "YEN": 1.85, "DIR": 0.043, "WON": 16.58},
#     "DIR": {"USD": 0.27, "EUR": 0.26, "YEN": 43.12, "INR": 23.18, "WON": 387.9},
#     "WON": {"USD": 0.00071, "EUR": 0.00068, "YEN": 0.11, "INR": 0.060, "DIR": 0.0026}
# }


# root = Tk()
# root.title("Currency exchanger 💰")
# root.geometry('300x200')

# def currency_convertor():
#     try:
#         amount = float(amount_entry.get())
#         f_currency = from_currency.get()
#         t_currency = to_currency.get()

#         if f_currency == t_currency:
#             converted_amount = amount
#         else:
#             converted_amount = amount * exchange_rates[f_currency][t_currency]
#         result_label.config(text=f"{converted_amount}")
#     except ValueError:
#         result_label.config(text=f"Please enter a valid amount!")
#     except KeyError:
#         result_label.config(text=f"Conversion rate not available!")

# amount_label = Label(root,text="Amount : ")
# amount_label.pack(pady=5)

# amount_entry = Entry(root)
# amount_entry.pack()

# currencies = list(exchange_rates.keys())

# from_currency = StringVar(value="USD")
# to_currency = StringVar(value="INR")

# f_dropdown = Label(root,text="Convert from")
# f_dropdown.pack()
# from_dropdown = ttk.Combobox(root,textvariable=from_currency,value=currencies)
# from_dropdown.pack()


# t_dropdown = Label(root,text="Convert to")
# t_dropdown.pack()
# to_dropdown = ttk.Combobox(root,textvariable=to_currency,value=currencies)
# to_dropdown.pack()

# convertor_button = Button(root,text="Convert",command=currency_convertor)
# convertor_button.pack()

# result_label = Label(root)
# result_label.pack()


# root.mainloop()


# from tkinter import *
# from tkinter import ttk

# # Unit conversion dictionary
# conversion = {
#     "Length": {
#         "inch": {"centimeter": 2.54, "meter": 0.0254, "kilometer": 0.0000254, "mile": 0.0000157},
#         "centimeter": {"inch": 0.393701, "meter": 0.01, "kilometer": 0.00001, "mile": 0.00000621},
#         "meter": {"centimeter": 100, "inch": 39.3701, "kilometer": 0.001, "mile": 0.000621371},
#         "kilometer": {"centimeter": 100000, "meter": 1000, "inch": 39370.1, "mile": 0.621371},
#         "mile": {"centimeter": 160934, "meter": 1609.34, "kilometer": 1.60934, "inch": 63360},
#     },
#     "Weight": {
#         "pounds": {"kilograms": 0.453592, "tons": 0.0005, "ounces": 16, "grams": 453.592},
#         "kilograms": {"pounds": 2.20462, "tons": 0.00110231, "ounces": 35.274, "grams": 1000},
#         "tons": {"kilograms": 907.18474, "pounds": 2000, "ounces": 32000, "grams": 907184.74},
#         "ounces": {"kilograms": 0.0283495, "tons": 0.00003125, "pounds": 0.0625, "grams": 28.3495},
#         "grams": {"kilograms": 0.001, "tons": 0.00000110231, "ounces": 0.035274, "pounds": 0.00220462},
#     }
# }

# # Initialize the Tkinter window
# root = Tk()
# root.title("Unit Converter")
# root.geometry('400x300')

# def unit_changer():
#     try:
#         amount = float(amount_entry.get())
#         category = category_combobox.get()
#         f_unit = from_unit_combobox.get()
#         t_unit = to_unit_combobox.get()

#         if category not in conversion:
#             result_label.config(text="Invalid Category")
#             return
#         if f_unit not in conversion[category] or t_unit not in conversion[category][f_unit]:
#             result_label.config(text="Invalid Inputs!")
#             return

#         if f_unit == t_unit:
#             converted_amount = amount
#         else:
#             converted_amount = amount* conversion[category][f_unit][t_unit]
#         result_label.config(text=f"Converted Amount : {converted_amount:.2f} {t_unit}")
#     except ValueError:
#         result_label.config(text="Please enter a valid number")

# amount_label= Label(root,text="Amount : ")
# amount_label.pack(pady = 5)

# amount_entry = Entry(root)
# amount_entry.pack(pady=5)

# category_label = Label(root,text="Category : ")
# category_label.pack(pady=5)

# category_combobox= ttk.Combobox(root,values=list(conversion.keys()),state="readonly")
# category_combobox.pack(pady=5)

# from_unit_label = Label(root, text="From Unit:")
# from_unit_label.pack(pady=5)

# from_unit_combobox = ttk.Combobox(root, state="readonly")
# from_unit_combobox.pack(pady=5)

# # Update units based on category selection
# def update_units(event):
#     category = category_combobox.get()
#     if category in conversion:
#         units = list(conversion[category].keys())
#         from_unit_combobox.config(values=units)
#         to_unit_combobox.config(values=units)
#         from_unit_combobox.set("")
#         to_unit_combobox.set("")

# category_combobox.bind("<<ComboboxSelected>>", update_units)

# to_unit_label = Label(root, text="To Unit:")
# to_unit_label.pack(pady=5)

# to_unit_combobox = ttk.Combobox(root, state="readonly")
# to_unit_combobox.pack(pady=5)

# convert_button = Button(root, text="Convert", command=unit_changer)
# convert_button.pack(pady=10)

# result_label = Label(root, text="")
# result_label.pack(pady=5)

# # Run the application
# root.mainloop()




# Auto clicker 

# pip install pyautogui

from tkinter import * 
from tkinter import messagebox
import pyautogui
import threading 
import time

def start_clicking():
    try:
        interval = float(entry_interval.get())
        messagebox.showinfo("Auto Clicker","Auto Clicker Started! Press 'Stop' to end")
        global running 
        running = True
        threading.Thread(target=auto_click,args=(interval,)).start()
    except:
        messagebox.showerror("Error","Please enter a valid number for the interval")

def stop_clicking():
    global running
    running = False
    messagebox.showinfo("Auto Clicker","Auto clicker stopped!")

def auto_click(interval):
    while running:
        pyautogui.click()
        time.sleep(interval)

root = Tk()
root.title("Autoclicker")

Label(root,text="Click interval (seconds): ").pack(pady=5)
entry_interval = Entry(root)
entry_interval.pack(pady=5)

start_button = Button(root,text="Start",bg="green",fg="white",command=start_clicking)
start_button.pack(pady=5)

stop_button = Button(root,text="Stop",bg="red",fg="white",command=stop_clicking)
stop_button.pack(pady=5)

running = False

root.mainloop()