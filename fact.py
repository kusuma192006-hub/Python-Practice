#Find the factorial of a given number using a while loop
number=int(input("Enetr a number : " ))
fact=1
while number>0:
    fact*=number
    number-=1
print("The Factorial of the number is : ", fact) 

