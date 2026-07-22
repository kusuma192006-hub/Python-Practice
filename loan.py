#Bank Loan Eligibility
age=int(input("Enter Your Age : "))
monthly_salary=int(input("Enter your Monthly Salary : "))
credit_score=int(input("Enter Your Credit score : "))
existing_loan = input("Do you have an existing loan? (yes/no): ")
if age>=21 :
    if monthly_salary>=30000:
        if credit_score>=700:
            if  existing_loan.lower()=="no":
                print("Loan Approved")
            else:
                print("Loan Rejected : You have a existing loan.")
        else:
            print("Loan Rejected : Credit score is less")
    else:
        print(" Loan Rejected : Monthly Salary is Low")
else:
    print("Loan Rejected : Must be 21 or above")