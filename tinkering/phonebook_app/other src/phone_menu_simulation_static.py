def display_menu(menus):

    for menu in menus:
        print(menu)

    menu_option = input('Type your menu: ')
    show_menu(menus[menu_option])

def show_menu(menu):
    info = menu.items() if type(menu) == dict else enumerate(menu)
    for key, value in info:
        print(f"{key} => {value}")

contact_menu = {
    'shile':"09087650678",
    'bob':"08066654675",
}

messages_menu = {
    'shile':'i\'ll text you back',
    'MTN':'Your balance is low'
}

settings_menu = ['phone', 'connection', 'call', 'display']

menu_dictionary = {
    'contacts':contact_menu,
    'messages':messages_menu,
    'settings':settings_menu
}

display_menu(menu_dictionary)
