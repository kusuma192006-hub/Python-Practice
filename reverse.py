numbers=[1,2,3,4,5]
result=[]
for i in range(len(numbers)-1,-1,-1):
    result.append(numbers[i])
print("The reversed list is : " , result)