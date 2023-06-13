from turtle import Turtle
ALIGNMENT = "right"
FONT = ("Arial", 14, "normal")

class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(300, 300)
        self.hideturtle()
        self.reset()
        self.update_scoreboard()

    def write_text(self, text):
        self.write(text, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 100
        self.update_scoreboard()