import json

fav_num = input("What is your favorite number?: ")

file_name = 'numbers.json'
with open(file_name, 'w') as f:
    json.dump(fav_num, f)

with open(file_name) as f:
    numbers = json.load(f)

print(numbers)
