phonebook = {
    "Rahul": "9876543210",
    "Priya": "9876543211",
    "Anil": "9876543212"
}

while True:
    print("\n PHONEBOOK ")
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Count Total Contacts")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter Contact Name: ")

        if name in phonebook:
            print("Contact already exists!")
        else:
            number = input("Enter Phone Number: ")
            phonebook[name] = number
            print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter Contact Name: ")

        if name in phonebook:
            print(f"{name} : {phonebook[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter Contact Name to update: ")

        if name in phonebook:
            new_number = input("Enter New Phone Number: ")
            phonebook.update({name: new_number})
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter Contact Name to delete: ")

        if name in phonebook:
            phonebook.pop(name)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            print("\nContacts:")
            for name, number in phonebook.items():
                print(name, ":", number)

    elif choice == "6":
        print("Total Contacts:", len(phonebook))

    elif choice == "7":
        print("Thank you for using Phonebook!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")