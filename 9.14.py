from random import choice

lotter = [5, 6, 7, 5, 6, 8, "cso", "dqwd", "cce"]
wins = []
y = 0
while y < 4:
    x = choice(lotter)
    lotter.remove(x)
    wins.append(x)
    print(f"Los {x} wygrał!")
    y += 1
