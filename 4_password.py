'''Create a program that takes the length of the password as input and generates a random password of the same 
length. The strength of the password depends equally on the 4 properties mentioned below. 
If the password generated randomly following the rules or constraints given below, then that password
is treated as good in terms of strength and accepted otherwise ignore that password.
The properties to be followed for a strong password are:
•	At least 12 characters.
•	A mixture of both uppercase and lowercase letters.
•	A mixture of letters and numbers. 
•	Inclusion of at least one special character, e.g., @ #?]
Note: do not use < or > in your password, as both can cause problems in Web browsers.
'''
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
