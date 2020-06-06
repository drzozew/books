guests = ["dziadek", "babcia", "rodzina"]
rem = []

for x in guests:
    print(f"Zapraszam {x.title()} na obiad !")

cant_come = "dziadek"

print(f"{cant_come.title()} nie może przyjść")

guests.remove(cant_come)
can_come = "badzi"

print(f"Za to  {can_come.title()} przyjdzie")

guests.append(can_come)

for x in guests:
    print(f"Zapraszam {x.title()} na obiad !")

print("Oho, znalazł się wiekszy stół można zaprosić wiecej osób !")

guests.insert(0, "edek")
guests.insert(2, "zigi")
guests.append("kora")

for x in guests:
    print(f"Zapraszam {x.title()} na obiad !")

print("Lipa stół zaginął, zostało miejce dla dwóch osób")


while len(guests) >= 3:
    rem = guests.pop()
    print(f"Przykro mi {rem.title()} ale nie możesz przyjśc")

for x in guests:
    print(f"Zapraszam {x.title()}")
