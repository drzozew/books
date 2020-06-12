class User():
    def __init__(self, first_name, Last_name, age, city):
        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age
        self.city = city
        self.login_attemps = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.Last_name.title()} ma "
              f"{self.age} lat i pochodzi z {self.city.title()}")

    def greet_user(self):
        print(f"Witaj {self.first_name.title()} {self.Last_name.title()}")

    def increment_login_attempts(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0


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
