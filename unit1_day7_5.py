'''Laasya bought a new volleyball in the sports shop. It looks medium size. She somehow found the radius of the sphere. But she would like to know the volume
of that ball.
Can you help him in finding the Volume of the ball?
Functional Description:
Volume = 4/3 πr³
pie= 314
Constraint:
1.00 ≤r ≤5.00
Sample Test case:
21
38772.72'''
a=float(input())
volume=4/3*3.14*a**3
print("{:.2f}".format(volume))