#Create a dictionary of five students and their marks
students={
    "Kusuma":9.07,
    "Harshitha":9.07,
    "Bhaanupriya":8.04,
    "Bhuvija":8,
    "Nandhini":8.5
}
print(students)
print(students.keys())
print(students.values())
print(students.items())
students.pop("Bhuvija")
print(students)
print("Nandhini" in students)
students["Hemavathi"]=8.9
print(students)
#Updating the student marks
students.update({"Bhaanupriya":9.5})
print(students)
#Count the total number of keys
print(len(students.keys()))
#Copy one dictionary to another
new_students=students.copy()
print("The copied dict is : " , new_students)