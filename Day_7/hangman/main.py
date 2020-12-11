from replit import clear
import random
import stages
import word_list

print(stages.logo)
print('''


''')

game_play = True
word = word_list.word
word_len = len(word)

display = []

lives = 6

#print the word to be guessed
for char in word:
  display += '_'
print(' '.join(display))

while game_play == True:
  guess = input("Guess a letter: \n")
  clear()
  

  #check if the letter is correct or not
  for index in range(word_len):
    letter = word[index]
    if letter == guess:
      display[index] = letter
  print(' '.join(display))

  #tell the player they guessed wrong
  if guess not in word:
    lives -= 1
    print(stages.stages[lives])

  #end the game: WIN
  if "_" not in display:
    game_play = False
    print("YOU WIN!!\n")
  
  #end the game: LOSE
  if lives == 0:
    game_play = False
    print("YOU LOSE\n")
    print(f"The word was {word}")





  
  