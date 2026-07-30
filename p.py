#Count how many students passed 
marks={"Ram":80,"Anu":95,"Tom":20}
count=0
for key,value in marks.items():
    if value>=35:
        count+=1
print("The count of passed students are : " , count)