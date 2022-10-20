'''Isaac purchased a high-definition television for Rs.P with a compound interest rate of R percent and a term of T years. A compound interest calculation was requested by him on monthly basis. Would you be able to assist him with the compound interest calculation?
Functional Description:
CI = P(1+(R/12))^12t-p
Where,
P is the principal amount
R is the rate of interest in decimal points.
T is the time span in years
Constraints:
P, R, and T must be > 1
Rate of interest can be a floating type decimal value
Print the result upto 2 decimal places (Don't try to roundoff the value)
Sample Test case:
1500 (First line of input is P)
1 (Second line of the input is T)
.043(Third line of input is R in decimal point not %)
65.79 (output)'''
p=int(input())
t=int(input())
r=float(input())
print("{:.2f}".format((p*((1+(r/12))**(12*t)))-p))