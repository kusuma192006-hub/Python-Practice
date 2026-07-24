#Find the smallest digit in agiven number
num=int(input("Enter a number : "))
smallest=9
while num>0:
    last_digit=num%10
    if last_digit<smallest:
        smallest=last_digit
    num//=10
print("The Smallest Number is : ", smallest)