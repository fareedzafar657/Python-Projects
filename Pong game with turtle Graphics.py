import turtle
import time
import winsound

window_of_game = turtle.Screen()  # New window interface for game
window_of_game.title("Pong game by Fareed Zafar")  # Title of game on top bar
window_of_game.bgcolor(
    "black")  # Background color     #if don't have a screen then window_of_game.getscreen().bgcolor("red")
window_of_game.setup(width=800, height=600)  # window interface size
window_of_game.tracer(0)  # Frame rate? not sure, without it the game will run slower

# Score variables
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()  # New Pointer for drawing
paddle_a.speed(0)  # Max speed of drawing the shapes
paddle_a.shape("square")  # Shape of the graphic
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=10, stretch_len=1)  # Size of the graphics
paddle_a.penup()  # picks up the pointer so as not to draw lines whereever it goes
paddle_a.goto(-350, 0)  # position of the pointer after lifting it  # first value is x and second is y (x, y)

# Paddle B
paddle_b = turtle.Turtle()  # New Pointer for drawing
paddle_b.speed(0)  # Max speed of drawing the shapes
paddle_b.shape("square")  # Shape of the graphic
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=10, stretch_len=1)  # Size of the graphics
paddle_b.penup()  # picks up the pointer so as not to draw lines whereever it goes
paddle_b.goto(350, 0)  # position of the pointer after lifting it  # first value is x and second is y (x, y)

# Ball
ball = turtle.Turtle()  # New Pointer for drawing
ball.speed(0)  # Max speed of drawing the shapes
ball.shape("circle")  # Shape of the graphic
ball.color("white")
ball.penup()  # picks up the pointer so as not to draw lines whereever it goes
ball.goto(0, 0)  # position of the pointer after lifting it  # first value is x and second is y (x, y)
ball.dx = 0.4  # moves given pixels in x cor
ball.dy = 0.4  # moves given pixels in y cor

# Pen
pen = turtle.Turtle()
pen.speed(0)  # Max animation speed
pen.hideturtle()  # hides turtle pen mark
pen.color("white")
pen.penup()  # picks up the pen so as not to draw lines on its way to next positioned command line
pen.goto(0, 250)
pen.write(f"Player A: 0       Player B: 0", align="center", font=("Press Start 2P", 15, "normal"))


# updated printed score are in while loop

# Function for animation
def paddle_a_up():  # paddle a moves up 20 pixels once move
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():  # paddle a moves down 20 pixels once move
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():  # paddle b moves up 20 pixels once move
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():  # paddle b moves down 20 pixels once move
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keybinding
window_of_game.listen()  # commanding the window to listen to the following function
window_of_game.onkeypress(paddle_a_up, "w")  # it does what its message says
window_of_game.onkeypress(paddle_a_down, "s")
window_of_game.onkeypress(paddle_b_up, "Up")
window_of_game.onkeypress(paddle_b_down, "Down")

# Main game loop         #Every game needs this loop
while True:
    window_of_game.update()  # while True loop runs continiuosly and every time it runs the game updates screen

    # ball movements
    ball.setx(ball.xcor() + ball.dx)  # continiously moves in xy-co-ordinates
    ball.sety(ball.ycor() + ball.dy)

    # Border of game for Ball
    if ball.ycor() > 290:  # if ball reaches the end of y cor then it will change its direction
        ball.sety(290)
        winsound.PlaySound("mixkit-small-hit-in-a-game-2072.wav", winsound.SND_ASYNC)
        ball.dy *= -1  # reverses direction

    if ball.ycor() < -290:  # if ball reaches the end of -y cor then it will change its direction
        ball.sety(-290)
        winsound.PlaySound("mixkit-small-hit-in-a-game-2072.wav", winsound.SND_ASYNC)
        ball.dy *= -1  # reverses direction

    if ball.xcor() > 390:  # if ball reaches end of x cor then it will go back to starting point center
        score_b += 1
        ball.goto(0, 0)  # center co-ordinates
        ball.dx *= -1  # it will start next round from opposite x-direction
        pen.clear()
        pen.write(f"Player A: {score_a}       Player B: {score_b}", align="center",
                  font=("Press Start 2P", 15, "normal"))

    if ball.xcor() < -390:  # same as above
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write(f"Player A: {score_a}       Player B: {score_b}", align="center",
                  font=("Press Start 2P", 15, "normal"))

    # Paddle and Ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 100 and ball.ycor() > paddle_b.ycor() - 100):
        winsound.PlaySound("mixkit-small-hit-in-a-game-2072.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 100 and ball.ycor() > paddle_a.ycor() - 100):  # 340 and 350 are set according to stretch which was 1 meaning 10 pixels and +100 and -100 are according to width which is width of the paddle 10.
        winsound.PlaySound("mixkit-small-hit-in-a-game-2072.wav", winsound.SND_ASYNC)
        ball.setx(-340)  # sends back the ball to -340 pixels which is center
        ball.dx *= -1  # reverses the direction
turtle.done()
