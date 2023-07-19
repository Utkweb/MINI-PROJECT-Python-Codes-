import turtle
import time
from OOP_is_best_ping_pong import Paddle, Ball

sc = turtle.Screen()
sc.setup(width=800, height=600)
sc.bgcolor('black')
sc.title("Ping Pong but its ping pong")
sc.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

sc.listen()
sc.onkey(r_paddle.up, 'Up')
sc.onkey(r_paddle.down, 'Down')
sc.onkey(l_paddle.up, 'w')
sc.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    sc.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
sc.exitonclick()


from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape(name='square')
        self.color('white')
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 0.1
        self.y_move = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1