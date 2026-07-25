#Print the multiplication table of a given number
num=int(input("Enter a number : "))
i=1
while i<=10:
    result=num*i
    print(num,"*",i,"=",result)
    i+=1