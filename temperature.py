#Temperature Analysis
temperatures=(30,32,28,27,25,26,29,31)
days_above_average=0
days_below_average=0
maximum_temperature=max(temperatures)
minimum_temperature=min(temperatures)
total=sum(temperatures)
average=total/len(temperatures)
for tem in temperatures :
    if tem>average:
        days_above_average+=1
    if tem<average:
        days_below_average+=1
print("The maximun temperature is : ",maximum_temperature)
print("The minimum temperature is : ",minimum_temperature)
print("The average is : " ,average)
print(" The days above average is : " ,days_above_average)
print("The days below the average is : ",days_below_average)
