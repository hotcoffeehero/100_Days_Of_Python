
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / height ** 2

if BMI < 18.5:
  print(f"Your BMI is {BMI}. are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}. You are normal for your weight. ")
elif BMI < 30:
  print(f"Your BMI is {BMI}. You are slightly overweight. ")
elif BMI < 35:
  print(f"Your BMI is {BMI}. You are overweight. ")
else:
  print(f"Your BMI is {BMI}. You are clinically obese. ")
