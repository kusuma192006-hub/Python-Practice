#Count how many numbers bewtween 1 and 100 are divisible by 5 
count=0
for i in range(1,101):
    if i %5==0:
        count+=1
print(count)