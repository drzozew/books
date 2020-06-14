file_name = "guest_book.txt"
close = 'tak'

while close != 'nie':
    name = input("Write your name: ")
    print(f"Witaj {name.title()}!")
    with open(file_name, 'a') as file_object:
        file_object.write(f"{name}\n")
    close = input("Czy dodać kolejne imie ? tak/nie: \n")
