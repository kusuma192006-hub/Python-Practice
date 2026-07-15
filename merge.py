L1=[1,2,3,4,5,6]
L2=[2,3,4,5,6,7,8,9]
merged_list=L1+L2
result=[]
for num in merged_list :
    if num not in result:
        result.append(num)
print(" The new list is : " , result)
