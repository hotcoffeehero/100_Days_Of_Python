import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


input("Let's play Rock Paper Scissors!\n")
guess = input("Type 'rock', 'paper' or 'scissors' and hit ENTER.\n").lower()

rps = ['rock','paper','scissors']
randomInt = random.randint(0, 2) 
compGuess = rps[randomInt]


if guess == 'rock' or guess == 'paper' or guess == 'scissors':
  if guess != compGuess:
    if compGuess == 'rock':
      if guess == 'paper':
        print("You Win!")
        print(f"You chose '{guess}':")
        print(paper)
        print(f"The Computer chose '{compGuess}'")
        print(rock)
      else: 
        print("You Lose!")
        print(f"You chose '{guess}':")
        print(scissors)
        print(f"The Computer chose '{compGuess}'")
        print(rock)
    elif compGuess == 'paper':
      if guess == 'rock':
        print("You Lose!")
        print(f"You chose '{guess}':")
        print(rock)
        print(f"The Computer chose '{compGuess}'")
        print(paper)
      else:
        print("You win!")
        print(f"You chose '{guess}':")
        print(scissors)
        print(f"The Computer chose '{compGuess}'")
        print(paper)
    else:
      if guess == 'rock':
        print("You Win!")
        print(f"You chose '{guess}':")
        print(rock)
        print(f"The Computer chose '{compGuess}'")
        print(scissors)
      else:
        print('You Lose!')
        print(f"You chose '{guess}':")
        print(paper)
        print(f"The Computer chose: '{compGuess}'")
        print(scissors)
  else:
    print(f"Try Again. The computer also chose '{guess}'.")
else:
  print("Giant Spelling Error. Try Agane.")