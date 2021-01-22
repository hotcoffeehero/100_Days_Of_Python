from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
sedge = Turtle()
sedge.shape('turtle')
sedge.pensize(15)
sedge.speed(10)


def ran_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


def morph():
    sedge.fillcolor(ran_color())
    sedge.pencolor(ran_color())


ran_march = random.randint(0, 100)
angle = random.randint(1, 360)

# def right():
#     angle = random.randint(0, 359)
#     return sedge.right(angle)
#
#
# def left():
#     angle = random.randint(0, 359)
#     return sedge.left(angle)


# def ran_turn():
#     turns = [left(), right()]
#     random_turn = random.choice(turns)
#     return random_turn

def sedge_turn():
    morph()
    return sedge.setheading(random.randint(1, 360))


def sedge_go():
    return sedge.forward(random.randint(0, 80))


for _ in range(10000):
    sedge_turn()
    sedge_go()

screen.exitonclick()