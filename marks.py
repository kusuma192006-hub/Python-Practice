#Student Marks Analyzer
marks=(100,34,89,35,78,36,56,45,54,90)
student_above_35=0
student_below_35=0
Highest_mark=max(marks)
Lowest_mark=min(marks)
total=sum(marks)
average=total/len(marks)
for mark in marks:
    if mark>=35:
        student_above_35+=1
    else:
        student_below_35+=1
print("Student Mars Analysis : ")
print("The Highest mark is : ",Highest_mark)
print("The Student Lowest mark is : " , Lowest_mark)
print("The Average is : " , average)
print("The Number of students got above 35 : " , student_above_35)
print("The Number of students failed : " ,student_below_35)
print("\n Grades : ")
for mark in marks:
    if mark>=90:
        print(mark, " : Grade A")
    elif mark>75:
        print(mark, ": Grade B")
    elif mark>=35:
        print(mark , " : Grade C")
    else:
        print(mark, " : Fail ")

