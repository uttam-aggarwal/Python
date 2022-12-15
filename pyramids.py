# Pattern #1: Simple Number Triangle Pattern
# Pattern:
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
a=1
for i in range(1,5):
    for j in range(0,i):
        print(a,end=" ")
    print("")
    a=a+1
# Pattern #2: Inverted Pyramid of Numbers
# Pattern:
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5
a=1
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(a,end=" ")
    print("")
    a=a+1
# Pattern #3: Half Pyramid Pattern of Numbers
# Pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
for i in range(1,6):
    a=1
    for j in range(0,i):
        print(a,end=" ")
        a=a+1
    print("")
# Pattern #4: Inverted Pyramid of Descending Numbers
# Pattern:
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1
a=5
for i in range(5,0,-1):
    for j in range(0,i):
        print(a,end=" ")
    a=a-1
    print("")
# Pattern #5: Inverted Pyramid of the Same Digit
# Pattern:
# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
a=5
for i in range(5,0,-1):
    for j in range(0,i):
        print(a,end=" ")
    print("")
# Pattern #6: Reverse Pyramid of Numbers
# Pattern:
# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1
a=1
for i in range(1,6):
    b=a
    for j in range(0,i):
        print(b,end=" ")
        b-=1
    print("")
    a+=1

# Pattern #7: Inverted Half Pyramid Number Pattern
# Pattern:
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
for i in range(7,2,-1):
    a=0
    for j in range(0,i-1):
        print(a,end=" ")
        a+=1
    print("")
 
# Pattern #8: Pyramid of Natural Numbers Less Than 10
# Pattern:
# 1 
# 2 3 4 
# 5 6 7 8 9
a=1
b=1
for i in range(1,4):
    for j in range(0,b):
        print(a,end=" ")
        a+=1
    b+=2
    print("")
   
# Pattern #9: Reverse Pattern of Digits from 10 
# Pattern:
# 1
# 3 2
# 6 5 4
# 10 9 8 7
a=0
for i in range(1,5):
    b=a
    for j in range(i,0,-1):
        print(b+j,end=" ")
        a+=1
    print("")
# Pattern #10: Unique Pyramid Pattern of Digits
# Pattern:
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1
#will continue...
# Pattern #11: Connected Inverted Pyramid Pattern of Numbers
# Pattern:
# 5 4 3 2 1 1 2 3 4 5 
# 5 4 3 2 2 3 4 5 
# 5 4 3 3 4 5 
# 5 4 4 5 
# 5 5
# Pattern #12: Even Number Pyramid Pattern
# Pattern:
# 10 
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2
  
 
# Pattern #13: Pyramid of Horizontal Tables
# Pattern:
# 0  
# 0 1  
# 0 2 4  
# 0 3 6 9  
# 0 4 8 12 16  
# 0 5 10 15 20 25  
# 0 6 12 18 24 30 36
# Pattern #14: Pyramid Pattern of Alternate Numbers
# Pattern:
# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9
# Pattern #15: Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers
# Pattern:
#            1 
#          1 2 
#       1 2 3 
#    1 2 3 4 
#  1 2 3 4 5
 
  
# Pattern #16: Equilateral Triangle with Stars (Asterisk Symbol)
# Pattern:
#             *   
#            * *   
#           * * *   
#          * * * *   
#         * * * * *   
#        * * * * * *   
#       * * * * * * *
 
    
# Pattern #17: Downward Triangle Pattern of Stars
# Pattern:
#         * * * * * * 
#          * * * * * 
#           * * * * 
#            * * * 
#             * * 
#              * 
 
 
 
 
#    Pattern #18: Pyramid Pattern of Stars
# Pattern:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
