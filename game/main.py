import time
from turtle import Screen
from capstone import Capstone
from car_block import CarManager
from scoreboard import Scoreboard

FINISH_LINE = 260
CONTROLLER = "Up"

game_is_on = True
my_screen = Screen()
my_screen.title("Capstone")
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

turtle = Capstone()
car_manager = CarManager()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(turtle.upward, CONTROLLER)

while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False

    if turtle.ycor() > FINISH_LINE:
        scoreboard.level += 1
        car_manager.increase_speed()
        turtle.reset()
        scoreboard.display_score()


my_screen.exitonclick()