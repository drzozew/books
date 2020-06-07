fav_languages = {
    "badzi": "python",
    "zigi": "C#",
    "aga": "js",
    "ida": "pascal",
    "nadar": "python",
}

names = ["badzi", "stefan", "ada", "betar"]

for name, language in fav_languages.items():
    print(f"{name.title()} lubi {language}")

for name in names:
    if name not in fav_languages:
        print(f"{name.title()} nie brał udziału w ankiecie")
        fav_languages[name] = input(
            f"{name.title()} jaki jest twój ulubiony język?: ")

for vale in set(fav_languages.values()):
    print(vale)
