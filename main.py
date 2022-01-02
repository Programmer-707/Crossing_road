from car_manager import CarManager
from player import  Player
from scoreBoard import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

screen.listen()
player = Player()
carManager = CarManager()
score = ScoreBoard()
screen.onkeypress(player.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    score.showScore()

    carManager.create_car()
    carManager.move()



    # when turtle across the road
    if player.isFinish():
        score.upgrade()
        carManager.update_speed()

    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()


screen.exitonclick()
