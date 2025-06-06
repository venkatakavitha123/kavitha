def add_contact(contacts):
    file = open("./file1.txt" , "a")
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file.write(f"{name},{mobile}\n")
    file.close()
def view_contacts(contacts):
    print("\n")
    for i in contacts:
        print(f"{i} : {contacts[i]}")

def delete_contact(contacts):
    file = open("./file1.txt" , "r")
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact:" , name_to_delete)
    contacts[name_to_delete] = file.readline()
    list_contacts = contacts.split("\n")
    print("contact list after delete" , list_contacts)
    file.close()
    
def find_contact(contacts):
    find = input("Enter name to search : ")
    found = False
    for i in contacts:
        if find in i:
            print(f"{i} => {contacts[find]}")
            found = True
    if not found:
        print("contact not Found!!!")

def edit_contact(contacts):
    file = open("./file1.txt" , "r")
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    print("edited contact",name_to_edit)  
    contacts[name_to_edit] = file.readline() 
    list_contacts = contacts.split("\n")
    print("contact list after edit", list_contacts)
    file.close()