#100% Original Code!!
import random

password = ''
bigList = []

alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

alphaNum = input("How many letters would you like?\n")
alphaNum = int(alphaNum)

numNum = input("How many numbers would you like?\n")
numNum = int(numNum)

symNum = input("How many symbols would you like?\n")
symNum = int(symNum)

#Here we will store the random values of letters, numbers etc

#Get random letters
for index in range(0, (alphaNum + 1)):
  ranAlpha = random.randint(0, (len(alphas) -1))
  index = alphas[ranAlpha]
  bigList.append(index)

#Get random numbers
for index in range(0, (numNum + 1)):
  ranNumber = random.randint(0, (len(numbers)-1))
  index = numbers[ranNumber]
  bigList.append(index)

#Get random symbols
for index in range(0, (symNum +1)):
  ranSymbol = random.randint(0, (len(symbols)-1))
  index = symbols[ranSymbol]
  bigList.append(index)


#Now we piece them together
for index in bigList:
  ranVal = random.randint(0, (len(bigList)-1))
  index = str(bigList[ranVal])
  password += index

print(f"Your new password is: {password}")