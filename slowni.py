persons = {
    "name": "błażej",
    "lname": "kowalski",
    "city": "kraków",
    "age": "22",
}

print(persons)

favorite_numbers = {
    "badzi": 1,
    "stefan": 2,
    "aga": 3,
    "zin": 4,
    "eu": 5,
}
for name in favorite_numbers:
    favorite_number = favorite_numbers[name]
    print(f"Ulubina liczba {name.title()} to {favorite_number}")