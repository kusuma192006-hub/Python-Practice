l=[10,20,30,20,40,10,50]
seen=set()
repeated=set()
for i in l:
    if i in seen:
        repeated.add(i)
    else:
        seen.add(i)
print("The Repeated elements are : ", repeated)