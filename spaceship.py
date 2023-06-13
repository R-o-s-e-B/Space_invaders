from turtle import Turtle

class Spaceship(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 4, 1)
        self.penup()
        self.goto(pos)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def check(self):
        if self.xcor() < -400:
            self.goto(-390, self.ycor())
        if self.xcor() > 400:
            self.goto(390, self.ycor())



