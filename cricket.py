#Cricket Score Analysis
scores=(45,78,0,62,91,33,55,0,49,84)
players_names=("Virat Kohli","Rohit Sharma","Shubman Gill","KL Rahul","Hardik Pandya"," Rishabh Pant"," Suryakumar YAdav","Ravindra Jadeja","Jasprit Bumrah","Mohammed Shami")
above_50=0
zero_score=0
Highest_score=max(scores)
Lowest_score=min(scores)
total=sum(scores)
average=total/len(scores)
print(" The Highest score is : ",Highest_score)
print("The Lowest score is : " , Lowest_score)
print("The average is : " , average)
for score in scores:
    if score>50:
        above_50+=1
    if score==0:
        zero_score+=1
print("Cricket score Analysis : ")
print(" The Highest score is : ",Highest_score)
print("The Lowest score is : " , Lowest_score)
print("The average is : " , average)
print("The score above 50 is : " ,above_50)
print("The scoring zero is : ", zero_score)