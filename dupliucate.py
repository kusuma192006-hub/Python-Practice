#Remove duplicate elements while preserving the original order
numbers=[1,8,9,1,2,3,4,1,9,8,1,2,6,5,1,3]
result=[]
for num in numbers:
    if num not in result:
        result.append(num)
print(" The new list without changing the original list is : " , result)