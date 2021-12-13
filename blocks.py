from turtle import Turtle


class Block(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()

    def delete(self):
        self.goto(1000, 1000)
