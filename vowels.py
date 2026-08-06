# Count the vowels in a string using a function
def vowel(string):
    count=0
    for ch in string:
        if ch in "aeiouAEIOU":
            count+=1
    print("The Count of vowel is : ", count)
vowel("kusuma")

