from random import choice

lotter = [5, 6, 7, 1, 6, 8, "cso", "dqwd", "cce"]
wins = []
my_ticket = [5, ]
y = 0
x = 0

while x != my_ticket[0]:
    x = choice(lotter)
    lotter.remove(x)
    wins.append(x)
    print(f"Los {x} wygrał!")
    y += 1
print(f"Aby wygrać potrzeba było {y} szans")
