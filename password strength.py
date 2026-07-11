# password strength checker
a="Engineering123@Kusuma"
uppercase=0
lowercase=0
digit=0
special_character=0
for ch in a:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
    elif ch.isdigit():
        digit+=1
    else:
        special_character+=1
print("Uppercase Letters : " , uppercase)
print("lowercase Letters : " , lowercase)
print("digits : " , digit)
print("special_character : " , special_character)
if uppercase>=1 and  lowercase>=1 and digit>=1 and  special_character>=1:
    print("strong password")