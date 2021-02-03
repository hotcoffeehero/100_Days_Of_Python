from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Place your bets', prompt='Who will win? Choose your color: ')
print(user_bet)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'teal', 'pink']

y_positions = [-100, -70, -40, -10, 20, 50, 80, 110]

constestants = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    constestants.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in constestants:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('You won!')
            else:
                print(f"The {winning_color} turtle won. And you suuuuuuuck. ")
        ran_forward = random.randint(0, 11)
        turtle.forward(ran_forward)





# for color in colors:
#     sedge = Turtle(shape='turtle')
#     sedge.color(colors[color])
#     sedge.penup()
#     x = -230
#     y = 100
#     sedge.goto(x=x, y=y - 30)


screen.exitonclick()