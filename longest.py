#find a longest word
a=" python is very powerful "
words=a.split()
largest=""
for word in words:
    if len(word)>len(largest):
        largest=word
print("the largest word is : " , largest)
print("length of the word is : ", len(word))