#Create a function using **kwargs that calculates the total of all numeric values passed to it.
def total(**details):
    result=0
    for key,value in details.items():
        if isinstance(value,(int,float)):
            result+=value
    return result
print(total(name="Kusuma",age=20,marks=20))
