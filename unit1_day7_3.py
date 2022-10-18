'''Take a string whose length is 5. Your job is to swap the first and last characters of the string and print the resultant string.
Python
Sample test case 1:
pytho (input contains a string with five characters).
oythp (output contains a string in which first and last characters are swapped
with each other)'''
a=input()
for i in range(len(a)):
    if i==0:
        print(a[len(a)-1], end="")
    elif i<len(a)-1:
        print(a[i], end="")
    else:
        print(a[0])

