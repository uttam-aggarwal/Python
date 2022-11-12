num=int(input("enter the number: "))
power=int(input("enter the number: "))
def pow(a,b):
    if b==0:
        return 1
    powm1=pow(a,b-1)
    powm=powm1*a
    return powm
print(pow(num,power))
