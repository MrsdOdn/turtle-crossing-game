import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
screen.title("Turtle Crossing")
player = Player()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "Up")

time_t = 0.1

game_is_on = True
while game_is_on:
    time.sleep(time_t)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.starting_pasition()
        scoreboard.increase_score()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()