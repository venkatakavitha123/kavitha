import appcon
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
            appcon.add_contact(contacts)
        elif choice == 2:
            appcon.view_contacts(contacts)
        elif choice == 3:
            appcon.delete_contact(contacts)
        elif choice == 4:
            appcon.find_contact(contacts)
        elif choice == 5:
            appcon.edit_contact(contacts)
        else:
            print("thank you!!")
            break
    except Exception as error:
        print("error occured")
    finally:
        print("successfully create a contact")