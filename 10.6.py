num_1 = input("First number: ")
num_2 = input("Second number: ")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
except ValueError:
    print("Numbers only allowed")
else:
    output = num_1 / num_2
    print(output)
