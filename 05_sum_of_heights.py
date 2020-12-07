#Original Solution! No starter Code!
strInput = input("Input a list of student heights separated by a space:\n").split()
loopCount = 0
sumInt = 0
heightList = []
for index in strInput:
  index = int(index)
  loopCount += 1
  sumInt += index
  avgHeight = sumInt/loopCount
  heightList.append(avgHeight)
  result = int(heightList[-1])

print(f"The average height of everyone in the class is {result} cm.")

#hotcoffeehero