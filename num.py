#Reverse a number
num=int(input("Enter a number to reverse : "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("The Reversed Number is : " , rev)