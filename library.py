#Library Book Manager
books_list={"Python Programming","Algorithms","Machine Learning Basics"}
while True:
    print("\n Library book Manager")
    print("1. Add books ")
    print("2.REmove books ")
    print("3.Search books")
    print("4. Display available books")
    print("5. Exit")
    choice=input("Enter your choice between (1 to 5) : ")
    if choice=="1":
        book=input("enter the book name : ")
        books_list.add(book)
        print(book,"Added Succesfully.")
    elif choice=="2":
        book=input("Enter the book name to remove : ")
        if book in books_list:
            books_list.remove(book)
            print(book,"Removed Succesfully.")
        else:
            print("book not found.")
    elif choice=="3":
        book=input("Enter the book name to search : ")
        if book in books_list:
            print(book,"is There.")
        else:
            print(book,"is not There.")
    elif choice=="4":
        if books_list:
            print("\n Book List")
            for books in books_list:
                print(books)
        else:
            print("Books are not there")
    elif choice=="5":
        print("Thank You!")
        break
    else:
        print("Enter valid choice between ( 1 to 5) ")