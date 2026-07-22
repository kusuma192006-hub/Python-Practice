#ATM Machine
pin=int(input("Enter the pin : "))
current_balance=int(input("Enter the current balance : "))
withdrawal_amount=int(input("Enter the amount to withdraw : "))
if pin==1234:
    if current_balance>=withdrawal_amount:
        if current_balance-withdrawal_amount>=1000:
            current_balance=current_balance-withdrawal_amount
            print("Transaction Successful.")
            print("Remainining balance is : " ,current_balance )
        else:
            print(" Minimum balance rule is violated.")
    else:
        print("Insufficient amount.")
else:
    print("Incorrect pin")