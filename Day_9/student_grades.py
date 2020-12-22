student_scores = {
  "Casey": 81,
  "Stokely": 78,
  "Zeke": 99, 
  "MaryBeth": 74,
  "Stan": 62,
}

student_grades = {}

for student in student_scores:
  grade = ''
  score = student_scores[student]
  if score > 90:
    grade = 'Outstanding'
  elif score > 80:
    grade = 'Exceeds Expectations'
  elif score > 70:
    grade = 'Acceptable'
  else:
    grade = 'Fail'
  student_grades[student] = grade

print(student_grades)



