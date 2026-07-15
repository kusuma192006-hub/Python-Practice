#Print all Even numbers and odd numbers seperately
numbers=[1,2,3,4,5,6,7,8,9,10]
print("The Even numbers are : " )
for num in numbers:
    if num%2==0:
        print(num)
print("The Odd number are : " )
for num in numbers:
    if num % 2 !=0:
        print(num)