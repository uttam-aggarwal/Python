'''Students have been given an assignment by their teacher. During the
assignment, the teacher gave a positive number n and asked students to find the value which when multiplied two times became exactly equal to the provided number n
Constraints:
n is > 0
Display the result upto 2 decimal places
Sample test case
9 (Only line of input contains the integer n)
3.00 (Print the value when multiplied by itself two times, equals the number n).'''
import math
n=int(input())
print("{:.2f}".format(math.sqrt(n)))