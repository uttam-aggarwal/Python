'''In this project user will enter single or multiple numbers and your system will predict
that the entered number or number’s is/are valid number(s) in a Fibonacci series or not.
For example, if user inputs 2 numbers
0 and 7
0 is valid and 7 is invalid.
Because if we plot Fibonacci series 0 1 1 2 3 5 8 13……, In this series 0 is their but 7 is not present.
Constraint: range of the single number or multiple numbers you are entering can be huge.'''
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

