from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        file=open("highscore.txt")
        content=file.read()
        self.highscore=int(content)
        file.close()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}     High Score:{self.highscore}", align="center", font=("Arial", 18, "normal"))


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            file=open("highscore.txt",mode="w")
            file.write(str(self.highscore))
            file.close()
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))


