'''Sita has bought a Saree. The shopkeeper measured the saree in terms of centimeters but she wanted the length of the saree in meters. Can you help Sita
to find out the length of her Saree in meters
Constraints:
1 <= cm <= 500
Sample test case:
200-- Only line of input contains the length in centimeters
2 ---> Print the length of the saree in meters'''
a=float(input())
print("{:.2f}".format(a/100))
