marks={
    "Ram":90,
    "Anu":45,
    "Tom":30,
    "Sam":80
}
new_dict={key:value for key,value in marks.items() if value>50}
print(new_dict)