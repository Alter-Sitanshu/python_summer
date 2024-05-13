import turtle as t
import random
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SPEED = 10
class Snake:
    def __init__(self):
        self.state = []
        self.create_snake()
        self.head = self.state[0]
    def create_snake(self):
        for state in range(3):
            instance = t.Turtle("square")
            instance.color("white")
            instance.penup()
            instance.goto(-20*state,0)
            instance.speed(SPEED)
            self.state.append(instance)
    def move(self):
        for states in range(len(self.state)-1,0,-1):
            posx = self.state[states-1].xcor()
            posy = self.state[states-1].ycor()
            self.state[states].goto(posx,posy)
        self.head.forward(MOVE)
    def up(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(LEFT)
    def elongate(self):
        instance = t.Turtle("square")
        instance.color("white")
        instance.penup()
        instance.goto(self.state[-1].position())
        instance.speed(SPEED)
        self.state.append(instance)

class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-50,280)
        self.score = 0
        score_str = "Score : {}".format(self.score)
        self.write(score_str, font=("Verdana",15, "normal"))
    def refresh(self):
        self.clear()
        score_str = "Score : {}".format(self.score)
        self.write(score_str, font=("Verdana",15, "normal"))

    def game_over(self):
        self.goto(-50,0)
        self.write("Game Over", font=("Verdana",15, "normal"))

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.random_food()
    def random_food(self):
        xcord = random.randint(-270,270)
        ycord = random.randint(-270,270)
        self.goto(xcord,ycord)
        self.dot(10,"blue")


        
