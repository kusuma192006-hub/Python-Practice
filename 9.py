#Keep asking the user for numbers until they enter 0
""" after stopping, print: 
total numbers entered
sum
Average"""
num=int(input("Enter a number : "))
count=0
total=0
while num !=0:
    count+=1
    total+=num
    avg=total/count
    num=int(input("Enter a number ( 0 to stop) : "))
print("The total numbers entered : " , count)
print("The sum of the numbers : ", total)
print("The average of the number is : ",avg)