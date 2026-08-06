#Check whether a number is prime using a function
def prime(num):
    if num<=1:
        return "Not a Prime Number"
    for i in range(2,num):
        if num%i==0:
            return "Not a Prime Number"
    return "Prime Number"
result=prime(10) 
print(result)   