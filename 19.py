#Check whether a given number is prime
num=int(input("Enter a number: "))
if num<=1:
    print("it is not a prime number.")
else:
    for i in range(2,num):
        if num%i==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number.")