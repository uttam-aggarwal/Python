numbers=[]
while True:
    a=int(input("enter the number: "))
    numbers.append(a)
    b=input("another number? N/Y: ")
    if b=="N":
        break
count_p=0
count_c=0
stop=0
for i in numbers:
    if i>0:
        for j in range(2,i):
            if i%j==0:
                stop=1
    elif i<0:
        for j in range(-2,i,-1):
            if i%j==0:
                stop=1
    if stop==0:
        print(i,"is a prime number")
        count_p+=1
    elif stop==1:
        print(i,"is a composite number")
        count_c+=1
print("there are",count_p,"prime numbers")
print("there are",count_c,"composite numbers")