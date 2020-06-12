from random import randint as ri


class Die():
    """Kostka do gry"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = ri(1, self.sides)
        print(f"Kostka wylosowała {roll}")


x = Die(20)
y = 0

while y < 10:
    x.roll_die()
    y += 1
