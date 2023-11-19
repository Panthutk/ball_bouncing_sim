import turtle
import random
from ball_oop import Ball

balls = Ball()

turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

# Prompt the user to enter the number of balls
num_balls = 5

# Initialize balls with random positions
balls.initializing(canvas_width, canvas_height, ball_radius, num_balls)
turtle.done()
while True:
    turtle.clear()
    for i in range(num_balls):
        balls.draw_circle(
            balls.ball_color[i], ball_radius, balls.xpos[i], balls.ypos[i])
        balls.move_circle(i, canvas_width, canvas_height, ball_radius)
    turtle.update()

# Hold the window; close it by clicking the window close 'x' mark
