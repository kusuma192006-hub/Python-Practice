#Count frequency of characters in a string
text="maheshKumar"
d={}
for ch in text:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print("The frequency of characters in a string are : " , d)