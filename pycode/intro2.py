import turtle

# Setup the turtle screen
screen = turtle.Screen()
screen.bgcolor("yellow")

# Create a turtle instance
pen = turtle.Turtle()
pen.speed(2)  # Set the drawing speed

# Draw the base of the house
pen.penup()
pen.goto(-100, -100)
pen.pendown()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)

# Draw the roof of the house
pen.penup()
pen.goto(-100, 100)
pen.pendown()
pen.setheading(45)
pen.forward(141)
pen.right(90)
pen.forward(141)

# Draw the door of the house
pen.penup()
pen.goto(-50, -100)
pen.pendown()
pen.setheading(90)
pen.forward(100)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(100)

# Draw the window of the house
pen.penup()
pen.goto(30, 0)
pen.pendown()
pen.setheading(90)
pen.forward(60)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(60)
pen.left(90)
pen.forward(60)

# Hide the turtle
pen.hideturtle()

# Exit on click
turtle.done()
