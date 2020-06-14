import json


file_name = 'numbers.json'

try:
    with open(file_name) as f:
        numbers = json.load(f)
except FileNotFoundError:
    fav_num = input("What is your favorite number?: ")
    with open(file_name, 'w') as f:
        json.dump(fav_num, f)
        print("Your favorite number was added to a list")
else:
    print(f"Your favorite number is {numbers}")
