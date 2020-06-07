question = "Ile masz lat ?: "
active = True

while active:
    age = input(question)
    if age == 'koniec':
        active = False
        continue
    elif int(age) <= 3:
        print("Bilet jest za darmo")
    elif int(age) > 3 and int(age) <= 12:
        print("Bilet kosztuje 10 zł")
    elif int(age) > 12:
        print("Bilet kosztuje 15 zł")
