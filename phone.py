#Build a Phonebook Using Dictionaries
structure={
    "Rahul":"9876543210",
    "Priya":"9876543211",
    "Anil":"9876543212"
}
while True:
    print("\ Phobebook")
    print("1. Add a new contact")
    print("2.Search a contact by number")
    print("3.Delete a contact")
    print("4.Display all contacts")
    print("5.Count total contacts")
    choice=input("Enter the choice between (1 to 5 ) : ")
    if choice=="1":
        contact=input("Enter a new contact : ")
        structure.add(contact)
        if contact in structure:
            print("enter the correct contact.")
        else:
            print("Added succesfully.")
    elif choice=="2":
        contact=input("Enter a contact to search : ")
        if contact in structure:
            print(contact,"is there")
        else:
            print(contact,"Not Found")
    elif choice=="3":
        contact=input("Enter a number to update : ")
        structure.update(contact)
        print("Updated Succesfully.")
    elif choice=="4":
        for contacts in structure:
            if contacts in structure:
                print(contacts)
            else:
                print("Empty!")
    elif choice=="5":
        len(structure)
        print("The Total contacts are : ", structure)
    else:
        print("ENter the valid choices")