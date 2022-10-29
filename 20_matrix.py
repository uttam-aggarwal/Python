'''A basket is given to you in the shape of a matrix. If the size of the matrix is N x N then the range of number of 
eggs you can put in each slot of the basket is 1 to N2 . You task is to arrange the eggs in the basket such that 
the sum of each row, column and the diagonal of the matrix remain same.
Test case for your reference:
Input by the user dimension of the basket i.e., N = 3
So, number of eggs you can put at each slot are in the range of 1 to 3^2 (1 to 9)
Input: 
6 3 6
5 5 5
4 7 4
Explanation: 
    Now the value of the sum of 
    any row or column as well as diagonal is 15
Note:  2 < = N <= 100'''
#incomplete
'''n=int(input("enter the size of matrix: "))
R1,R2,R3=[],[],[]
for i in range(0,n):
    R1.append(0)
a=1
b=0
c=0
while True:
    for i in range(1,a+1):
        R1[0]=i
        for i in range(0,n):
            b+=R1[i]
            c+=R2[i]
            if b==c:
                pass
'''
for i in range(0,3):
    print(i,end='')
    for j in range(0,3):
        print(j)