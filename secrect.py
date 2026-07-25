#Guess the secret number using break
secret="123"
guess=""
while secret !=guess:
    num=input("Enter a number : ")
    guess=num
    if secret ==guess:
        break
print(" You're Guess is correct.")