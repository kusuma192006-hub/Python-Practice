#Shopping bill
items=("rice","milk","bread","Eggs","Aplle")
price=(60,30,40,72,120)
print(" Shopping items and prices are : ")
for i in range(len(items)):
    print(items[i], ": ",price[i])
Total=sum(price)
Highest=max(price)
Lowest=min(price)
average=Total/len(price)
print("\n Total price is : ",Total)
print("Highest price is : " , Highest)
print("Lowest price is : ", Lowest)
print(" Average price : " , average)