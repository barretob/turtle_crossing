import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# car and player objects
cars = CarManager()
player_1 = Player()
scoreboard_1 = Scoreboard()
scoreboard_1.display_score()

# keystrokes
screen.onkey(player_1.move_up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
#   speed of cars
    time.sleep(0.1)
#   creates cars and moves them
    cars.create_car()
    cars.move_car()

#   car collision detection
    for part in cars.all_cars:
        if player_1.distance(part) < 20:
            scoreboard_1.game_over()
            game_is_on = False
#   winner
    if player_1.ycor() > 250:
        scoreboard_1.game_winner()
        scoreboard_1.add_point()
        cars.next_level()
        player_1.reset()


screen.exitonclick()

