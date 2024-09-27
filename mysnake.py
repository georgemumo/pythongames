import random
import turtle
import time
from turtle import Screen

# from snake import delay

delaid = 0.3
wn = Screen()
wn.setup(width= 500, height= 500)
wn.bgcolor("green")
wn.title("Snake")
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.penup()
head.speed(1)
head.color('white')
head.goto(0, 0)
head.direction = 'stop'
pen = turtle.Turtle()
pen.penup()
pen.color('black')
pen.speed(1)
pen.hideturtle()
pen.goto(0,230)
pen.write('Score:0              High score: 0',align='center',font=('Courier',14,'normal'))

score = 0
high_score = 0
body= []

food = turtle.Turtle()
food.shape("circle")
food.penup()
food.color('red')
food.goto(98, 100)




def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'



def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


wn.listen()
wn.onkey(go_up, 'Up')
wn.onkey(go_down, 'Down')
wn.onkey(go_left, 'Left')
wn.onkey(go_right, 'Right')


while True:
    wn.update()

    time.sleep(delaid)
    if head.xcor() > 235 or head.xcor() < -235 or head.ycor() > 235 or head.ycor() < -235:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for size in body:
            size.goto(1000, 1000)
        body.clear()
        score = 0
        pen.clear()
        pen.write("Score: {} Highscore {}".format(score, high_score), align='center', font=('Courier', 14, 'normal'))

    if head.distance(food) < 20:
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        food.goto(x, y)


        new_size = turtle.Turtle()
        new_size.shape("square")
        new_size.speed(1)
        new_size.penup()
        new_size.color('black')
        body.append(new_size)
        delaid -= 0.01

        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} Highscore {}".format(score, high_score),align='center',font=('Courier',14,'normal'))
    # increase size
    for you in range(len(body) -1, 0, -1):
        x = body[you -1 ].xcor()
        y = body[you -1 ].ycor()
        body[you].goto(x, y)
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)



    move()
    for size in body:
        if size.distance(head) < 20:
            time.sleep(1.5)
            head.goto(0, 0)
            head.direction = 'stop'

            for size in body:
                size.goto(1000,1000)
            size.clear()
            score = 0
            pen.clear()
            pen.write("Score: {} Highscore {}".format(score, high_score), align='center',
                      font=('Courier', 14, 'normal'))


wn.mainloop()