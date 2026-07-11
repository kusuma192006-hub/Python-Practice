#find the most repeated character
a="Kusuma"
d={}
for ch in a:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
max_char=''
max_count=0
for key in d:
    if d[key]>max_count:
        max_count=d[key]
        max_char=key
print("most repeated character : ", max_char)
print("count : ", max_count)
