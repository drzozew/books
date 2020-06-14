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
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Przytiwanie urzytkownika z użyciem jego imienia"""
    username = get_stored_username()
    if username:
        print(f"Witamy ponownie, {username}.")
    else:
        username = get_new_username()
        print(
            f"Twoje imie zostało zapisane i zostanie użyte "
            f"ponownie później {username}")


def check_user():
    """Sprawdza czy użytkowni już istnieje"""


greet_user()
