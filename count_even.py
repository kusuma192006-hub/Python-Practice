#Create a function that accepts multiple numbers and counts how many of them are even
def even(*numbers):
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    return count
print(even(2, 5, 8, 11, 14, 17))