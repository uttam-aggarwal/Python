'''There are N students in a school, and the administration wants the classes to be divided such that each class can have maximum strength of S. Find out how many classes with strength S will be formed
Constraints:
N and S must be > 0
S<= N
Sample Test case:
2000 (First line of input contains N)
60 (Second line of input contains S)
33 (Output as required)'''
N=int(input())
S=int(input())
print(int(N/S))