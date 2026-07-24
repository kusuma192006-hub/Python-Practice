#Find the largest digit in a given number
num=int(input("Enter a number: "))
largest=0
while num>0:
    last_digit=num%10
    if last_digit>largest:
        largest=last_digit
    num//=10
print("The Largest Digit is : ", largest)