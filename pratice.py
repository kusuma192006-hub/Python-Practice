#Count vowels in every word
words=["apple","cat","orange"]
for word in words:
    count=0
    for ch in word:
        if ch in "aeiou":
            count+=1
    print(word,":",count)
