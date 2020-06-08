sandwich_orders = ["bułka", "kebs", "z jajkiem", "wege"]
finisched_sandwiches = []

while sandwich_orders:
    finisched = sandwich_orders.pop(0)
    finisched_sandwiches.append(finisched)
    print(f"{finisched} zrobiona")

print(finisched_sandwiches)
