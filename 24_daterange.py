print("Enter the date in format - dd/mm/yyyy")
a=input("staring date: ")
b=input("ending  date: ")
s_date=int(a[6:10])
e_date=int(b[6:10])
leap,nonleap=[],[]
for i in range(s_date,e_date+1):
    if i%4==0:
        leap.append(i)
    else:
        nonleap.append(i)
print("leap years are: ",leap)
print("nonleap years are: ",nonleap)