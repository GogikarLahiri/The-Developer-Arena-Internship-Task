# Program to store and display student scores

# Empty dictionary to store scores
student_scores = {}

# Input number of students
n = int(input("Enter number of students: "))

# Store scores
for i in range(n):
    name = input("Enter student name: ")
    score = float(input("Enter score: "))
    student_scores[name] = score

# Display scores
print("\nStudent Scores:")
for student, score in student_scores.items():
    print(student, ":", score)