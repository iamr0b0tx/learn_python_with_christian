class User:
    def __init__(self, username):
        self.username = username

    def buy_product(self):
        print(f"{self.username} is buying a product")

    def login(self):
        print(f"{self.username} is logging in...")

    def logout(self):
        print(f"{self.username} is loggin out ...")


jake = User("jakey2000")
jake.login()
jake.buy_product()
jake.logout()


class Admin(User):
    def delete_user(self):
        print(f"{self.username} is deleteing a user")

chris_admin = Admin("chris_admin")
chris_admin.login()
chris_admin.buy_product()
chris_admin.logout()
chris_admin.delete_user()