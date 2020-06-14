def collect_phone_number():
    phone_number = input("type your number: ").strip()
    while not phone_number.isdigit() or len(phone_number) != 11:
        print('Invalid Phone number')
        phone_number = input("type your number: ").strip()

    return phone_number

def collect_name():
    name = input("type your name[or q to quit]: ").strip().lower()
    while not name.isalpha():
        print('Invalid Name!')
        name = input("type your name[or q to quit]: ").strip().lower()
        
    return name

def store_contacts():
    print('STORAGE MODE', 'created in phonebook.py = ', id(contacts))

    while True:
        name = collect_name()
        if name == 'quit' or name == 'q':
            break

        # collect phone number with function
        phone_number = collect_phone_number()    
        contacts[name] = phone_number

def retrieve_contact():
    print('\nRETRIVAL MODE')
    while True:
        name = collect_name()
        if name == 'quit' or name == 'q':
            break

        try:
            print(name, contacts[name])

        except:
            print('Key does  not exist')

#create contacts dictinary
contacts = {}

