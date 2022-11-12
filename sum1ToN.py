n=int(input("enter the number: "))
b=0
def sumton(n):
    if n==1:
        return 1
    summ1=sumton(n-1)
    summ=summ1+n
    return summ
for i in range(1,n+1):
    b=b+i
print(b)
print(sumton(n))
