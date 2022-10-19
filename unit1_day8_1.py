'''Write a complete program to read a positive number n from the user, and find out the sum of squares of first n even natural numbers.
Functional description:
2n(n+1)(2n+1)
Constraints:
n is >= 1
The result is displayed as float with precision upto 2 decimal places.
Sample test case
5 (Only line of input contains the integer n)
220.00 (Print the sum of squares of first n even numbers)'''
n=float(input())
a=(2*n*(n+1)* (2*n+1))/3
print("{:.2f}".format(a))