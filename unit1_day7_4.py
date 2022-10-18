'''Captain Johnson was in charge of the Giant Ship. He traveled for many days from India to various countries around the world. For planning the upcoming trip. it would be useful for the captain to know his total number of travel days in the format of (year month: day). Would you be able to help Captain Johnson?
Constraints:
1 <=ndays <= 15000
no of days in a month are fixed to 30.
no of days in a year are fixed to 365
Sample test case:
9451->he only line of input has single integer representing the number days
the ship was travelling.
25 Y 10 M 26 D ->No of days in the year:month day format.'''
a=int(input())
year=int(a/365)
a=a-year*365
month=int(a/30)
a=a-month*30
day=int(a)
print (int(year), "y", int (month), "M", int(day), "D")