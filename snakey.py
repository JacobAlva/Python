import turtle
import time
import random

delay = 0.15  # Reduced initial game start speed
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("lightblue")  # Colorful background
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Initialize the segments list
segments = []

# Pen to write the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Functions
def show_message(message, submessage):
    """Displays a message on the screen."""
    pen.clear()
    pen.goto(0, 0)
    pen.write(message, align="center", font=("Courier", 36, "normal"))
    pen.goto(0, -40)
    pen.write(submessage, align="center", font=("Courier", 24, "normal"))
    time.sleep(2)
    pen.clear()

def update_score():
    """Updates the score display."""
    pen.clear()
    pen.goto(0, 260)
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def start_game():
    global delay, score, high_score, segments
    delay = 0.15
    score = 0
    high_score = max(high_score, score)

    # Reset the snake's head
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    segments = []

    # Move the food to a random spot
    food.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Start the main game loop
    main_game_loop()

def main_game_loop():
    global score, high_score, segments, delay
    while True:
        wn.update()

        # Check for a collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            show_message("Game Over", f"Score: {score}  High Score: {high_score}")
            start_game()
            return

        # Check for a collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Shorten the delay
            delay -= 0.001

            # Increase the score
            score += 1

            if score > high_score:
                high_score = score

            update_score()

        # Move the end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with the body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                show_message("Game Over", f"Score: {score}  High Score: {high_score}")
                start_game()
                return

        time.sleep(delay)

# Show start message
show_message("Welcome to Snake Game", "Press Enter or Space to Start")

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(start_game, "Return")
wn.onkeypress(start_game, "space")

wn.mainloop()
