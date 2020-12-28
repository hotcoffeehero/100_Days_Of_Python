def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print("Welcome, I am Calculator.")

  num1 = float(input('What is the first number? '))

  for symbol in operations:
    print(symbol)
  game_play = True

  while game_play:

    op_symbol = input('what kind of calculation? ')

    num2 = float(input('What is the next number? '))


    calc_function = operations[op_symbol]

    answer = calc_function(num1, num2)

    print(f"{num1} {op_symbol} {num2} is {answer}")

    if input(f"Perform another operation with {answer}? y or n?") == 'y':
      num1 = answer
    else:
      game_play = False
      calculator()

calculator()