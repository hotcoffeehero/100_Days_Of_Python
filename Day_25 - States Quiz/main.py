import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Quiz')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_coords(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_coords)
# turtle.mainloop()

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='Name a state.').title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_coords = data[data.state == answer_state]
        t.goto(int(state_coords.x), int(state_coords.y))
        t.write(answer_state)