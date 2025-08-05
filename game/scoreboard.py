from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-220, 240)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)