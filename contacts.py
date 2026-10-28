

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