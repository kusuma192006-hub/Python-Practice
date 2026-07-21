marks = {
    "A":90,
    "B":75,
    "C":99
}

highest = max(marks, key=marks.get)

print(highest)
print(marks[highest])