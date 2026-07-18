#Remove duplicate words from a sentence
s="Python is easy and Python is powerful"
print(type(s))
words=s.split()
print(words)
unique_words=set()
for i in words:
    if i not in unique_words:
        unique_words.add(i)
print("The New list is : " ,unique_words)
print("The New Sentence is : " ," ".join(unique_words))
