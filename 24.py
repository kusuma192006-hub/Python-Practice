#Create a list containing only even numbers using list comprehension
l=[1,2,3,4,5,6,7,8,9,10]
even=[x for x in l if x%2==0]
print("the even numbers are : ", even)