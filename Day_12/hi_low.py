import random
EASY = 10
HARD = 5

def ran_number():
  numbers = []
  correct_answer = 0
  for n in range(1, 101):
    numbers.append(n)
  correct_answer = random.choice(numbers)
  return correct_answer


def guess_check(guess, answer, turns):
  
  if guess == answer:
    print(f"That's it! It was {answer}.")
    return 
  elif guess > answer:
    print("Too High. Try Again.")
    return turns - 1
  else:
    print("Too Low. Try Again.")
    return turns - 1

def set_difficulty():
  level = input("Hard Mode or Soft Mode? 'h' or 's'? \n")
  if level == 'h':
    return HARD
  elif level == 's':
    return EASY
  else:
    return EASY


def play_game():
  answer = ran_number()
  guess = 0
  print('Welcome to Hi-Low. \n')
  turns = set_difficulty()
  print("I'm thinking of a number between 1 and 100. \n")
  print(f"Psssst. Answer: {answer}")
  
  while guess != answer:
    print(f"{turns} guesses left")
    guess = int(input('Guess a number: '))
    
    turns = guess_check(guess, answer, turns)
    if turns == 0:
      print('You have no turns left. Game over dude.')
      return
      
    elif guess != answer:
      print('Guess Again, bruh.')
   
    

play_game()