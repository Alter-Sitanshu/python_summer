import turtle as t
import random
MOVE= 30
BALL_SPEED = 25


class Paddle(t.Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if side == 'right':
            self.side = 1
        else:
            self.side = -1
        self.goto(self.side*360,0)
    def move_up(self):
        if self.ycor() <=220:
            self.goto(self.side*360, MOVE+self.ycor())
    def move_down(self):
        if self.ycor() >= -220:
            self.goto(self.side*360, -1*MOVE+self.ycor())
        
def divide_line():
    divider = t.Turtle()
    divider.color('white')
    divider.hideturtle()
    divider.penup()
    divider.goto(0, -300)
    divider.setheading(90)
    divider.width(5)
    while divider.ycor() <= 300:
        divider.pendown()
        divider.forward(10)
        divider.penup()
        divider.forward(10)

class ScoreBoard(t.Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score = 0
        if side == 'right':
            self.side = 1
        else:
            self.side = -1
        self.goto(self.side*185, 280)
        self.write('Score', font=("Verdana",15, "normal"))
        self.goto(self.side*185 + 20, 260)
        self.write(f'{self.score}', font=("Verdana",15, "normal"))

    def refresh(self):
        self.clear()
        self.goto(self.side*185, 280)
        self.write('Score', font=("Verdana",15, "normal"))
        self.goto(self.side*185 + 20, 260)
        self.write(f'{self.score}', font=("Verdana",15, "normal"))

    def game_over(self):
        self.goto(-50,0)
        self.write("Game Over", font=("Verdana",15, "normal"))

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.rng = [range(-30,30),range(150,220)]
        self.start()
    def start(self):
        self.home()
        self.setheading(random.choice(random.choice(self.rng)))
    def move(self):
        self.forward(BALL_SPEED)
    def out_bounds(self, side):
        self.home()
        if side == 'right':
            self.setheading(random.choice(self.rng[1]))
        else:
            self.setheading(random.choice(self.rng[0]))