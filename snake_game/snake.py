import turtle as t
import time
import classes

screen = t.Screen()
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=600,height=600)
    

snake = classes.Snake()
food = classes.Food()
score_board = classes.ScoreBoard()
screen.listen()
gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score_board.score += 1
        food.clear()
        snake.elongate()
        score_board.refresh()
        food.random_food()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        gameOn = False
        score_board.game_over()

    for states in snake.state[1:]:
        if snake.head.distance(states) < 15:
            gameOn = False
            score_board.game_over()

    screen.onkeypress(fun=snake.up,key="Up")
    screen.onkeypress(fun=snake.down,key="Down")
    screen.onkeypress(fun=snake.right,key="Right")
    screen.onkeypress(fun=snake.left,key="Left")


screen.exitonclick()