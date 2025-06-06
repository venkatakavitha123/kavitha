import contact
contacts = {}
print("contact app")
while True:
    try:
        print("1.add contacts")
        print("2.view contacts")
        print("3.delete contact")
        print("4.find contact")
        print("5.edit contact")
        print("exist")
        choice = int(input("enter choice:"))   

        if choice == 1:
            contact.add_contact(contacts)
        elif choice == 2:
            contact.view_contacts(contacts)
        elif choice == 3:
            contact.delete_contact(contacts)
        elif choice == 4:
            contact.find_contact(contacts)
        elif choice == 5:
            contact.edit_contact(contacts)
        else:
            print("thank you")
            break
    except Exception as error:
        print("error occured")
    finally:
        print("successfully create a contact")
        