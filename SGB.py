# Grade Book

grades = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78,
    "David" : 88,
    "Emma" : 95
}

# Calculate class average using for loop
total = 0

for score in grades.values():
    total += score

average = total / len(grades)

# Find top and bottom scorer
top_score = max(grades.values())
bottom_score = min(grades.values())

top_student = [name for name, score in grades.items() if score == top_score][0]
bottom_student = [name for name, score in grades.items() if score == bottom_score][0]

print("Class Average:", average)
print("Top Scorer:", top_student, "-", top_score)
print("Bottom Scorer:", bottom_student, "-", bottom_score)

# Search for a student 
name = input("Enter student name: ")

score = grades.get(name)

if score is not None:
    print(name, "scored", score)
else:
    print("Student not found.")