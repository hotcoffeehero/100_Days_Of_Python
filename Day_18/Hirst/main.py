import turtle as turt_mod
import random

import colorgram

# colors = colorgram.extract('sistine_chapel.jpg', 30)
#
# print(colors)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turt_mod.colormode(255)
sedge = turt_mod.Turtle()
sedge.speed('fastest')
colors = [(227, 220, 206), (117, 94, 68), (182, 160, 131), (217, 222, 218), (61, 37, 23), (212, 217, 223), (149, 133, 93), (213, 197, 156), (144, 155, 171), (84, 66, 35), (148, 169, 150), (227, 218, 220), (116, 79, 83), (64, 28, 31), (174, 148, 150), (88, 100, 89), (92, 49, 43), (94, 46, 50), (97, 108, 121), (30, 38, 31), (152, 116, 111), (212, 183, 176), (28, 29, 34), (152, 113, 117), (109, 125, 155), (206, 183, 186), (178, 200, 180), (182, 190, 206), (56, 69, 56), (119, 136, 116)]


def starting_position():
    sedge.setheading(225)
    sedge.penup()
    sedge.forward(500)
    sedge.setheading(0)


def new_row():
    sedge.penup()
    sedge.left(90)
    sedge.forward(50)
    sedge.left(90)
    sedge.forward(750)
    sedge.right(180)


def paint():
    for _ in range(15):
        sedge.dot(20, random.choice(colors))
        sedge.penup()
        sedge.forward(50)


def hirst():
    paint()
    new_row()


def go(num):
    starting_position()
    for _ in range(num):
        hirst()

go(15)











screen = turt_mod.Screen()
screen.exitonclick()