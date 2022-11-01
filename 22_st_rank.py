'''Your task is to find the name of the student with maximum marks after updation in marks and the jump in the student’s rank i.e., previous rank – current rank. 
You are given three lists’ names, mark’s and update’s where: 
•	Names contain the names of students.
•	Marks contain the marks of the same students.
•	Updates contains the integers by which the marks of these students are to be updated'''
#incomplete
def sort_dict(dict1):
    new_dict = sorted(dict1.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(new_dict)

    return converted_dict
name=["A","B","C","D","E"]
marks=[14,12,33,44,32]
updates=[33,22,44,55,11]
dict1={}
dict_u={}
for i in range (0,len(name)):
    dict1[name[i]]=marks[i]
new_dict=(sort_dict(dict1))
for i in range (0,len(name)):
    dict_u[name[i]]=updates[i]
new_dict_u=(sort_dict(dict_u))
print("previous ranking- ")
#for i in range(0,len(dict1)):
#   print(i,"-",end='')
for key,value in new_dict.items():
    print(key,end=' -- ')
print("\n","new ranking- ")
#for i in range(0,len(dict1)):
#   print(i,"-",end='')
for key,value in new_dict_u.items():
    print(key,end=" -- ")

