#Studence Attendance System
print("THIS IS THE NEW CODE")
attendance = {"Asha", "Rahul", "Priya", "Kiran", "Ravi"}
while True:
    print("\n Student Attendance SYsytem ")
    print("1. Add Student ")
    print("2. Remove Student ")
    print("3. Search Student ")
    print("4. Count  Students ")
    print("5. Display Attendance ")
    print("6. Exit ")
    choice=input(" enter your choice(1-6) : ")
    if choice=="1":
        name=input("enter student name : ")
        attendance.add(name)
        print(name,"added succesfully.")
    elif choice == "2":
        name = input("Enter student name to remove: ")
        print("Current attendance:", attendance)
        if name in attendance:
            attendance.remove(name)
            print(name, "removed Successfully.")
        else:
             print("student not found.")
    elif choice=="3":
        name=input("enter student name to search : ")
        if name in attendance:
            print(name,"is Present.")
        else:
            print(name,"is Absent.")
    elif choice=="4":
        print("Total Students present :", len(attendance))
    elif choice=="5":
        if attendance:
            print("\n Attendance List:")
            for student in attendance:
                print(student)
        else:
            print("Attendance list is empty.")
    elif choice=="6":
        print("Thank you!")
        break
    else:
        print("Invalid choice! please enter a number between 1 and 6.")