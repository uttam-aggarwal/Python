'''A lecture on Armstrong numbers has been given by the teacher.
Lecture Notes on Armstrong numbers:
If N = 153 and as it is a 3-digit number we compute as:
sum of the cubes of the digits 1, 5, and 313+53 +33 153, As 153 == 153, So 153 is an Armstrong number.
And if N=1532 and as it is a 4-digit number we compute as.
sum of the 4th root of digits 1, 5, 3, and 2-14+54 +34 +24-723 that is not equal to the number N = 1532, So 1532 is not an armstrong number.
The teacher selected a student at random and assigned them a 3 digit number. and questioned whether the supplied number is armstrong or not. If it is armstrong, the student must respond with True; otherwise, he must give a False response. Would you be able to assist the learner in finding the answer?
Constraints:
100 <= Number <= 999
Sample test case:
153 (Online line of the input contains three digit number)
True (Print the result in the boolean type(True or False))'''
a=input()
b=0 
for i in a:
    b=b+int(i)**len(a)

print(b==int(a))
