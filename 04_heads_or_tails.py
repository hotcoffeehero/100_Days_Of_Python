import random

guess = input("Heads or Tails?\n").lower()


if guess == 'heads':
  guessStr = 'heads'
  guessInt = 0
else:
  guessStr = 'tails'
  guessInt = 1

print(f"You said {guess}!")

print(input("Flip a coin!\n"))

ran = random.randint(0,1)

if ran == guessInt:
  print(f"The coin said {guessStr}! You win!")
else:
  print(f"The coin said {guessStr}! You lose!")