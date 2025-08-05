from turtle import Turtle
STARTING_POSITION = (0,-280)

class Capstone(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def upward(self):
        self.forward(20)

    def reset(self):
        self.goto(STARTING_POSITION)