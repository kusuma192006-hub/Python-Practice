#Create a dictionary showing the frequency of every word in a sentence
sentence="I Love Python And I Love Coding".split()
frequency={}
for word in sentence:
    frequency[word]=sentence.count(word)
for key,value in frequency.items():
    print(f"{key}:{value}")

