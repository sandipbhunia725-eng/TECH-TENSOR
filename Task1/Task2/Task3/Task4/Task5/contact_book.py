contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No Contacts Found!")
        else:
            for c in contacts:
                print("----------------------")
                print("Name   :", c["name"])
                print("Phone  :", c["phone"])
                print("Email  :", c["email"])
                print("Address:", c["address"])

    elif choice == "3":
        search = input("Enter Name: ")
        found = False

        for c in contacts:
            if c["name"].lower() == search.lower():
                print("Name   :", c["name"])
                print("Phone  :", c["phone"])
                print("Email  :", c["email"])
                print("Address:", c["address"])
                found = True

        if not found:
            print("Contact Not Found!")

    elif choice == "4":
        search = input("Enter Name to Update: ")

        for c in contacts:
            if c["name"].lower() == search.lower():
                c["phone"] = input("New Phone: ")
                c["email"] = input("New Email: ")
                c["address"] = input("New Address: ")
                print("Contact Updated Successfully!")
                break
        else:
            print("Contact Not Found!")

    elif choice == "5":
        search = input("Enter Name to Delete: ")

        for c in contacts:
            if c["name"].lower() == search.lower():
                contacts.remove(c)
                print("Contact Deleted Successfully!")
                break
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
