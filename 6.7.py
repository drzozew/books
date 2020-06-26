p1 = {
    "fnam": "badzi",
    "lnam": "kara",
    "city": "kartuzy",
    "age": 20
}

p2 = {
    "fnam": "aga",
    "lnam": "bir",
    "city": "siera",
    "age": 23
}

p3 = {
    "fnam": "stefa",
    "lnam": "zig",
    "city": "kartuzy",
    "age": 22
}

people = {
    "user_1": p1,
    "user_2": p2,
    "user_3": p3,
}

for persona, user_info in people.items():
    full_name = f"{user_info['fnam']} {user_info['lnam']}"

persons_list = [p1, p2, p3]

for persona in persons_list:
    print(f"{persona['fnam'].title()} {persona['lnam'].title()} pochodzi z "
          f"{persona['city'].title()} i ma {persona['age']} lat")
