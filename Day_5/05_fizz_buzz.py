
input("Let's play Fizz Buzz. Press ENTER")

for index in range(1, 101):
  if index % 3 == 0 and index % 5 == 0:
    print("Fizz Buzz")
  elif index % 3 == 0:
    print("Fizz")
  elif index % 5 == 0:
    print("Buzz")
  else:
    print(index)