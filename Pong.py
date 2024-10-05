import turtle

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turns off the screen updates for better performance

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=6, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=6, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(40)  # Increase ball speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Set horizontal speed (increased for faster gameplay)
ball.dy = -0.2  # Set vertical speed (increased for faster gameplay)

# Function to move paddle_1 up
def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 30  # Adjust the paddle speed
        paddle_1.sety(y)

# Function to move paddle_1 down
def paddle_1_down():
    y = paddle_1.ycor()
    if y > -240:
        y -= 30  # Adjust the paddle speed
        paddle_1.sety(y)

# Function to move paddle_2 up
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30  # Adjust the paddle speed
        paddle_2.sety(y)

# Function to move paddle_2 down
def paddle_2_down():
    y = paddle_2.ycor()
    if y > -240:
        y -= 30  # Adjust the paddle speed
        paddle_2.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (350 > ball.xcor() > 340) and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
