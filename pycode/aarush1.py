# import turtle

# screen = turtle.Screen()
# screen.bgcolor("yellow")

# # Create a turtle instance
# pen = turtle.Turtle()
# pen.speed(2)  # Set the drawing speed

# # Draw the base of the house
# pen.penup()
# pen.goto(-100, -100)
# pen.pendown()
# pen.forward(200)
# pen.left(90)
# pen.forward(200)
# pen.left(90)
# pen.forward(200)
# pen.left(90)
# pen.forward(200)
# pen.left(90)


# # Hide the turtle
# pen.hideturtle()

# # Exit on click
# turtle.done()


import turtle

t = turtle.Turtle()

s1 = 200
s2 = 100

t.forward(s1)
t.left(90)

t.forward(s2)
t.left(90)

t.forward(s1)
t.left(90)

t.forward(s2)
t.left(90)


turtle.done()  # Add this line to keep the window open
