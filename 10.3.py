file_name = 'guest.txt'

name = input("Write your name: ").strip()

with open(file_name, 'a') as file_object:
    file_object.write(f"{name}\n")
