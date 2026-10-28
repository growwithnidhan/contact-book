

def add_contact(contacts,name,phone,email=""):
    key = name.lower()
    if key in contacts:
        return False
    contacts[key] = {"phone": phone , "email" : email , "tags" : set()}
    return True


contacts = {}
print(add_contact(contacts, "Asha", "9876543210"))
print(add_contact(contacts, "asha", "1111111111"))
print(add_contact(contacts, "Riya", "9123456789", "riya@example.com"))
print(contacts)

def find_contact(contacts,name):
    key = name.lower()
    return contacts.get(key)
print(find_contact(contacts,"ASHA"))
print(find_contact(contacts, "Meera"))

def delete_contact(contacts, name):
    key = name.lower()
    if key in contacts:
        # remove the key, then return True
        contacts.pop(key)
        return True
    else:
        return False
    # otherwise return False
print(delete_contact(contacts, "RIYA"))
print(delete_contact(contacts, "Riya"))
print(contacts)


def add_tag(contacts, name, tag):
    key = name.lower()
    if key not in contacts:
        # return False
        return False
    contacts[key]["tags"].add(tag.lower())
    return True
    # add tag.lower() to the set, then return True
print(add_tag(contacts, "Asha", "Hostel"))
print(add_tag(contacts, "asha", "hostel"))
print(add_tag(contacts, "Meera", "friend"))
print(contacts["asha"]["tags"])


def search_by_tag(contacts, tag):
    tag = tag.lower()
    matches = []
    for name, details in contacts.items():
        if tag in details["tags"]:
            matches.append(name)
    return matches

add_contact(contacts, "Riya", "9123456789")
add_contact(contacts, "Meera", "9000000000")
add_tag(contacts, "Riya", "hostel")
add_tag(contacts, "Meera", "family")

print(search_by_tag(contacts, "Hostel"))
print(search_by_tag(contacts, "family"))
print(search_by_tag(contacts, "college"))
        