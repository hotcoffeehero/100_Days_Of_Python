print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is yo crush's name? \n").lower()

bigString = name1 + name2

T = bigString.count("t")
R = bigString.count("r")
U = bigString.count("u")
E = bigString.count("e")
L = bigString.count("l")
O = bigString.count("o")
V = bigString.count("v")
E = bigString.count("e")

loveScore = T+R+U+E+L+O+V+E

if loveScore > 90 or loveScore < 10: 
  print(f"Your Love Score is: {loveScore}. You are like coke and mentos.")
elif loveScore > 40 and loveScore < 60:
  print(f"Your Love Score is: {loveScore}. You are okay together.")
else: 
  print(f"Your Love Score is: {loveScore}. Make what you will of that.")

