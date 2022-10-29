'''Email Slicer is just a simple tool that will take multiple email address as an input and slice it to produce 
the username and the domain associated with it. The email must be divided into two strings by using @ as the separator.
So, user provides n number of email addresses and you have to design a logic to slice the username and the 
domain out of those email addresses. The domain part must print in capitals.
Note: Email addresses must be stored first in some container and then operate the required logic on it.'''
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