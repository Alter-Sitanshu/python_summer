import turtle as t
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 3
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10

class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(400, random.randint(-230,230))
    def car_move(self):
        new_xcor = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_xcor, self.ycor())

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-380,270)
        self.level = 1
        score_str = "Level : {}".format(self.level)
        self.write(score_str, font=("Verdana",15, "normal"))
    def refresh(self):
        global STARTING_MOVE_DISTANCE
        self.clear()
        score_str = "Level : {}".format(self.level)
        self.write(score_str, font=("Verdana",15, "normal"))
        STARTING_MOVE_DISTANCE += MOVE_DISTANCE

    def game_over(self):
        self.goto(-50,0)
        self.write("Game Over", font=("Verdana",15, "normal"))


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.color(random.choice(COLORS))
    
    def move_up(self):
        new_ycor = self.ycor() + MOVE_INCREMENT
        self.goto(self.xcor(), new_ycor)
    def level_up(self):
        self.goto(STARTING_POSITION)
