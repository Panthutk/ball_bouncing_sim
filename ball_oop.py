import turtle
import random


class Ball:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

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

    def move_circle(self, i, canvas_width, canvas_height, ball_radius):
        self.xpos[i] += self.vx[i]
        self.ypos[i] += self.vy[i]

        # Reflect from walls
        if abs(self.xpos[i] + self.vx[i]) > (canvas_width - ball_radius):
            self.vx[i] = -self.vx[i]

        if abs(self.ypos[i] + self.vy[i]) > (canvas_height - ball_radius):
            self.vy[i] = -self.vy[i]

        # Check for collisions with other balls
        for j in range(len(self.xpos)):
            if i != j:
                distance = ((self.xpos[i] - self.xpos[j]) ** 2 +
                            (self.ypos[i] - self.ypos[j]) ** 2) ** 0.5
                min_distance = 2 * ball_radius
                if distance < min_distance:
                    # If collision, adjust ball position randomly
                    self.xpos[i] = random.randint(
                        -1 * canvas_width + ball_radius, canvas_width - ball_radius)
                    self.ypos[i] = random.randint(
                        -1 * canvas_height + ball_radius, canvas_height - ball_radius)

        # Reflect from walls
        if abs(self.xpos[i] + self.vx[i]) > (canvas_width - ball_radius):
            self.vx[i] = -self.vx[i]

        if abs(self.ypos[i] + self.vy[i]) > (canvas_height - ball_radius):
            self.vy[i] = -self.vy[i]

    def initializing(self, canvas_width, canvas_height, ball_radius, num_balls):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls
        for i in range(self.num_balls):
            self.xpos.append(random.randint(
                -1 * self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.randint(
                -1 * self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(random.randint(1, 10))
            self.vy.append(random.randint(1, 10))
            self.ball_color.append(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
