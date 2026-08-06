#Find the Fibonacci series uo to n terms using a function
def fibonocci(num):
    a=0
    b=1
    for i in range(num):
        print(a,end=' ')
        c=a+b
        a=b
        b=c
fibonocci(9)