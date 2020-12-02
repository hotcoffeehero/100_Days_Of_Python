bill = float(input("How much was your bill?"))
tip = 1+ .01*float(input("How much would you like to tip? 10%, 12% or 15%"))
people  = int(input("How many people are with you?"))
total = round((bill/people)*tip, 2)
print(f"Each person should pay ${total}")

