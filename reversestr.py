a=input("enter the string: ")
def reverse(a,stoper):
    if stoper==len(a)-1:
        return a[stoper]
    revm1=reverse(a,stoper+1)
    revm=revm1+a[stoper]
    return revm
for i in range(-1,-len(a)-1,-1):
    print(a[i],end="")
print()
print(reverse(a,0))
