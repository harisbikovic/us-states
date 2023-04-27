from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(200, 210)
        self.write(f"Score: {self.score}/50", False, "left", ("Console", 15, "normal"))

    def increment_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}/50", False, "left", ("Console", 15, "normal"))