from turtle import Turtle, Screen

sedge = Turtle()
screen = Screen()


def march():
    sedge.forward(10)

def right():
    sedge.right(10)

def left():
    sedge.left(10)

def reverse():
    sedge.right(180)

def clear():
    sedge.clear()
    sedge.penup()
    sedge.home()
    sedge.pendown()



screen.listen()
screen.onkey(key="Up", fun=march)
screen.onkey(key="Down", fun=reverse)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()