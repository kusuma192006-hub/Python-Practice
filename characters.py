#count occurence of each character without using count()
a="strawberry"
visited=""
for ch in a:
    if ch not in visited:
        count=0
        for i in a:
            if ch==i:
                count+=1
        print(ch, " : ",count)
        visited+=ch
    