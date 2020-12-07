#Original Code! 
input("Do you want to know the sum of even numbers between 1 and 100? Hit ENTER.\n")

sum = 0

for i in range(1, 101):
  if i % 2 == 0:
    sum += i

print(f"It's {sum}.")