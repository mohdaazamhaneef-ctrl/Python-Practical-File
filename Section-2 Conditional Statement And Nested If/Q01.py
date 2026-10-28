#Q1: ATM Withdrawal 
#Write a Python program for ATM withdrawal. 
#Conditions: 
#- Check whether the PIN is correct. 
#- If the PIN is correct, check whether the withdrawal amount is a multiple of 100. 
#- If it is, check whether the balance is sufficient. 
#- If sufficient, withdraw the amount. 
#- Otherwise, print "Insufficient Balance". 
#-If the PIN is incorrect, print "Invalid PIN". 
correct_pin=9760
balance=15000
pin=int(input("Enter Your Pin:"))
if pin==correct_pin:
    amount=int(input("Enter Withdrawal Amount:"))
    if amount%100==0:
        if balance>=amount:
            balance-=amount
            print("Withdrawal Successfull")
            print("Remaining Balance:",balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be multiple of 100")
else:
    print("Invalid PIN")