#count occurence of each character using dict
a="pineapple"
d={}
for ch in a:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)