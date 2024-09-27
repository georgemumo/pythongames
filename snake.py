import turtle
import random
import time
from turtle import Screen

delay = 0.3
# snake
wn = Screen()
wn.setup(width=600, height=500)
wn.bgcolor('green')
wn.tracer(0)
wn.title("Snake game")
# head
head = turtle.Turtle()
head.speed(2)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'up'

#food
food = turtle.Turtle()

food.shape('circle')
food.color('red')
food.penup()
food.goto(45, 180)

# segments
segments = []
# directions
def go_up():
    if head.direction != 'down':

        head.direction = 'up'
def go_down():
    if head.direction != 'up':

        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'

# function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


wn.listen()
wn.onkey(go_up, 'Up')
wn.onkey(go_down, 'Down')
wn.onkey(go_right, 'Right')
wn.onkey(go_left, 'Left')
# mainloop
while True:
    wn.update()

    # collision with bounderies
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor() > 290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()




    time.sleep(delay)
    # collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-240, 240)
        food.goto(x, y)

#     enlarging body
        new_segment = turtle.Turtle()
        new_segment.speed(2)
        new_segment.shape('square')
        new_segment.color('yellow')
        new_segment.penup()
        segments.append(new_segment)

#         attaching segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
# collision with segments
    for segment in segments:
         if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()


wn.mainloop()