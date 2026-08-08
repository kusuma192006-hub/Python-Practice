#Create a function that accepts any number of numbers using *args and prints their sum
def add(*numbers):
    return sum(numbers)
print(add(2,3,4,5))
print(add(10, 20))
print(add(1, 2, 3, 4, 5))
print(add(5, 10, 15, 20, 25))