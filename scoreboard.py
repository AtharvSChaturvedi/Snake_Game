from turtle import Turtle

class ScoreBoared(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def update_score(self):
         self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()