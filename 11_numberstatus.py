'''In this project you have to enter a range [A, B] and system will randomly pick any number from your 
given range and check the status of that given number.
The properties to be checked are:
1.	Is that number is odd or even
2.	Is that number is positive or negative number
3.	Is that number is prime number or composite number.
After checking the status, you have to display all the properties followed by the randomly picked number.
For example 
Range is (1,12) and randomly picked number is 10
Then the properties followed by this number are:
10 is a positive number
10 is an even number
10 is a composite number
'''
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