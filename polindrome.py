#Check whether a number is a palindrome
num=int(input("Enter a number : "))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10
print("The Reversed Number is : ",rev)
if rev==original:
    print("The Number is polindrome")
else:
    print("Its not a polindrome")