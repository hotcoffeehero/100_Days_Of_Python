import random

names = input("Party of how many? Give me a list of names, please.\n")

if names.find(", ") != -1:

  namesStr = names.split(", ")
  namesInt= len(names.split(", "))
  
  randomCard = random.randint((namesInt - namesInt), (namesInt - 1))

  shortStraw = namesStr[randomCard]

  print(f"It looks like {shortStraw} will be paying the bill tonight.")

else:
  print("Please separate the names with commas and spaces. For example: 'Bateman, Halberstran, Lewis, VanPatten, Allen, etc.'")