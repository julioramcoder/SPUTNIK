#MY CONTACTS FROM MY PHONE 
contacts = []  # here we create an empty list to store all contacts we will add later

while True:  # this keeps the program running in a loop until the user chooses to exit
    print("\nCONTACTS AGENDA")
    print("1. add contact")
    print("2. view contacts")
    print("3. search contact")
    print("4. exit")

    option = input("choose an option: ")  # ask the user which action they want to do

    if option == "1":
        # here we collect all the information to add a new contact
        name = input("name: ")
        phone = input("phone: ")
        email = input("email: ")
        contact = {"name": name, "phone": phone, "email": email}  # we put all info together inside a dictionary
        contacts.append(contact)  # we add the dictionary into the list
        print("contact added successfully")  # confirm the contact was saved

    elif option == "2":
        # in this part, we show all the contacts saved in the list
        if not contacts:  # check if the list is empty
            print("no contacts saved yet")
        else:
            print("\ncontacts list:")
            for c in contacts:  # we go one by one through the list
                print(f"name: {c['name']}, phone: {c['phone']}, email: {c['email']}")  # show the contact info

    elif option == "3":
        # here we let the user look for a contact by name
        name = input("enter the name to search: ")
        found = False  # we use this to check if we find the name or not
        for c in contacts:  # go through each contact in the list
            if c["name"].lower() == name.lower():  # compare names without worrying about capital letters
                print(f"name: {c['name']}, phone: {c['phone']}, email: {c['email']}")  # show the data if found
                found = True
                break  # stop the search if we already found the contact
        if not found:
            print("contact not found")  # message when no name matches

    elif option == "4":
        # if the user chooses to exit, we stop the loop and end the program
        print("leaving the program...")
        break  # this breaks the while loop

    else:
        # this runs if the user writes something different from 1 to 4
        print("invalid option, try again")