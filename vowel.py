#remove all vowels
a="engineering"
result=''
for ch in a:
    if ch not in "aeiouAEIOU":
        result+=ch
print(result)
       