import json
from phonebook import *

def main():
    global contacts
    
    try:
        file_object = open('backup_file.json', 'r')
        contacts.update(json.load(file_object))
        file_object.close()
    except FileNotFoundError:
        print('No backup file Available!')

    #collect and store contacts in dictionary    
    store_contacts()
    print(f"contacts = {contacts}")

    file_object = open('backup_file.json', 'w')
    json.dump(contacts, file_object)
    file_object.close()
    
    #helps to retrieve a contact by a given name
    retrieve_contact()
    
if __name__ == '__main__':
    main()
    
