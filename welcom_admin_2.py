current_users = ["badzi", "admin", "stefan", "zigi", "ada"]
new_users = ["admin", "badzi", "stega", "adna"]
new_userss = new_users[:].lower()

for new_user in new_users:
    if new_user in current_users:
        print(f"Przykro mi {new_user}, nazwa {new_user} jest zajęta")
    else:
        print(f"Nazwa {new_user} jest wolna")