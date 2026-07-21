#Create a dictionary of five students and their marks
students={
    "Kusuma":9.07,
    "Harshitha":9.07,
    "Bhaanupriya":8.04,
    "Bhuvija":8,
    "Nandhini":8.5
}
print(students)
#Print all keys
print(students.keys())
#Print all values
print(students.values())
#Print all key-value pairs
print(students.items())
#Remove one Student
students.pop("Bhuvija")
print(students)
#Check whether a key exists
print("Nandhini" in students)
#Add a new student
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