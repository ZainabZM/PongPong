# Simple Pong Game in Python 3
# By @zaindes on discord

import turtle # Library for creating graphics

# Window 
window = turtle.Screen()
window.title("PongPong by @zaindes")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # Stops the window from updating, speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.pencolor("lime")
paddle_a.fillcolor("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(100)
paddle_b.shape("square")
paddle_b.pencolor("lime")
paddle_b.fillcolor("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(100)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.8 # Moves the ball by 2 pixels to the right
ball.dy = -0.8 # Moves the ball down by 2 pixels 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # To prevent drawing a line when the pen moves
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0 | Player B : 0", align="center", font=("Courier", 24, "normal"))



# Functions
    # Paddles
def paddle_a_up():
    y = paddle_a.ycor() # Returns the y coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # Returns the y coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() # Returns the y coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # Returns the y coordinate
    y -= 20
    paddle_b.sety(y)

    # Ball



# Keyboard binding
window.listen() # Listens for keyboard inputs
window.onkeypress(paddle_a_up, "Up") # When user presses Up, call the function
window.onkeypress(paddle_a_down, "Down") # When user presses Down, call the function
window.onkeypress(paddle_b_up, "a") 
window.onkeypress(paddle_b_down, "q")
# Main game loop
while True:
    window.update() # Every time the loop runs it updates the screen

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
        score_a += 1
        pen.clear()
        pen.write("Player A : {} | Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {} | Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1