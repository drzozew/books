fav_nums = {
    "zigi": [4, 5, 7],
    "badzi": [2, 33, 43],
    "stefan": [3, 123, 232],
    "ingar": [22, 84, 84],
    "ada": [223, 845, 74],
}

for name, num in fav_nums.items():
    print(f"Ulubione liczby {name.title()} to: ")
    for fav_num_1 in num:
        print("  " + str(fav_num_1))
