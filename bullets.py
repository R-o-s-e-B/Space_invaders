from turtle import Turtle

class Bullets(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('yellow')
        self.shapesize(0.25, 1.5)
        self.penup()
        self.goto(pos)
        self.setheading(90)
        self.hideturtle()
        self.pos = pos
        self.collide = False


    def shoot(self,):
        self.collide = True
        self.goto(self.pos)
        self.showturtle()
        self.collide = False

class EnemyBullets(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.shapesize(0.25, 1)
        self.penup()
        self.goto(pos)
        self.setheading(270)
        self.hideturtle()
        self.pos = pos
        self.collide = False


    def shoot(self,):
        self.collide = True
        self.goto(self.pos)
        self.showturtle()
        self.collide = False

