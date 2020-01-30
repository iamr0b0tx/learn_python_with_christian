def display_menu():
    menus = ['messages', 'settings', 'contacts']
    for menu in menus:
        print(f"Type {menu} for {menu.capitalize()}")

    menu_option = input('Type your menu: ')
    menu_option = menu_option.lower()
    
    if menu_option == 'contacts':
        contacts()

    elif menu_option == 'settings':
        settings()

    elif menu_option == 'messages':
        messages()

    else:
        menu_error()

def contacts():
    print('shile => 09087650678')

def settings():
    print('Phone')
    print('Developer Settings')
    print('Call settings')

def messages():
    print('You have no messages')

def menu_error():
    print('Invalid Menu Option!')
    display_menu()

display_menu()
