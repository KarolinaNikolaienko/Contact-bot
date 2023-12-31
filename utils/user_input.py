from utils.ValidationUtils import ValidationUtils
import re


def contact_input(add=True, name=None):

    if not add:
        name = input("Enter name: ").strip()
    while not name and add:
        name = input("Name is mandatory\nEnter name: ").strip()
    
    if not add:
        print(" * Enter '-' to delete old data" )
    explanation = "{:<35} {:<50}\n".format(" - Edit phones", "<old> - <new>, <old1> - <new1>, ...")
    explanation += "{:<35} {:<50}\n".format(" - Add phones", "<phone1>, <phone2>, ...")
    explanation += "{:<35} {:<50}\n".format(" - Remove phone", "del <phone1>, del <phone2>")
    explanation += "{:<35} {:<50}".format(" - Combinations are supported", "<add_phone>, del <del_phone>, <old_phone> - <new_phone>")

    if not add:
        print(explanation)

    phones = list(filter(None, input("Enter phones (comma-separated): ").strip().split(',')))
    if add:
        if not ValidationUtils.validate_phone_list(phones):
            phones = list(filter(None, input("Enter phones (comma-separated): ").strip().split(',')))
    else:
        if phones and phones != '-':
            for phone in phones:
                del_edit_phones = list(filter(None, re.split(r'[- ]|del', phone)))
                if not ValidationUtils.validate_phone_list(del_edit_phones):
                    phones = list(filter(None, input("Enter phones (comma-separated): ").strip().split(',')))

    
    email = input("Enter email (optional): ").strip()
    while not ValidationUtils.validate_email(email) and email != '-':
        email = input("Enter email (optional): ").strip()
    
    address = input("Enter address (optional): ").strip()
    
    birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    while not ValidationUtils.validate_birthday(birthday) and birthday != '-':
        birthday = input("Enter birthday (DD.MM.YYYY, optional): ").strip()
    
    return {"name" : name, "phones" : phones, "email" : email, "address" : address, "birthday" : birthday}

def note_input(add=True):

    title = input("Enter title: ").strip()
    while not title and add:
        title = input("Title is mandatory\nEnter title: ").strip()
    
    text = input("Enter text: ").strip()
    while not text and add:
        text = input("Text is mandatory\nEnter text: ").strip()
    
    tags = list(filter(None, input("Enter tags (comma-separated): ").strip().split(',')))

    return {"title" : title, "text" : text, "tags" : tags}