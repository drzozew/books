sandwich_orders = ["bułka", "kanapka z czyms", "kebs",
                   "kanapka z czyms", "z jajkiem", "kanapka z czyms", "wege"]
finisched_sandwiches = []

print("skończyło się 'coś'")

while "kanapka z czyms" in sandwich_orders:
    sandwich_orders.remove("kanapka z czyms")

while sandwich_orders:
    finisched = sandwich_orders.pop(0)
    finisched_sandwiches.append(finisched)
    print(f"{finisched} zrobiona")

print(finisched_sandwiches)
