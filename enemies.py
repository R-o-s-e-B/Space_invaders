from turtle import Turtle
enemy_list = []
class Enemies():
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.place()

    def place(self):
        global enemy_list
        for i in self.level:
            enemy = Turtle()
            enemy.shape('images/Asset-1.gif')
            enemy.penup()
            enemy.goto(i)
            enemy_list.append(enemy)









