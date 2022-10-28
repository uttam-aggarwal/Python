numbers=[]
while True:
    a=int(input("enter the number: "))
    numbers.append(a)
    b=input("another number? N/Y: ")
    if b=="N":
        break
a=0
no=0
for i in numbers:
    for j in range(0,i):
        if i==a:
            no=1
            print(i,"is not valid")
        a+=i
    if no==0:
        print(i,"is valid")

