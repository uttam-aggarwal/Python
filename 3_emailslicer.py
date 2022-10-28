emails=[]
while True:
    n=input("EMAIL: ")
    emails.append(n)
    repeat=input("want to enter another one? Y/N: ")
    if repeat=="N":
        break
for i in emails:
    for j in range(0,len(i)):
        if i[j]=="@":
            print("username:",i[0:j])
            print("domain:",i[j+1:len(i)].upper())