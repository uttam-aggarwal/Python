'''Design an application where user will input two dates.
1.	His/her date of birth in DD/MM/YY format.
2.	Current (Present day) date in DD/MM/YY format.
Your app will calculate and let the user know how many days that person survived in this world.
Note: Your calculation must be accurate and you have to consider leap and non-leap years separately.'''
#incomplete
print("Enter the date in format - dd/mm/yyyy")
a=input("DOB: ")
b=input("TODAY: ")
b_year=int(a[6:10])
t_year=int(b[6:10])
leap,nonleap=[],[]
for i in range(b_year,t_year+1):
    if i%4==0:
        leap.append(i)
    else:
        nonleap.append(i)
days=0
days=(len(leap)*366)+((len(nonleap)-1)*365)
b_month=int((a[3:5]))
t_month=int((b[3:5]))
days=days-(b_month*30)+(t_month*30)
b_days=int(a[0:2])
t_days=int(b[0:2])
days=days-b_days+t_days
print("congratulations you have successfully survived for",days,"days")