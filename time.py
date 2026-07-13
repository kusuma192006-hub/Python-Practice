#Time Converter
total_seconds=int(input("enter the total seconds : "))
hours=total_seconds //3600
remaining_seconds=total_seconds % 3600
minutes=remaining_seconds //60
seconds=remaining_seconds % 60
print(" the hours :  " , hours)
print("remaining_seconds : ", remaining_seconds)
print("minutes : " , minutes)
print("seconds : ", seconds)