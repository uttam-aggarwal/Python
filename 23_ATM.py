'''You task is to replicate the working of ATM for a single user, lets say, Mr. John, who has already 
successfully logged into her account on the ATM Machine, now, we will program the next steps 
he may want to perform. 
Like display his name and cash available in his savings account
Withdraw cash and display the status of the cash balance.
Deposit cash and display the status of the cash balance.
(Your task is to design and implement the ATM functionality by taking care of all constraints, for example 
if minimum cash available is less than 5000 then system will display low balance)'''
print("HEllO MR. JOHN")
print("CASH AVAILABLE IN YOUR ACCOUNT IS $25000 ")
BALANCE=25000
while True:
    a=int(input('''PRESS 1 TO WITHDRAW CASH
PRESS 2 TO DEPOSIT  CASH
PRESS 3 TO KNOW YOUR CURRENT BALANCE
PRESS 4 TO EXIT
ENTER: '''))
    if a==1:
        W_AMOUNT=int(input("ENTER THE AMOUNT TO WITHRAW IN MULTIPLE OF 500: "))
        if BALANCE>=W_AMOUNT:
            if W_AMOUNT%500==0:
                print(W_AMOUNT, "HAS BEEN WITHDRAWN SUCCESSFULLY")
                BALANCE-=W_AMOUNT
                print("CURRENT BALANCE IS ",BALANCE)
                
            else:
                print("INAPPOROPIRATE ENTRY")
        else:
            print("INSUFFICENT BALANCE")
    elif a==2:
        D_AMOUNT=int(input("ENTER THE AMOUNT TO DEPOSIT: "))
        BALANCE+=D_AMOUNT
        print("CURRENT BALANCE IS ",BALANCE)
    elif a==3:
        print("CURRENT BALANCE IS ",BALANCE)
        if BALANCE<5000:
            print("LOW BALANCE")
    elif a==4:
        print('''THANKS FOR USING ATM
        ---- SUCCESSFULLY EXITED ----''')
        break
    
    