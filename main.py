from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Block
import time

# gui set up
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=800)
screen.title('Breakout Clone')
screen.tracer(1)

Block_locations = [(-350, 250), (-300, 250), (-250, 250), (-200, 250), (-150, 250), (-100, 250), (-50, 250), (0, 250),
                   (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (300, 250), (350, 250), (-350, 210),
                   (-300, 210), (-250, 210), (-200, 210), (-150, 210), (-100, 210), (-50, 210), (0, 210), (50, 210),
                   (100, 210), (150, 210), (200, 210), (250, 210), (300, 210), (350, 210), (-350, 170), (-300, 170),
                   (-250, 170), (-200, 170), (-150, 170), (-100, 170), (-50, 170), (0, 170), (50, 170), (100, 170),
                   (150, 170), (200, 170), (250, 170), (300, 170), (350, 170), (-350, 130), (-300, 130), (-250, 130),
                   (-200, 130), (-150, 130), (-100, 130), (-50, 130), (0, 130), (50, 130), (100, 130), (150, 130),
                   (200, 130), (250, 130), (300, 130), (350, 130), (-350, 90), (-300, 90), (-250, 90), (-200, 90),
                   (-150, 90), (-100, 90), (-50, 90), (0, 90), (50, 90), (100, 90), (150, 90), (200, 90), (250, 90),
                   (300, 90), (350, 90)]

# holder for all blocks and have blocks line up
blocks = []
for i in Block_locations:
    new_brick = Block()
    blocks.append(new_brick)
    new_brick.goto(i)

# create paddle, ball and tell gui to listen for user input
paddle = Paddle((0, -300))
ball = Ball()
screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')

# game play
keep_playing = True
while keep_playing:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # detect ball passing the paddle
    if ball.ycor() < -350:
        keep_playing = False

    # detect if ball touches wall
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.bounce_x()

    # detect if ball touches ceiling
    if ball.ycor() > 350:
        ball.bounce_y()

    # detect if ball touches paddle
    if ball.distance(paddle) < 50 and ball.ycor() > -320:
        ball.bounce_y()

    # detect if ball touches brick to "break"
    for i in blocks:
        if ball.distance(i) < 10:
            i.delete()
            ball.bounce_y()

screen.exitonclick()
