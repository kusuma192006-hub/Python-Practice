#Calculate the factorial of a number using a function
def fact(num):
   result=1
   for i in range(1,num+1):
      result=result*i
   return result
result=fact(6)
print(result)