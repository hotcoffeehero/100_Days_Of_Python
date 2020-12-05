#This is 100% original code - Clinton A!

#Banker Roulette is something Wall Street types do where after dinner they all toss their bank cards onto a tray and the waiter picks one randomly. 

import random 

input("Let's play Banker Roulette!! ")
names = input("Type a list of everyone in your group.\n \n")

if names.find(", ") != -1:

  names = list(enumerate(names.split(", ")))

  randomCard = random.randint((len(names) - len(names)), (len(names)-1))

  shortStraw = names[randomCard][1]

  print(f"It looks like {names[randomCard][1]} will be settling the bill tonight. Thank you for playing. And dining. Goodbye. \n")

else:
  print("Separate the names with commas like this: Halberstran, Bateman, VanPatten, etc.") 

# My solution:

# 1. split the string input into an array
# 2. use enumerate() to tuplify each index of that array because I wanted a paired index and stringValue
# 3. I used List() to turn the 'names' variable into an array of tuples.
# 4. Now I can access all of that data using the Array[][] syntax we all know and love without having to create a new variable for each step of the process. 

# I also added the initial statement, anticipating the user might not comma separate the names. 

# Is this good? Thoughts?

# -hotcoffeeheeeeeeeeeeeeeeero