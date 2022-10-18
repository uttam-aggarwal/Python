'''Bony and Tony went to California to attend the Apple products launch event. In the event location, there are a lot of mini-contests going on with exciting rewards. In one such stall, there was a contest where a floating point decimal number is given and asked the visitors to display the rightmost digit of an integral part of the number using programming logic
Can you help Bony and Tony to display the rightmost digit of an integral part of the number so that they get the exciting apple products as a reward?
Constraints:
1.000 number ≤ 1000.999
Sample test case:
1985.674 Only line of input has a single floating point value with three values after decimal point.
5 ->Print the output in a single line rightmost integral part of the number.'''
a=float(input())
b=int(a)
print(b%10)