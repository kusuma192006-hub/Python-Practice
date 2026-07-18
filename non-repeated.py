#Find the first non-repeated element in a list
l=[4,2,3,2,4,5]
for element in l:
    if l.count(element)==1:
        print("The first non-repeated element is : ", element)
        break