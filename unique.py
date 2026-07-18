#FInd the unique characters in a sting
s="characters"
t=set()
for i in s:
    if i not in t:
        t.add(i)
print("The Unique charactersare : ", t)