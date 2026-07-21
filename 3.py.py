#Find the student with highest marks
students={
    "Kusuma":9.07,
    "Harshitha":9.07,
    "Bhaanupriya":8.04,
    "Bhuvija":8,
    "Nandhini":8.5
}
highest=max(students,key=students.get)

print("Highest Scoring Student:", highest)
print("Marks:", students[highest])