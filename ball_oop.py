import turtle
import random


class Ball:
    def __init__(self):
        self.turtle = turtle.Turtle()

    def draw_circle(self, color, size, x, y):
        self.turtle.penup()
        self.turtle.color(color)
        self.turtle.fillcolor(color)
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(size)
        self.turtle.end_fill()
        self.turtle.hideturtle()

    def move_circle(self, i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
            self.vx[i] = -self.vx[i]

        if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
            self.vy[i] = -self.vy[i]

    def initilizing(self, xpos, ypos, vx, vy, ball_color, canvas_width, canvas_height, ball_radius, num_balls):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = vx
        self.vy = vy
        self.ball_color = ball_color
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls
        for i in range(self.num_balls):
            self.xpos.append(random.randint(-1*self.canvas_width +
                                            self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.randint(-1*self.canvas_height +
                                            self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 0.01*self.canvas_width))
            self.vy.append(random.randint(1, 0.01*self.canvas_height))
            self.ball_color.append(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


my_ball = Ball()
