#Check whether a string is a palindrome using a function
def palindrome(string):
    reverse=""
    for ch in string:
        reverse=ch+reverse
    if reverse==string:
        print("It is a Palindrome.")
    else:
        print("It is not a Palindrome")
palindrome("level")
