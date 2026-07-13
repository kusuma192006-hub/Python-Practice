#ATM withdrawal
correct_pin=987654
balance=10000
pin=int(input("enter the correct PIN : "))
if pin==correct_pin:
    amount=int(input(" Enter the withdrwal amount : "))
    if balance>=amount:
        print("withdrawal successful ")
        remaining_balance=balance-amount
        print(" The  remaining_balance is : " ,  remaining_balance)
    else: 
        print("Insufficient balance ")
else:
    print("Incorrect pin")