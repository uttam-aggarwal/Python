a=[]
b=0
while True:
    n=int(input("enter the number: "))
    a.append(n)
    cont=input("another? Y/N- ")
    if cont=="N":
        break
def sumlist(a,stoper):
    if stoper==len(a)-1:
        return a[len(a)-1]
    sumlistm1=sumlist(a,stoper+1)
    sumlistm=sumlistm1+a[stoper]
    return sumlistm
for i in a:
    b=b+i
print(b)
print(sumlist(a,0))
