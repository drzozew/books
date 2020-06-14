import json


def get_stored_username():
    """pobieranie imienia z pliku, o ile taki istnieje"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """
    Poproszenie użytkownika, aby podał swoje imię,
    a nastepnie zapisanie tego imienia w pliku.
    """
    username = input("Jak masz na imię? ")
    filename = 'username.json'
    with open(filename, 'a') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Przytiwanie urzytkownika z użyciem jego imienia"""
    check_names()
    username = get_stored_username()
    if username:
        print(f"Witamy ponownie, {username}.")
    else:
        username = get_new_username()
        print(
            f"Twoje imie zostało zapisane i zostanie użyte "
            f"ponownie później {username}")


def make_user_list():
    """Tworzy listę użytkowników"""
    filename = 'username.json'
    global user_list
    user_list = []
    try:
        with open(filename) as f:
            for line in f:
                user_list.append(line.replace('"', ""))
    except FileNotFoundError:
        return None
    else:
        return user_list


def check_names():
    make_user_list()
    name_check = input("Jak masz na imie?: ")
    if name_check in user_list:
        pass
    else:
        print("nie ma")


greet_user()
