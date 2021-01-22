from turtle import Turtle, Screen
import random

screen = Screen()
sedge = Turtle()
screen.colormode(255)
sedge.shape('turtle')
sedge.pensize(2)
sedge.speed(100)


def ran_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


def morph():
    sedge.pencolor(ran_color())
    sedge.fillcolor(ran_color())


def sedge_turn(num):
    return sedge.right(num)

# My original solution
# for _ in range(72):
#     sedge.circle(150)
#     sedge_turn(5)
#     morph()


def spino_graph(space, radius):
    for _ in range(int(360/space)):
        morph()
        sedge.circle(radius)
        sedge_turn(space)


spino_graph(15, 250)

screen.exitonclick()