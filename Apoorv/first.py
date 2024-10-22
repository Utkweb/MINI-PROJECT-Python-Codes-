# # # # # print('''1. Welcome to the class of the Python Programming
      
      
      
# # # # #       ''')
# # # # # print("Apoorv")

# # # # # # # 1. Print the table of 5 using for loop.


# # # # # operators and operands

# # # # # a+b

# # # # # operators:

# # # # # 1. Arithmetic operators
# # # # #     a. Addition +
# # # # #     b. Subtraction -
# # # # #     c. Multiplication *
# # # # #     d. Division /
# # # # #     e. Floor Division //
# # # # #     f. Modulus %
# # # # #     g. Exponent **

# # # # # a**b

# # # # # data types:

# # # # # 1. Integer (int)
# # # # # 2. Float (float)
# # # # # 3. String (str)
# # # # # 4. Boolean (bool)

# # # # # a = "4.00"
# # # # # print(type(a))


# # # # # a = int(input("Enter the first number: "))
# # # # # b = int(input("Enter the second number: "))

# # # # # conditional statements

# # # # # if condition:
# # # # #     statements  
    
# # # # # if condition:
# # # # #     statements
# # # # # else:
# # # # #     statements

# # # # # if condition:
# # # # #     statements
# # # # # elif condition:
# # # # #     statements
# # # # # else:
# # # # #  
# # # # # a=input("enter first number;")

# # # # # b=input("enter second number:")

# # # # # print("the addition of two number is" ,a+b)
# # # # # print("the subtraction of two numbers is",a-b)
# # # # # print("the multiplication of two numbers is",a*b)
# # # # # print("the division of two numbers is", a/b)
# # # # # print("the modulus of two numbers is" ,a%b)
# # # # # print("the exponent of two numbers is ",a**b)
# # # # # print("end of all the calculations")

# # # # #program to check if it is a leap year or not

# # # # # a=int(input("enter the year: '"))
# # # # # if a%4==0:
# # # # #     print("it is a leap year")
# # # # # else:
# # # # #     print("it is not a leap year")
    

# # # # # a=input("enter your name:")

# # # # # 1. Problem: Grading System
# # # # # Write a Python function grade_student(marks) that takes an integer marks (ranging from 0 to 100) as input and returns the corresponding grade based on the following grading system:

# # # # # Marks >= 90: Grade 'A'
# # # # # Marks >= 80 and < 90: Grade 'B'
# # # # # Marks >= 70 and < 80: Grade 'C'
# # # # # Marks >= 60 and < 70: Grade 'D'
# # # # # Marks < 60: Grade 'F'

# # # # marks=int(input("enter the marks:"))
# # # # if marks>=90:
# # # #     print("grade A")    
# # # # elif marks>=80 and marks<90:
# # # #     print("Grade b")
# # # # elif marks >=70 and marks<80:
# # # #     print("Grade c")
# # # # elif marks>=60 and marks<70:
# # # #     print("Grade D")
# # # # else:
# # # #     print("Grade F")


# # # # # Problem 2: FizzBuzz
# # # # # Write a function fizz_buzz(n) that takes an integer n and returns a list of strings with the numbers from 1 to n. But for multiples of three, the string should be "Fizz" instead of the number, and for the multiples of five, the string should be "Buzz". For numbers which are multiples of both three and five, the string should be "FizzBuzz".

# # # # number =int(input("enter the number :"))

# # # # for i in range(1,number+1):
# # # #     if i%3==0 and 5%i==0:
# # # #         print("Fizzbuzz")
# # # #     elif (3%i==0):
# # # #         print("fizz")
# # # #     elif(5%i==0):
# # # #         print("buzz")
# # # #     else:
# # # #         print(i)


# # # # # Problem 3: Number Classification
# # # # # Write a function classify_number(num) that takes an integer num as input and returns a string "Positive" if the number is positive, "Negative" if the number is negative, and "Zero" if the number is zero.

# # # # check=int(input("enter the number to be checked :"))
# # # # if check>0:
# # # #     print("Positive")
# # # # elif check<0:
# # # #     print("Negative")
# # # # else:
# # # #     print("zero")


# # # # # Problem 4: Age Category
# # # # # Write a function age_category(age) that takes an integer age as input and returns the age category as a string based on the following criteria:

# # # # # Age < 13: "Child"
# # # # # Age >= 13 and < 20: "Teenager"
# # # # # Age >= 20 and < 60: "Adult"
# # # # # Age >= 60: "Senior"

# # # # age = int(input("enter the age :"))

# # # # if age<13:
# # # #     print("Child")
# # # # elif age>=13 and age<20:
# # # #     print("Teenagers")
# # # # elif age>=20 and age<60:
# # # #     print("Adult")
# # # # else:
# # # #     print("Senior")



# # # # # Problem 5: Triangle Type
# # # # # Write a function triangle_type(a, b, c) that takes three integers a, b, and c as input representing the lengths of the sides of a triangle. The function should return a string representing the type of the triangle:

# # # # # "Equilateral" if all three sides are equal.
# # # # # "Isosceles" if exactly two sides are equal.
# # # # # "Scalene" if no sides are equal.
# # # # # "Not a triangle" if the input values do not form a valid triangle.

# # # # len1=int(input("enter the lenth of the first side :"))
# # # # len2=int(input("enter the lenth of the second side :"))
# # # # len3=int(input("enter the lenth of the third side :"))
# # # # if len1==len2 and len2==len3:
# # # #     print("equilateral")
# # # # elif len1==len2 or len2==len3 or len1==len3:
# # # #     print("isoceles")
# # # # elif len1!=len2 and len2!=len3 and len1!=len3:
# # # #     print("scalene")
# # # # else:
# # # #     print("not a triangle")



# # # # array : 

# # # # 1. list - mutable, ordered, allows duplicate elements, [].

# # # # l1 = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10]

# # # # for i in l1:
# # # #     print(i,end =  " " )

# # # # 2. tuple
# # # # 3. set
# # # # 4. dictionary





# # # # ---

# # # # ### Easy Level

# # # # 1. **Sum of List**: 
# # # #    Write a function to return the sum of all elements in a list.
# # # l1=[1,2,3,4,5,6,7,8,9,10]
# # # sum=0
# # # for i in l1:
# # #      sum=sum+i
# # #      print(sum)


# # # # 2. **Maximum Element**:
# # # #    Write a function to return the maximum element in a list.

# # # l2=[1,2,3,4,5,6,7,8,9,10]
# # # max=0
# # # for i in l2:
# # #     if i>max:
# # #         max=i
# # #         print(max)

# # # # 3. **Minimum Element**:
# # # #    Write a function to return the minimum element in a list.

# # # l3=[1,2,3,4,5,6,7,8,9,10]
# # # min=0
# # # for i in l3:
# # #     if i<min:
# # #         min=i
# # #         print(min)

# # # # 4. **Average of List**:
# # # #    Write a function to return the average of all elements in a list.

# # # l4=[1,2,3,4,5,6,7,8,9,10]
# # # sum=0
# # # for i in l4:
# # #    sum=sum+i
# # # print(sum/len(l4))



# # # # 5. **Count Occurrences**:
# # # #    Write a function to count the occurrences of a given element in a list.
# # # l5=[1,2,3,4,5,6,7,8,9,10]
# # # count=0
# # # for i in l5:
# # #     count=count+1
# # #     print(count)


# # # # 6. **Remove Duplicates**:
# # # #    Write a function to remove duplicates from a list.
# # # l6=[1,1,2,2,3,3,4,4,5,5]
# # # for i in l6:
# # #     if i not in l6:
# # #        print(i)

# # # # 7. **Reverse List**:
# # # #    Write a function to reverse a list.

# # # l7=[1,2,3,4,5,6,7,8,9,10]
# # # for i in l7:
# # #     print(i[::-1])


# # # # 8. **Check Sorted**:
# # # #    Write a function to check if a list is sorted in ascending order.

# # # l8=[1,2,3,4,5,6,7,8,9,10]
# # # for i in l8:
# # #     if i==sorted(l8):
# # #         print("sorted")
# # #     else:
# # #         print ("not sorted")

# # # # 9. **Find Element**:
# # # #    Write a function to find if an element exists in a list and return its index.

# # # l9=[1,2,3,4,5,6,7,8,9,10]
# # # for i in l9:
# # #     if i==5:
# # #         print(l9.index(i))
# # #     else:
# # #         print("element not found")

# # # # 10. **List Slicing**:
# # # #     Write a function to return the first and last n elements of a list.

# # # l10=[1,2,3,4,5,6,7,8,9,10]
# # # for i in l10:
# # #     print(l10[0],l10[-1])

# # # # ### Medium Level

# # # # 1. **Merge Two Lists**:
# # # #    Write a function to merge two sorted lists into a single sorted list.
# # # l11=[1,2,3,4,5,6,7,8,9,10]
# # # l12=[11,12,13,14,15,16,17,18,19,20]
# # # l13=l11=l12
# # # print(l13)

# # # # 2. **Rotate List**:
# # # #    Write a function to rotate a list by k elements.

# # # l14=[1,2,3,4,5,6,7,8,9,10]
# # # k=2
# # # for i in l14:
# # #     print(l14[k:]+l14[:k])




# # # # 3. **Intersection of Lists**:
# # # #    Write a function to return the intersection of two lists.

# # # l15=[1,2,3,4,5,6,7,8,9,10]
# # # l16=[11,12,13,14,15,16,17,18,19,20]
# # # l17=[]
# # # for i in l15:
# # #     if i in l16:
# # #         l17.append(i)
# # #         print(l17)


# # # # 4. **Union of Lists**:
# # # #    Write a function to return the union of two lists.

# # # l18=[1,2,3,4,5,6,7,8,9,10]
# # # l19=[11,12,13,14,15,16,17,18,19,20]
# # # l20=[]
# # # for i in l18:
# # #     l20.append(i)
# # #     for i in l19:
# # #         l20.append(i)
# # #         print(l20)


# # # # 5. **List Comprehension**:
# # # #    Given a list of numbers, write a list comprehension to return the squares of all even numbers.

# # # l21=[1,2,3,4,5,6,7,8,9,10]
# # # for i in l21:
# # #     if i%2==0:
# # #         print(i**2)


# # # # 6. **Sublist Check**:
# # # #    Write a function to check if a list is a sublist of another list.

# # # l22=[1,2,3,4,5,6,7,8,9,10]
# # # l23=[1,2,3,4]
# # # for i in l22:
# # #     if i in l23:
# # #         print("sublist")
# # #     else:
# # #         print("not a sublist")



# # # # 7. **Sum of Pairs**:
# # # #    Write a function to find all pairs in a list that sum up to a given number.

# # # l24=[1,2,3,4,5,6,7,8,9,10]
# # # sum=10
# # # for  i in l24:
# # #     for j in l24:
# # #         if i+j==sum:
# # #             print(i,j)


# # # # 8. **Flatten List**:
# # # #    Write a function to flatten a nested list.

# # # l25=[[1,2,3],[4,5,6],[7,8,9]]
# # # for i in l25:
# # #     for j in i:
# # #         print(j)



# # # # 9. **Zigzag Merge**:
# # # #    Write a function to merge two lists in a zigzag manner.

# # # l26=[1,2,3,4,5]
# # # l27=[6,7,8,9,10]
# # # l28=[]
# # # for i in range(len(l26)):
# # #     l28.append(l26[i])
# # #     l28.append(l27[i])
# # #     print(l28)



# # # # 10. **Frequency Count**:
# # # #     Write a function to return a dictionary with the frequency count of each element in a list.

# # # l29=[1,2,3,4,5,6,7,8,9,10]
# # # d={}
# # # for i in l29:
# # #     if i in d:
# # #         d[i]+=1
# # #     else:
# # #         d[i]=1

# # # # ---

# # # #append is a built in fuction to add some new or required elements at the enf of a list
# # # #its syntax is list.append(element)


# # # # operators in python :
# # # # Arithmetic
# # # # relational 
# # # # logical(and,not.or)
# # # # identity(is ,is not)
# # # # bitwise(&,|,^,<<,>>)
# # # # assingment(=


# # # type()it is used to determine the type of the variables 
# # # capitalize ()function capitalize the first letter of the string only the first letter
# # # find()function find the substring in a given string
# # # tuples and list almost the same but the element of tuples cannot be changed as that in list it can be changed with an ease



# # # append() - it always add the element at the list
# # # insert() -  it always add the element at the specific index 

# # # pop() - it is delete the element

# # # capitalize()	Converts the first character to upper case

 
# # a="apoorv singh"
# # print(capitalize(a))


# # # casefold()	Converts string into lower case
# # # center()	Returns a centered string
# # # count()	Returns the number of times a specified value occurs in a string
# # # encode()	Returns an encoded version of the string
# # # endswith()	Returns true if the string ends with the specified value
# # # expandtabs()	Sets the tab size of the string
# # # find()	Searches the string for a specified value and returns the position of where it was found
# # # format()	Formats specified values in a string
# # # format_map()	Formats specified values in a string
# # # index()	Searches the string for a specified value and returns the position of where it was found
# # # isalnum()	Returns True if all characters in the string are alphanumeric
# # # isalpha()	Returns True if all characters in the string are in the alphabet
# # # isascii()	Returns True if all characters in the string are ascii characters
# # # isdecimal()	Returns True if all characters in the string are decimals
# # # isdigit()	Returns True if all characters in the string are digits
# # # isidentifier()	Returns True if the string is an identifier
# # # islower()	Returns True if all characters in the string are lower case
# # # isnumeric()	Returns True if all characters in the string are numeric
# # # isprintable()	Returns True if all characters in the string are printable
# # # isspace()	Returns True if all characters in the string are whitespaces
# # # istitle()	Returns True if the string follows the rules of a title
# # # isupper()	Returns True if all characters in the string are upper case
# # # join()	Joins the elements of an iterable to the end of the string
# # # ljust()	Returns a left justified version of the string
# # # lower()	Converts a string into lower case
# # # lstrip()	Returns a left trim version of the string
# # # maketrans()	Returns a translation table to be used in translations
# # # partition()	Returns a tuple where the string is parted into three parts
# # # replace()	Returns a string where a specified value is replaced with a specified value
# # # rfind()	Searches the string for a specified value and returns the last position of where it was found
# # # rindex()	Searches the string for a specified value and returns the last position of where it was found
# # # rjust()	Returns a right justified version of the string
# # # rpartition()	Returns a tuple where the string is parted into three parts
# # # rsplit()	Splits the string at the specified separator, and returns a list
# # # rstrip()	Returns a right trim version of the string
# # # split()	Splits the string at the specified separator, and returns a list
# # # splitlines()	Splits the string at line breaks and returns a list
# # # startswith()	Returns true if the string starts with the specified value
# # # strip()	Returns a trimmed version of the string
# # # swapcase()	Swaps cases, lower case becomes upper case and vice versa
# # # title()	Converts the first character of each word to upper case
# # # translate()	Returns a translated string
# # # upper()	Converts a string into upper case
# # # zfill()	Fills the string with a specified number of 0 values at the beginning

# # print("hello world ")
# # name='apoorv singh.is a man '
# # print(name.capitalize())

# # ist1=['shaswat','parth','sparsh']
# # list2=['mahi','shirid','vedansh']
# # list3=list1+list2
# # print(list3)l
# # l1=[1,2,3,4,5]
# # l2=[1,2,3,4,5]
# # l3=(l1+l2)*3
# # print(l3)

# # to store charachter in list you need to use single qoutes around it and if you want to triple or add the following list u have to store it in a different variable firts or directly print it in the print() function but remember it to be syntax error free 
# # LEARNING LIST SLICES 

# # names=['parth','apoorv','sangeeta','mohit','sparsh','utkarsh','om']
# # print(names[1:4])
# # print(names[2:5])
# # print(names[:2])
# # print(names[4:])

# # append() function is used to add only a single element at the end of the list but extend()fucntion is used to add a new list at te end of a list it usually means that to append a list at the end of another list

# # list69=[1,2,3,4,5,6,7,8,9,0]
# # list420=[11,12,13,14,15,16,17,18,19,10]
# # list1=list69.extend(list420)
# # print(list1)

# # ENUGH FOR TODAY...

# import random

# x='y'

# while x=="y":
#     no = random.randint(1,6)

#     if no ==1:
#         print("[--------]")
#         print("[        ]")
#         print("[    0   ]")
#         print("[        ]")
#         print("[--------]")
#     if no==2:
#         print("[--------]")
#         print("[0       ]")
#         print("[        ]")
#         print("[     0  ]")
#         print("[--------]")
#     if no==3:
#         print("[--------]")
#         print("[        ]")
#         print("[0   0  0]")
#         print("[        ]")
#         print("[--------]")
#     if no==4:
#         print("[--------]")
#         print("[0      0]")
#         print("[        ]")
#         print("[0      0]")
#         print("[--------]")
#     if no==5:
#         print("[--------]")
#         print("[0      0]")
#         print("[    0   ]")
#         print("[0      0]")
#         print("[--------]")
#     if no==6:
#         print("[--------]")
#         print("[0   0  0]")
#         print("[        ]")
#         print("[0   0  0]")
#         print("[--------]")

#     x=input("press y to roll again and n to exit:")
#     print('\n')

# # random number guessing game
# 1. Take the input from the user of string and count the length without using len().

# name= str(input("enter a string to be counted : "))
# count=0
# for i in name :
#     count = count+1
    
# print(count)
# 2. Take a list by your side of string and count how many elements are there who are starting with vowel.


# list1=["apoorv","sangeeta","utkarsh","mohit","rajkumar","om"]
# vowel = 'AEIOUaeiou'
# count=0

# for i in list1:
#     if i[0] in vowel:
#        count= count +1
# print(count)


# 3. reverse the list without using normal method

# def Reverse(lst):
#    new_lst = lst[::-1]
#    return new_lst


# lst = [10, 11, 12, 13, 14, 15]
# print(Reverse(lst))


# 4. find the kth largest and kth smallest element in a list.


# def ksmall(list1,k):
#     for i in range(0,len(list1)):
#         return list1[k-1]
# def klarge(list1,k):
#     for i in range(0,len(list1)):
#         return list1[len(list1)-k]


# list1=[1,2,3,4,5,6,7,8,9]
# k = int(input("Enter the k value"))

# print(ksmall(list1,k))
# print(klarge(list1,k))


# import random
# numtoguess=random.randrange(100)
# chances=7
# guesscount=0

# while guesscount<chances:

#     guesscount=guesscount+1
#     myguess=int(input('please enter your guess:'))

#     if myguess==numtoguess:
#         print('the number is{numtoguess}and you found it right in the {guesscount}attempt')
#         break
#     elif guesscount>= chances and myguess!=numtoguess:
#         print('oops the number is {numtoguess} BETTER LUCK NEXT TIME')

#     elif myguess>numtoguess:
#         print('your guess is higher')
#     elif myguess<numtoguess:
#         print('your guess is leser')

# hillo day-9-9-24

# chapter 7 iteration 

# 1- while statement :while statement is often used for iteration as it is more reliable

# write a program to wrtie hello world three times


# name =str(input("enter the name to be printed :"))
# count =0
# while (count<3):
#     count=count+1
#     print(name)

# # write a program to count down from a given number 
# count=int(input("enter the number to be counted back:"))


# while True:
#     count=count-1
#     print(f"tick tick {count}")

#     if count==0:
#         break

# print("the loop has ended")


# Find the length of a string without using length fucntion 

# name= str(input("enter the string to be counted :"))
# i=0

# while i< len(name):
#      i+=1
#      pass
# print("the value of i is :",i)




# write first ten integers and thier squares 

# num=1 
# print("numbers -------squares")
# while(num<=10):
#     print(num,"------", {num**2})
#     num=num+1

# writ a program tp print the series : 105,98,91........7

# num= 105
# while (num>=7):
#     print(num)
#     num= num-7

# write a program in python to print  sum of first 10 even numbers 

# num=2
# sum=0
# while(num<=20):
#     sum= sum+num
#     num= num +2
# print(su


# write a program to print a table of a number entered by the user 


# i=1
# num=int(input("enter the number to be printed "))

# while (i<=10):
#     print(num,"*",i,"=",num*i)
#     i=i+1


# write a program to check whether the number is prime or not using the while loop 

# num1=int(input("enter any number :"))
# k=0
# if num1==0 or num1==1:
#     print("not a prime number ")
# else:
#     i=2
#     while(i<num1):
#         if num1%i==0:
#             k=k+1
#         i=i+1
# if k==0:
#     print("it is a prime number ")
# else:
#     print("it is not a prime number ")

# 

