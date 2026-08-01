student_marks = {}

for i in range(5):
    name = input(f"Enter the name of student {i + 1}: ")
    marks = int(input(f"Enter marks for {name}: "))
    student_marks[name] = marks

print("\n Student Marks ")
for student, marks in student_marks.items():
    print(student, ":", marks)

highest_mark = max(student_marks.values())
lowest_mark = min(student_marks.values())
average_marks = sum(student_marks.values()) / len(student_marks)

passed_students = 0
failed_students = 0

for marks in student_marks.values():
    if marks >= 35:
        passed_students += 1
    else:
        failed_students += 1

print("\n Summary ")
print("Highest Mark :", highest_mark)
print("Lowest Mark :", lowest_mark)
print("Average Marks :", average_marks)
print("Passed Students :", passed_students)
print("Failed Students :", failed_students)

print("\n Grades ")
for student, marks in student_marks.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "F"

    print(student, ":", grade)