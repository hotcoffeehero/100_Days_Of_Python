
def prime_checker(num):
  prime = True

  for i in range(2, num):
    if num % i == 0:
      prime = False
  if prime:
    print("It's prime!")
  else:
    print("It's not prime")

n = int(input("Check this number: "))
prime_checker(num=n)

