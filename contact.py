def add_contact(contacts):
    file = open("./mob.txt","a")
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file.write(f"{name},{mobile}\n")
    file.close()

def view_contacts(contacts):
    print("\n")
    file = open("./mob.txt","r")
    for i in contacts:
        print(f"{i} : {contacts[i]}")
        file.close()

def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    with open("./mob.txt","a") as file:
        if name_to_delete in contacts:
            del contacts[name_to_delete]
            msg = f"delete contact: {name_to_delete}" 
            print(msg)
            file.write(msg +"\n")
        else:
            msg = "no contact found"
            print(msg)
            file.write(msg +"\n")

def find_contact(contacts):
    find = input("Enter name to search : ")
    found = False
    with open("./mob.txt","a") as file:
        for i in contacts:
            if find in i:
                msg = f"{i} : {contacts[find]}"
                print(msg)
                file.write(msg + "\n")
                found = True
        if not found:
            msg = " contact not found "
            print(msg)
            file.write(msg +"\n")

def edit_contact(contacts):
    name = input("enter contact name to edit:")
    with open("mob.txt","a") as file:
        if name in contacts:
            number = int(input("Enter new number: "))
            contacts[name]=number
            msg = f"edited contact:{name}"
            print(msg)
            file.write(msg)
        else:
            msg = "contact not found"
            print("msg")
            file.write("./mob.txt","a")
        