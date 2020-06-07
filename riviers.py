riviers = {
    "nil": "egipt",
    "wisła": "polska",
    "amazonka": "brazylia"
}

for rivier, contry in riviers.items():
    print(f"{rivier.title()} płynie przez {contry.title()}")

for rivier in riviers.keys():
    print(rivier)

for value in riviers.values():
    print(value)
