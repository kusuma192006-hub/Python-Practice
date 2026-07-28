#Find the sum of numbers from 1 to N
num=int(input("Enter a number : "))
total=0
for i in range(1,num+1):
    total+=i
print("The sum of the number is : ",total)