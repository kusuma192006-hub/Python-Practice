#Find students who attended both worksshops , only python , only AI and At leasr one worksshops
students={"Kusuma","Mahesh","Mallika","Madhuri","Poornima","Harsha"}
workshops={"Python", "AI"}
python_workshop= {"Kusuma", "Mahesh", "Mallika", "Harsha"}
AI_workshop={"Kusuma", "Madhuri", "Harsha", "Poornima"}
both_workshop= python_workshop & AI_workshop
python=python_workshop - AI_workshop
AI=AI_workshop - python_workshop
atleast_one=python_workshop |  AI_workshop
print("The Students who attended the both workshops :",both_workshop)
print("The students who only attended python is : " ,python)
print("The students who only attended AI is : " , AI)
print("The students who attended at least one workshop : ",atleast_one)
