'''Your task is to find the name of the student with maximum marks after updation in marks and the jump in the student’s rank i.e., previous rank – current rank. 
You are given three lists’ names, mark’s and update’s where: 
•	Names contain the names of students.
•	Marks contain the marks of the same students.
•	Updates contains the integers by which the marks of these students are to be updated'''
#incomplete
name=["A","B","C","D","E"]
marks=[14,12,33,44,32]
updates=[33,22,44,55,11]
dict={}
for i in range (0,len(name)):
    dict[name[i]]=marks[i]

