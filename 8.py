#Find the sum of all even numbers from 1 to 100
i=1
total=0
while i<=100:
    if i%2 !=0:
        i+=1
        continue
    total+=i
    i+=1
print("The Sum of The Even Numbers are : " , total)