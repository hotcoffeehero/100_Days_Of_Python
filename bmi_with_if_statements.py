
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / height ** 2

if BMI < 18.5:
  print("You are underweight.")
elif BMI < 25:
  print("You are normal for your weight. ")
elif BMI < 30:
  print("You are slightly overweight. ")
elif BMI < 35:
  print("You are overweight. ")
else:
  print("You are clinically obese. ")
