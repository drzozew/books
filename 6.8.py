animal_1 = {
    "lew": "stefan",
}

animal_2 = {
    "słoń": "badzi",
}

animal_3 = {
    "kot": "ziga"
}

pets = [animal_1, animal_2, animal_3]

for pet in pets:
    for pet_, owner in pet.items():
        print(f"Właścicielem {pet_} jest {owner}")
