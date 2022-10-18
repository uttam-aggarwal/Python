'''Karthik was working in the HR division of Audi. The employees of the company were working on shifts. The company calculates salary for the employees on the basis of employee working days. Since the number of people working in the company is huge and the salary calculation become a tedious process at the end of the each day. Find out the total salary of the employees based on the total working days.
Constraints:
1 days <= 30
1 salaryperday <= 6000
salaryperday can be in floating type decimal number.
Input Format:
30 →→→→→ The First line of the input has a single value representing the total working days of type integer.
500→→→→→→ The Second line of the input has single value representing the salary per day.
Output Format:
Print the total salary in single line with two values after decimal point (Precision).'''
a=int(input())
b=float(input())
print("{:.2f}".format(a*b))