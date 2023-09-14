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


# import turtle as t

# # Set up the turtle screen
# t.speed(0)
# t.hideturtle()
# t.bgcolor("lightblue")

# # Define a function to draw a circle
# def draw_circle(x, y, radius, color):
#     t.penup()
#     t.goto(x, y - radius)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# # Define a function to draw a rectangle
# def draw_rectangle(x, y, width, height, color):
#     t.penup()
#     t.goto(x - width/2, y - height/2)
#     t.pendown()
#     t.fillcolor(color)
#     t.begin_fill()
#     for _ in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)
#     t.end_fill()

# # Draw Shinchan's head
# draw_circle(0, 0, 50, "pink")

# # Draw Shinchan's eyes
# draw_circle(-20, 10, 5, "white")
# draw_circle(20, 10, 5, "white")
# draw_circle(-20, 10, 2, "black")
# draw_circle(20, 10, 2, "black")

# # Draw Shinchan's mouth
# t.penup()
# t.goto(-15, -10)
# t.pendown()
# t.right(90)
# t.circle(15, 180)

# # Draw Shinchan's cheeks
# draw_circle(-35, -10, 7, "rosybrown")
# draw_circle(35, -10, 7, "rosybrown")

# # Hide the turtle and display the result
# t.hideturtle()
# t.done()
