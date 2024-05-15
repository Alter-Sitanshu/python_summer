import time
import turtle as t
import classes

def end_game():
    global game_is_on

    game_is_on = False


screen = t.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

tick_tick = 0
FREQ = 6
player = classes.Player()
score_board = classes.ScoreBoard()
car = classes.CarManager()
cars_list = [car]
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if tick_tick%FREQ == 0:
        new_car = classes.CarManager()
        cars_list.append(new_car)
    for cars in cars_list:
        if cars.xcor() < -400:
            cars_list.remove(cars)

        if cars.distance(player)<20:
            score_board.game_over()
            end_game()
        cars.car_move()
    if player.ycor() >290:
        score_board.level += 1
        score_board.refresh()
        player.level_up()

    screen.onkeypress(end_game, key='q')
    screen.onkeypress(player.move_up, key='Up')
    tick_tick += 1

screen.exitonclick()

