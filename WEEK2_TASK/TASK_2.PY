# Sample program to calculate average score

# Function to calculate average
def calculate_average(scores):
    if len(scores) == 0:
        return 0  # Avoid division by zero
    total = sum(scores)
    average = total / len(scores)
    return average

# Example usage
student_scores = [85, 90, 78, 92, 88]  # You can replace with actual scores
avg_score = calculate_average(student_scores)

print("Student Scores:", student_scores)
print("Average Score:", avg_score)