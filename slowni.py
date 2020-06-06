favorite_numbers = {}
x = 0

while True:
    if x < 4:
        name = input("Podaj swoje imie: ").strip().lower()
        f_num = input("Podaj swoją ulubioną liczbę: ").strip().lower()
        favorite_numbers[name] = f_num
        x = x + 1
    else:
        break

for name in favorite_numbers:
    favorite_number = favorite_numbers[name]
    print(f"Ulubina liczba {name.title()} to {favorite_number}")