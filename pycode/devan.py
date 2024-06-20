# print("Hello World!, I'm going to learn python from now")

# variables - a,b

# data types - int
#                 float
#                 string
#                 boolean



# a = 4 
# b = 5

# print(a+b)

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))


# String formatting
# print("Summation of two numbers are :",(a+b))


# name = input("Enter your name: ")
# standard = input("Enter your class: ")
# age = input("Enter your age: ")


# My name is Devan and I am 20 years old, and i study in 12th standard


# + 
# -
# *
# /
# //
# %
# **

# print(6**2)

# P - PARANTHESIS({})
# E - EXPONENT
# M - MULTIPLICATION
# D - DIVISION
# A - ADDITION
# S - SUBTRACTION




# a = int(input("Enter a number :"))
# b = int(input("Enter a number :"))

# print(a+b)


# conditional statements -

# if statements
# if-else statements
# if-elif-else statements


# if-statement 

# if(condition):
#     statements

# age = int(input("Enter your age: "))
# if(age>=18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")




# if- else statements

# if(condition):
#     statements
# else:
#     statements


# if-elif-else statements

# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements



# num = int(input("Enter a number: "))
# if(num%2 == 0):
#     print("The number is even")
# else:
#     print("The number is odd")
    
    
# loops: for loop, while loop
# for variable in range(start,stop,step):
#     statements

# for i in range(1,11):
#     print(i,end =" ")



# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# 8 * 6 = 48
# 8 * 7 = 56
# 8 * 8 = 64
# 8 * 9 = 72
# 8 * 10 = 80


# num = int(input("Enter the number of which you want the table of : "))
# for i in range(1,21):
#     print(num,"X",i,"=",num*i)

# for loop -> if else statements


# even_count = 0
# odd_count = 0
# for i in range(1,11):
#     if(i%2==0):
#         even_count+=1
#     else:
#         odd_count+=1
# print("Even numbers are :",even_count)
# print("Odd numbers are :",odd_count)



# while loop

# while condition:
#     statements

# i = 15
# while i>-20:
#     print(i,end =" ")
#     i=i-1


# import turtle

# sk = turtle.Turtle()

# for i in range(4):
#     sk.forward(100)
#     sk.right(90)


# import turtle
# star = turtle.Turtle()


# star.right(75)
# star.forward(100)

# for i in range(4):
#     star.right(144)
#     star.forward(100)

# turtle.done()

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("black")

# pen = turtle.Turtle()
# pen.speed(0)

# pen.fillcolor("white")
# pen.begin_fill()

# pen.circle(100)

# pen.end_fill()
# pen.hideturtle()

# turtle.done()

# import turtle


# t = turtle.Turtle()


# t.fillcolor("cyan")


# t.begin_fill()


# for _ in range(5):
#     t.forward(200)
#     t.right(288)


# t.end_fill()


# t.hideturtle()





# import turtle


# turtle.forward(200)

# turtle.left(90)

# turtle.forward(100)

# turtle.left(90)

# turtle.forward(200)

# turtle.left(90)
# turtle.forward(100)




# turtle.mainloop()



# import turtle

# turtle.forward(100)

# turtle.left(120)

# turtle.forward(100)

# turtle.left(120)

# turtle.forward(100)

# turtle.mainloop()
# import turtle

# turtle.seth(0)
# turtle.forward(80)
# turtle.write("East")
# turtle.home()

# turtle.setheading(90)
# turtle.forward(80)
# turtle.write("North")
# turtle.home()

# turtle.seth(180)
# turtle.forward(80)
# turtle.write("West", align="right")
# turtle.home()

# turtle.setheading(270)
# turtle.forward(80)
# turtle.write("South")
# turtle.ht()




# import turtle

# turtle.forward(150)
# turtle.right(90)
# turtle.forward(80)
# turtle.right(90)
# turtle.forward(150)
# turtle.right(90)
# turtle.forward(80)


# turtle.mailoop()


# import turtle 

# t = turtle.Turtle()


# t.speed(1)

# for _ in range(2):
#     t.forward(200)
#     t.left(120)
# t.forward(200)


# turtle.done()


# import turtle

# # Create a turtle object
# t = turtle.Turtle()

# # Draw the obtuse triangle
# side_length = 100
# angle = 120  # Angle for an obtuse triangle
# t.forward(side_length)  # Draw the first side
# t.left(angle)  # Turn left
# t.forward(side_length)  # Draw the second side
# t.left(angle)  # Turn left
# t.forward(side_length)  # Draw the third side

# # Close the turtle graphics window
# turtle.done()




import random 

def user_choice():
    user = input("Enter your choice between ('rock','paper','scissor') : ").lower()
    while user not in ['rock','paper','scissor']:
        print("Invalid choice")
        user = input("Enter your choice between ('rock','paper','scissor') : ").lower()
    return user
    
def bot_choice():
    return random.choice(['rock','paper','scissor'])

def winner(user_choice,bot_choice):
    if user_choice == bot_choice:
        return "It's a TIE"
    elif (user_choice == 'rock' and bot_choice == 'scissor') or \
        (user_choice == 'scissor' and bot_choice == 'paper') or \
        (user_choice == 'paper' and bot_choice == 'rock'):
            return "User wins"
    else:
        return "Bot wins"

def play_game():
    print("Welcome to the Rock Paper and Scissor Game!!!!!!!!")
    while True:
        user = user_choice()
        bot = bot_choice()
        
        print(f"User Choice : {user}")
        print(f"Bot Choice : {bot}")
        print(winner(user,bot))
        play = input("do you wanna play the game again? (yes/no) : ").lower()
        if play!='yes':
            print("Thanks for playing up the game")
            break
        
play_game()