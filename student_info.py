#Create a function that accepts student information using **kwargs and prints each key and value.
def student_info(**details):
    for key,value in details.items():
        print(key,":",value)
student_info(name="Kusuma",marks="20",USN="1NT24AE048")