extras = []
active = True
question = "Jaki dodatek do pizzy?"
question += "\nWpisz koniec jeżeli chcesz wyjść: "

while active:
    que = input(question)
    if que == 'koniec':
        active = False
    else:
        extras.append(que)

for extra in extras:
    print(f"Wybrany dodatek do pizzy to {extra}")
