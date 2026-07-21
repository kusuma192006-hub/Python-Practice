#Reverse a key-value pairs
student = {
    "name": "Kusuma",
    "age": 20,
    "branch": "Aeronautical"
}
reverse={}
for key,value in student.items():
    reverse[value]=key
print("The Reversed Key-value pair is : " , reverse)