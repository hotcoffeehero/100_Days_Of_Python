
#Original Code! No Starter Code!

strInput = input("Type a list of scores separated by a space. Don't worry about commas.\n").split()

highScore = 0

for index in strInput:
  index = int(index)
  if index > highScore:
    highScore = index

result = highScore
  
print(f"It looks like the high score was {result}.")