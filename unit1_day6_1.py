'''Your task is to:
1. Take two integers from the user p and q.
2. Perform the operations(<< and <=) on both the variables and store the
result of these two operations in two variables c and b respectively.
3. Then, perform the logical AND operation on variables c and b, and store the 
result in another variable r, and print the result in r.
4. At the end, perform logical NOT operation on r, and print the result.'''
p=int(input())
q=int(input())
c=p>q
b=p<=q
r=c&b
print(r)
print(not r)