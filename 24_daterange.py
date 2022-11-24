'''Your task to create a functionality in which when user will input a range of two dates. 
Then your module will find and print all years in the range of given dates those are leap years 
separately and rest of the years those are non-leap separately.'''
print("Enter the date in format - dd/mm/yyyy")
a=input("staring date: ")
b=input("ending  date: ")
s_date=int(a[6:10])
e_date=int(b[6:10])
leap,nonleap=[],[]
for i in range(s_date,e_date+1):
    if i%4==0:
        if i%400:
            leap.append(i)
        elif i%100:
            nonleap.append(i)
        else:
            leap.append(i)
    else:
        nonleap.append(i)
print("leap years are: ",leap)
print("nonleap years are: ",nonleap)