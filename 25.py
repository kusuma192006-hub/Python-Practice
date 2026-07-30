#Create a list of numbers divisible by both 3 and 5 from 1-100 using list comprehension
num=[x for x in range(1,100) if x%3==0 and x%5==0 ]
print(num)