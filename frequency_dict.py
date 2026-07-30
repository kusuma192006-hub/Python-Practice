#Count the frequency of each character in a string using a dictionary
string="Poornima"
frequency={ch:string.count(ch) for ch in string}
for key, value in frequency.items():
    print(f"{key}:{value}")