file_name = "pol.txt"

while True:
    question = input("Why do you like programing?: ")
    with open(file_name, 'a') as file_object:
        file_object.write(f"{question}\n")
