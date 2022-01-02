from turtle import Turtle
from player import Player

import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_cor= random.randint(-240, 250)
            new_car.goto(300, y_cor)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.current_speed)

    def update_speed(self):
        self.current_speed += MOVE_INCREMENT
