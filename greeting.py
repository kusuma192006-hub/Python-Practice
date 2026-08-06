#Create a program that demonstrates the difference between local and global variables
def fun(name):
    name="local"
    print(f"local variable:{name}")
name="global"
fun(name)
print(f"global variable:{name}")