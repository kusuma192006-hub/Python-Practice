#Student Result Analyzer
name=input("Enter your name : ")
age=int(input("Enter your age : " ))
marks=int(input("Enter your marks : "))
attendance=int(input("Enter your attendance : "))
print(" Student Report ")
print("Name : ",name)
if marks>=35:
    print("Result : Pass")
    if marks>90:
        print("Grade A")
    elif marks>75:
        print("Grade B")
    elif marks>60:
        print("Grade C")
    elif marks>35:
        print("Grade D")
    if marks>=85 and attendance>=90:
        print("Eligible For Scholarship.")
    else:
        print("Scholarship: Not Eligible")
else:
    print("Fail")
if age>=18:
    print("Eligible For Voting")
else:
    print("Not Eligible For Voting")
if attendance<75:
    print("Warning : Low Attendance")