# from turtle import Turtle, Screen

# jimmy = Turtle()
# print(jimmy)
# jimmy.shape('turtle')
# jimmy.color('teal')
#
# jimmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column('Pokemon', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(table)

