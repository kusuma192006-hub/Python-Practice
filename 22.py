#Find the sum of all odd numbers from 1 to N
num=int(input("Enter a number : "))
total=0
for i in range(1,num+1):
    if i%2 !=0:
        total+=i
print("The sum of the all odd number is : " , total)