#College Admission System
student_name=input("Enter the Student Name: ")
pcm_percentage=int(input("Enter your pcm percentage : "))
entrance_exam_rank=int(input(" Enter your Entrance Exam Rank :"))
category=input("Enter Your Category : ")
sports_quota=input(" Enter if you are in sports quota(yes\no) : ")
print("\n Final Admission Report ")
print("Student Name : ",student_name)
if pcm_percentage>=75 and entrance_exam_rank<=50000:
    print("Admission_status : Student is Eligible.")
else:
    print("Admission_status :Not Eligible.")
if category.lower()=="sc" or category.lower()=="st":
    print("Fee concession : 100%")
elif category.lower()=="obc":
    print("Fee Concession : 50% ")
else:
    print("Fee Concession : No Concession ")
if sports_quota.lower()=="yes":
    print("SPorts quota : Eligible.")
else:
    print("Sports quota :  Not Eligible")
if pcm_percentage>=90:
    print("Scholorship : Eligible.")
else:
    print("Scholorship: Not Eligible.")