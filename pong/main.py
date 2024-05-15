import turtle as t
import time
import game
MOVE = 20
def gameover():
    global gameOver
    gameOver = True

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)

r_paddle = game.Paddle('right')
l_paddle = game.Paddle('left')

r_score = game.ScoreBoard('right')
l_score = game.ScoreBoard('left')

gameOver = False
ball = game.Ball()
game.divide_line()
while not gameOver:
    screen.update()
    time.sleep(ball.delay)
    ball.move()

    #bounce logic
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        prev_heading = ball.heading()
        ball.setheading(360-prev_heading)
    if (ball.distance(r_paddle)<40) and (ball.xcor()>320):
        prev_heading = ball.heading()
        ball.setheading(540-prev_heading)
        ball.delay *= 0.9
    if (ball.distance(l_paddle)<40) and (ball.xcor()<-320):
        prev_heading = ball.heading()
        ball.setheading(540-prev_heading)
        ball.delay *= 0.9
    if ball.xcor() > 390:
        l_score.score +=1
        l_score.refresh()
        ball.out_bounds('right')
    if ball.xcor() < -390:
        r_score.score +=1
        r_score.refresh()
        ball.out_bounds('left')
    screen.onkeypress(r_paddle.move_up, 'Up')
    screen.onkeypress(r_paddle.move_down, 'Down')

    screen.onkeypress(l_paddle.move_up, 'w')
    screen.onkeypress(l_paddle.move_down, 's')

    screen.onkeypress(gameover,'q')
screen.exitonclick()