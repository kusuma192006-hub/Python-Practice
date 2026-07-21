#Find the duplicate values
student = {
    "Kusuma": 90,
    "Harshitha": 85,
    "Bhaanupriya": 90,
    "Nandhini": 75
}
seen=set()
duplicate=set()
for values in student.values():
    if values not in seen:
        seen.add(values)
    elif values in seen:
        duplicate.add(values)
print("The duplicate value is : " , duplicate)
