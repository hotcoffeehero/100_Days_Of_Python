import random

guess = input("Heads or Tails?").lower()

if guess == 'heads' or guess == 'tails':

  coinNumber = random.randint(0, 1)

  if coinNumber == 0:
    coinFace = 'heads'
  else:
    coinFace = 'tails'


  if coinNumber == 0 and guess == 'heads':
    print(f"You win! Dice said {coinFace}")

  elif coinNumber == 0 and guess == 'tails':
    print(f"You Lose. Dice said {coinFace}")

  elif coinNumber == 1 and guess == 'tails':
    print(f"You win! Dice said {coinFace}")

  else:
    print(f"You Lose. Dice said {coinFace}")

else:
  print(f"You said '{guess}'. Please hit 'Run' and try again.")

# ==================================================================
# HERE IS WHERE I WENT WRONG AT THE END OF 12/02/202

# import random

# guess = input("Heads or Tails?\n").lower()

# if guess == 'heads' or guess == 'tails':
#   if guess == 'heads':
#     guessStr = 'heads'
#     guessInt = 0
#   else:
#     guessStr = 'tails'
#     guessInt = 1

#     print(f"You said {guess}!")

#     print(input("Flip a coin! (Press Enter, lol.)\n"))

#     ran = random.randint(0,1)

#     if ran == guessInt:
#         print(f"The coin said {guessStr}! You win!")
#     else:
#         print(f"The coin said {guessStr}! You lose!")

# else:
#   print(f"You said {guess}. Click Run and try again. Goodbye. Please take this seriously next time.")