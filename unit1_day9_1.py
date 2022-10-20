'''Brown has been given a Six-letter word by Jack, and he has been instructed to reverse it. If the provided word's first and second letters are identical to the first and second letters of the reversed in any sequence then, Brown should respond with the word true. Otherwise, Brown will respond with false
Constraints:
length of the word = 6
letters of the word are case sensitive.
Sample Test case1:
madema (First line of input contains the string of length 6)
True (Output is in boolean type(True or False))'''
a=input()
b=""
for i in range(5,-1,-1):
    b=b+a[i]
print(b[0:2] in a[0:2] or b[2:0] in a[0:2])
