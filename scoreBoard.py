from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.showScore()

    def showScore(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level {self.level}", align="left", font=("Courier", 12, "bold"))

    def upgrade(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=("Courier", 14, "bold"))
