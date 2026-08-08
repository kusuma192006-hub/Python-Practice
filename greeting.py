#Create a program that demonstrates the difference between local and global variables
count=0
def counter():
    global count
    count+=1
    print(f"Function Called ",count,"times")
counter()
counter()
counter()