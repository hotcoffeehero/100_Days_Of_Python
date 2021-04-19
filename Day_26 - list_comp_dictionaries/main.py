import random
names = ['Adrian', 'Brad', 'Coraline', 'Donald', 'Edward', 'Fulton', 'Gertrude', 'Hugh', 'Iris']


student_scores = {student:random.randint(1, 100) for student in names }

print(student_scores)

passing_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passing_students)