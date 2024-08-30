# # # print('''1. Welcome to the class of the Python Programming
      
      
      
# # #       ''')
# # # print("Apoorv")

# # # # # 1. Print the table of 5 using for loop.


# # # operators and operands

# # # a+b

# # # operators:

# # # 1. Arithmetic operators
# # #     a. Addition +
# # #     b. Subtraction -
# # #     c. Multiplication *
# # #     d. Division /
# # #     e. Floor Division //
# # #     f. Modulus %
# # #     g. Exponent **

# # # a**b

# # # data types:

# # # 1. Integer (int)
# # # 2. Float (float)
# # # 3. String (str)
# # # 4. Boolean (bool)

# # # a = "4.00"
# # # print(type(a))


# # # a = int(input("Enter the first number: "))
# # # b = int(input("Enter the second number: "))

# # # conditional statements

# # # if condition:
# # #     statements  
    
# # # if condition:
# # #     statements
# # # else:
# # #     statements

# # # if condition:
# # #     statements
# # # elif condition:
# # #     statements
# # # else:
# # #  
# # # a=input("enter first number;")

# # # b=input("enter second number:")

# # # print("the addition of two number is" ,a+b)
# # # print("the subtraction of two numbers is",a-b)
# # # print("the multiplication of two numbers is",a*b)
# # # print("the division of two numbers is", a/b)
# # # print("the modulus of two numbers is" ,a%b)
# # # print("the exponent of two numbers is ",a**b)
# # # print("end of all the calculations")

# # #program to check if it is a leap year or not

# # # a=int(input("enter the year: '"))
# # # if a%4==0:
# # #     print("it is a leap year")
# # # else:
# # #     print("it is not a leap year")
    

# # # a=input("enter your name:")

# # # 1. Problem: Grading System
# # # Write a Python function grade_student(marks) that takes an integer marks (ranging from 0 to 100) as input and returns the corresponding grade based on the following grading system:

# # # Marks >= 90: Grade 'A'
# # # Marks >= 80 and < 90: Grade 'B'
# # # Marks >= 70 and < 80: Grade 'C'
# # # Marks >= 60 and < 70: Grade 'D'
# # # Marks < 60: Grade 'F'

# # marks=int(input("enter the marks:"))
# # if marks>=90:
# #     print("grade A")    
# # elif marks>=80 and marks<90:
# #     print("Grade b")
# # elif marks >=70 and marks<80:
# #     print("Grade c")
# # elif marks>=60 and marks<70:
# #     print("Grade D")
# # else:
# #     print("Grade F")


# # # Problem 2: FizzBuzz
# # # Write a function fizz_buzz(n) that takes an integer n and returns a list of strings with the numbers from 1 to n. But for multiples of three, the string should be "Fizz" instead of the number, and for the multiples of five, the string should be "Buzz". For numbers which are multiples of both three and five, the string should be "FizzBuzz".

# # number =int(input("enter the number :"))

# # for i in range(1,number+1):
# #     if i%3==0 and 5%i==0:
# #         print("Fizzbuzz")
# #     elif (3%i==0):
# #         print("fizz")
# #     elif(5%i==0):
# #         print("buzz")
# #     else:
# #         print(i)


# # # Problem 3: Number Classification
# # # Write a function classify_number(num) that takes an integer num as input and returns a string "Positive" if the number is positive, "Negative" if the number is negative, and "Zero" if the number is zero.

# # check=int(input("enter the number to be checked :"))
# # if check>0:
# #     print("Positive")
# # elif check<0:
# #     print("Negative")
# # else:
# #     print("zero")


# # # Problem 4: Age Category
# # # Write a function age_category(age) that takes an integer age as input and returns the age category as a string based on the following criteria:

# # # Age < 13: "Child"
# # # Age >= 13 and < 20: "Teenager"
# # # Age >= 20 and < 60: "Adult"
# # # Age >= 60: "Senior"

# # age = int(input("enter the age :"))

# # if age<13:
# #     print("Child")
# # elif age>=13 and age<20:
# #     print("Teenagers")
# # elif age>=20 and age<60:
# #     print("Adult")
# # else:
# #     print("Senior")



# # # Problem 5: Triangle Type
# # # Write a function triangle_type(a, b, c) that takes three integers a, b, and c as input representing the lengths of the sides of a triangle. The function should return a string representing the type of the triangle:

# # # "Equilateral" if all three sides are equal.
# # # "Isosceles" if exactly two sides are equal.
# # # "Scalene" if no sides are equal.
# # # "Not a triangle" if the input values do not form a valid triangle.

# # len1=int(input("enter the lenth of the first side :"))
# # len2=int(input("enter the lenth of the second side :"))
# # len3=int(input("enter the lenth of the third side :"))
# # if len1==len2 and len2==len3:
# #     print("equilateral")
# # elif len1==len2 or len2==len3 or len1==len3:
# #     print("isoceles")
# # elif len1!=len2 and len2!=len3 and len1!=len3:
# #     print("scalene")
# # else:
# #     print("not a triangle")



# # array : 

# # 1. list - mutable, ordered, allows duplicate elements, [].

# # l1 = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10]

# # for i in l1:
# #     print(i,end =  " " )

# # 2. tuple
# # 3. set
# # 4. dictionary





# # ---

# # ### Easy Level

# # 1. **Sum of List**: 
# #    Write a function to return the sum of all elements in a list.
# l1=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in l1:
#      sum=sum+i
#      print(sum)


# # 2. **Maximum Element**:
# #    Write a function to return the maximum element in a list.

# l2=[1,2,3,4,5,6,7,8,9,10]
# max=0
# for i in l2:
#     if i>max:
#         max=i
#         print(max)

# # 3. **Minimum Element**:
# #    Write a function to return the minimum element in a list.

# l3=[1,2,3,4,5,6,7,8,9,10]
# min=0
# for i in l3:
#     if i<min:
#         min=i
#         print(min)

# # 4. **Average of List**:
# #    Write a function to return the average of all elements in a list.

# l4=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in l4:
#    sum=sum+i
# print(sum/len(l4))



# # 5. **Count Occurrences**:
# #    Write a function to count the occurrences of a given element in a list.
# l5=[1,2,3,4,5,6,7,8,9,10]
# count=0
# for i in l5:
#     count=count+1
#     print(count)


# # 6. **Remove Duplicates**:
# #    Write a function to remove duplicates from a list.
# l6=[1,1,2,2,3,3,4,4,5,5]
# for i in l6:
#     if i not in l6:
#        print(i)

# # 7. **Reverse List**:
# #    Write a function to reverse a list.

# l7=[1,2,3,4,5,6,7,8,9,10]
# for i in l7:
#     print(i[::-1])


# # 8. **Check Sorted**:
# #    Write a function to check if a list is sorted in ascending order.

# l8=[1,2,3,4,5,6,7,8,9,10]
# for i in l8:
#     if i==sorted(l8):
#         print("sorted")
#     else:
#         print ("not sorted")

# # 9. **Find Element**:
# #    Write a function to find if an element exists in a list and return its index.

# l9=[1,2,3,4,5,6,7,8,9,10]
# for i in l9:
#     if i==5:
#         print(l9.index(i))
#     else:
#         print("element not found")

# # 10. **List Slicing**:
# #     Write a function to return the first and last n elements of a list.

# l10=[1,2,3,4,5,6,7,8,9,10]
# for i in l10:
#     print(l10[0],l10[-1])

# # ### Medium Level

# # 1. **Merge Two Lists**:
# #    Write a function to merge two sorted lists into a single sorted list.
# l11=[1,2,3,4,5,6,7,8,9,10]
# l12=[11,12,13,14,15,16,17,18,19,20]
# l13=l11=l12
# print(l13)

# # 2. **Rotate List**:
# #    Write a function to rotate a list by k elements.

# l14=[1,2,3,4,5,6,7,8,9,10]
# k=2
# for i in l14:
#     print(l14[k:]+l14[:k])




# # 3. **Intersection of Lists**:
# #    Write a function to return the intersection of two lists.

# l15=[1,2,3,4,5,6,7,8,9,10]
# l16=[11,12,13,14,15,16,17,18,19,20]
# l17=[]
# for i in l15:
#     if i in l16:
#         l17.append(i)
#         print(l17)


# # 4. **Union of Lists**:
# #    Write a function to return the union of two lists.

# l18=[1,2,3,4,5,6,7,8,9,10]
# l19=[11,12,13,14,15,16,17,18,19,20]
# l20=[]
# for i in l18:
#     l20.append(i)
#     for i in l19:
#         l20.append(i)
#         print(l20)


# # 5. **List Comprehension**:
# #    Given a list of numbers, write a list comprehension to return the squares of all even numbers.

# l21=[1,2,3,4,5,6,7,8,9,10]
# for i in l21:
#     if i%2==0:
#         print(i**2)


# # 6. **Sublist Check**:
# #    Write a function to check if a list is a sublist of another list.

# l22=[1,2,3,4,5,6,7,8,9,10]
# l23=[1,2,3,4]
# for i in l22:
#     if i in l23:
#         print("sublist")
#     else:
#         print("not a sublist")



# # 7. **Sum of Pairs**:
# #    Write a function to find all pairs in a list that sum up to a given number.

# l24=[1,2,3,4,5,6,7,8,9,10]
# sum=10
# for  i in l24:
#     for j in l24:
#         if i+j==sum:
#             print(i,j)


# # 8. **Flatten List**:
# #    Write a function to flatten a nested list.

# l25=[[1,2,3],[4,5,6],[7,8,9]]
# for i in l25:
#     for j in i:
#         print(j)



# # 9. **Zigzag Merge**:
# #    Write a function to merge two lists in a zigzag manner.

# l26=[1,2,3,4,5]
# l27=[6,7,8,9,10]
# l28=[]
# for i in range(len(l26)):
#     l28.append(l26[i])
#     l28.append(l27[i])
#     print(l28)



# # 10. **Frequency Count**:
# #     Write a function to return a dictionary with the frequency count of each element in a list.

# l29=[1,2,3,4,5,6,7,8,9,10]
# d={}
# for i in l29:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1

# # ---

# #append is a built in fuction to add some new or required elements at the enf of a list
# #its syntax is list.append(element)


# # operators in python :
# # Arithmetic
# # relational 
# # logical(and,not.or)
# # identity(is ,is not)
# # bitwise(&,|,^,<<,>>)
# # assingment(=


# type()it is used to determine the type of the variables 
# capitalize ()function capitalize the first letter of the string only the first letter
# find()function find the substring in a given string
# tuples and list almost the same but the element of tuples cannot be changed as that in list it can be changed with an ease



# append() - it always add the element at the list
# insert() -  it always add the element at the specific index 

# pop() - it is delete the element