from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            y_coord = random.randint(-240, 240)
            car.goto(280, y_coord)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def next_level(self):
        self.STARTING_MOVE_DISTANCE = self.STARTING_MOVE_DISTANCE + 10
        print(self.STARTING_MOVE_DISTANCE)
