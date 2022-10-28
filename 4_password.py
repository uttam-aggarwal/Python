#Q was not clear
import random
set=["#","@","_"]
for i in range(ord("A"),ord("Z")+1):
    set.append(chr(i))
for i in range(ord("a"),ord("z")+1):
    set.append(chr(i))
for i in range(0,10):
    set.append(i)
n=int(input("length of password: "))
for i in range(0,n):
    print(random.choice(set),end="")
