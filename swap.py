#swap first and last character
a="engineering"
l=list(a)
l[0],l[-1]=l[-1],l[0]
a="".join(l)
print("the swapped word is : " , a)

