#Create a function that accepts any number of numbers and finds the largest number without using max().
def maximum(*numbers):
    largest=numbers[0]
    for num in numbers:
        if largest<num:
            largest=num
    return largest
print(maximum(10,100,20,200,90))