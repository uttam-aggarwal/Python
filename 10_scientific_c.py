import math
a=input("do you wanna read instructions? Y/N: ")
if a=="Y":
    print("add(+) , sub(-) ,multiply (*), divide(/), mod(%),square root(sqrt),exponent(pow),sine(s),cosine(c),tangent(t),for radian to degree(1),for degree to radian(2) ")
while True:
    a=input("enter the string associated with the operation you want to perform: ")
    if a in ["+",'-','*','/','%','pow']:
        no1,no2=int(input("no1: ")),int(input("no2: "))
        if a=="+":
            print(no1+no2)
        elif a=="-":
            print(no1-no2)
        elif a=="*":
            print(no1*no2)
        elif a=="/":
            print(no1/no2)
        elif a=="%":
            print(no1%no2)
        elif a=="pow":
            print(no1**no2)
    elif a in ["s",'c','t','sqrt','1','2']:
        no=int(input("no: "))
        if a=="s":
            print(math.sin(no))
        elif a=="c":
            print(math.cos(no))
        elif a=="t":
            print(math.tan(no))
        elif a=="sqrt":
            print(math.sqrt(no))
        elif a=="1":
            print(no*(180/math.pi))
        elif a=="2":
            print(no*(math.pi/180))
    end=input("wanna continue? N/Y: ")
    if end=="N":
        break