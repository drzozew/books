class User():
    def __init__(self, first_name, Last_name, age, city):
        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"{self.first_name.title()} {self.Last_name.title()} ma "
        f"{self.age} lat i pochodzi z {self.city.title()}")

    def greet_user(self):
        print(f"Witaj {self.first_name.title()} {self.Last_name.title()}")


x = User("badzi", "kan", "22", "kista")
x.greet_user()
x.describe_user()
