names = ["admin", "badzi", "edward", "stefek", "zigi"]

if names:
    for name in names:
        if name is "admin":
            print(f"Witam {name} serdecznie")
        else:
            print(f"Witaj {name} , ciesze, ze jesteś ponownie")
else:
    print("Lista jest pusta!")
