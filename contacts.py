

def add_contact(contacts,name,phone,email=""):
    key = name.lower()
    if key in contacts:
        return False
    contacts[key] = {"phone": phone , "email" : email , "tags" : set()}
    return True




def find_contact(contacts,name):
    key = name.lower()
    return contacts.get(key)

def delete_contact(contacts, name):
    key = name.lower()
    if key in contacts:
        # remove the key, then return True
        contacts.pop(key)
        return True
    else:
        return False
    # otherwise return False


def add_tag(contacts, name, tag):
    key = name.lower()
    if key not in contacts:
        # return False
        return False
    contacts[key]["tags"].add(tag.lower())
    return True
    # add tag.lower() to the set, then return True


def search_by_tag(contacts, tag):
    tag = tag.lower()
    matches = []
    for name, details in contacts.items():
        if tag in details["tags"]:
            matches.append(name)
    return matches


def show_menu():
    print("\n1. Add contact")
    print("2. Find contact")
    print("0. Quit")

contacts = {}

while True:
    show_menu()
    choice = input("choose: ")

    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        name = input("enter the name: ")
        phone = input("enter the number: ")
        result = add_contact(contacts,name,phone)
        if result:
            print("Added!")
        else:
            print("Name already exists")

    elif choice == "2":
        name = input("enter the name to be searched: ")
        found = find_contact(contacts,name)
        if found is None:
           print("Not found")
        else:
           print(found)

    else:
        print("invalid choice")

            
            



