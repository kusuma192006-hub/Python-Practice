"""Ask the user for a password allow only 3 attempts. if the password is corect, print login 
Successful. otherwise print account locked"""
password=""
correct_password="9876"
attempts=0
while password !=correct_password and attempts<3:
    password=input("Enter a correct password : ")
    attempts+=1
if password==correct_password:
    print("Login Successfully.")
else:
    print("Account Locked.")