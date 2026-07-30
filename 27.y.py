#Swap keys and values of a dictionary
d={"A":1,"B":2}
swap={value:key  for key,value in d.items() }
print(swap)