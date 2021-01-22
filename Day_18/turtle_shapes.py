from turtle import Turtle, Screen
import random



def color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


screen = Screen()
sedge = Turtle()
screen.colormode(255)
sedge.fillcolor(color())
sedge.shape('turtle')


def morph():
    sedge.fillcolor(color())
    sedge.pencolor(color())
#
#
# print(color())
#
#

#
#
# sedge.left(180)
# sedge.penup()
# sedge.forward(100)
# sedge.right(90)
# sedge.forward(200)
# sedge.right(90)
# sedge.pendown()
#
# morph()
# sedge.forward(100)
# sedge.right(120)
# sedge.forward(100)
# sedge.right(120)
# sedge.forward(100)
# sedge.penup()
# sedge.forward(20)
# sedge.right(120)
# sedge.pendown()
#
# morph()
# sedge.forward(120)
# sedge.right(90)
# sedge.forward(120)
# sedge.right(90)
# sedge.forward(120)
# sedge.right(90)
# sedge.forward(120)
# sedge.penup()
# sedge.left(45)
# sedge.forward(20)
# sedge.right(135)
# sedge.pendown()
#
# # Pentagon
# morph()
# for _ in range(5):
#     sedge.forward(150)
#     sedge.right(72)
#

# sedge = Turtle()
# sedge.shape('turtle')
#

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        sedge.forward(50)
        sedge.right(angle)


for side in range(3, 20):
    morph()
    draw_shape(side)


screen = Screen()
screen.exitonclick()