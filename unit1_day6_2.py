'''You are given string S = "Python is a programming language"
Your task is to
Input 3 strings a, b, and c from the user.
. Check whether the given strings a, b, and c are present in the given string
S or not, and print the result in boolean type (True or False).'''


S = "Python is a programming language"
a=input("a: ")
b=input("b: ")
c=input("c: ")
print(a in S,b in S,c in S,sep="\n")