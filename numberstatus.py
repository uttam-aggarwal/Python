import random
a,b=int(input("Enter the start of range: ")),int(input("enter the end of range: "))
c=[]
stop=0
for i in range(a,b):
    c.append(i)
number=random.choice(c)
#odd or even-
if number%2==0:
    print(number,'is even')
else:
    print(number ,'is odd')
#positive or negative
if number>0:
    print(number,"is positive")
    for i in range(2,number):
        if number%i==0:
            stop=1
elif number<0:
    print(number,"is negative")
    for i in range(-2,number,-1):
        if number%i==0:
            stop=1
else:
    print(number,"is neither positive nor negative")
#prime or compositive
if stop==0:
    print(number ,"is a prime number")
else:
    print(number,"is a compositive number")