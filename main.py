from turtle import Turtle, Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(650, 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()# Add this to make snake grow
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # Skip the head (index 0)
        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()



screen.exitonclick()
































screen.exitonclick()