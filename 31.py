num = int(input("Enter a number: "))

for i in range(1, num + 1):
    temp = i
    digits = len(str(i))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == i:
        print(i)