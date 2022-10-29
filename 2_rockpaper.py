'''Create the Rock, Paper and Scissors game with Python, we need to take the user choice
and then we need to compare it with the computer choice which is taken using the random module in Python
from a list of choices, and if the user wins, then the score will increase by 1'''
import random
name=input("Enter your name: ")
user_s=0
cpu_s=0
while True:
    a=input("Rock(R),paper(P) or scissors(S)?: ")
    if a=="R":
        print(name,"-🪨",end=" 🆚  ")
    elif a=="P":
        print(name,"-💌",end=" 🆚  ")
    elif a=="S":
        print(name,"-✂️",end=" 🆚  ")
    b=["R","P","S"]
    cpu=random.choice(b)
    if cpu=="R":
        print("CPU -🪨")
    elif cpu=="P":
        print("CPU -💌")
    elif cpu=="S":
        print("CPU -✂️")
    
    if a==cpu:
        print("Tie")
    else:
        if a=="R":
            if cpu=="S":
                print(name,"wins")
                user_s+=1
            else:
                print("cpu wins")
                cpu_s+=1
        elif a=="P":
            if cpu=="R":
                print(name,"wins")
                user_s+=1
            else:
                print("cpu wins")
                cpu_s+=1
        elif a=="S":
            if cpu=="P":
                print(name,"wins")
                user_s+=1
            else:
                print("cpu wins")
                cpu_s+=1
    print(name,":",user_s,"cpu :",cpu_s)
    c=input("Once more? N/Y: ")
    if c == "N":
        break
    else:
        pass
if user_s>cpu_s:
    print("winner is",name)
else:
    print("winner is cpu")
print("-----game by uttam_aggarwal")