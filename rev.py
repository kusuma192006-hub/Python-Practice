#Reverse a string using a function
def rev(string):
    reverse=" "
    for ch in string:
        reverse=ch+reverse
    print("The reversed string is :  ",reverse)
rev("kusuma")