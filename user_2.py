from user_1 import User


class Admin(User):

    def __init__(self, first_name, Last_name, age, city):
        super().__init__(first_name, Last_name, age, city)
        self.show_priviliges = Priviliges()

    def user_name(self):
        self.user_full_name = f"{self.first_name} {self.Last_name}"
        self.user_full_name = self.user_full_name.title()
        return(self.user_full_name)


class Priviliges():

    def __init__(self, privileges=["może dodać post",
                                   "może usunąć post", "może zbanować kogoś"]):
        self.privileges = privileges

    def show_privilage(self):
        print("Ten użytkownik jako Admin może: ")
        for priv in self.privileges:
            print(f"- {priv}")
