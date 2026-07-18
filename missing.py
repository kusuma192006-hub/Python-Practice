#Find the missing numbers from 1 to 20
numbers={1,2,4,5,8,9,10,12,20}
missing=set()
for i in range(1,21):
    if i not in numbers:
        missing.add(i)
print("The Missing numbers are : " ,missing)
