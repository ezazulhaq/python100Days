from turtle import Turtle
import os
data_file_path = os.path.join(os.path.dirname(__file__), "data.txt")
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(data_file_path) as data:
            self.hight_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hight_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            with open(data_file_path, mode="w") as data:
                data.write(f"{self.hight_score}")

        self.score = 0
        self.update_scoreboard()
