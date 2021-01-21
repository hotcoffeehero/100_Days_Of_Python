from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("teal")


def square():
    for _ in range(4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(90)

square()



timmy_the_turtle.left(45)


def dash_line():
    for _ in range(7):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()


dash_line()



import heroes as h
hero_1 = h.gen()
print(hero_1)


screen = Screen()
screen.exitonclick()
