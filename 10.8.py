file_names = ['cats.txt', 'dogs.txt', 'birds.txt']


def read_file(file_name):
    try:
        with open(file_name) as f:
            for line in f:
                print(f"My pet name is {line.strip().title()}")
    except FileNotFoundError:
        print(f"{file_name} not found.")


for file_name in file_names:
    read_file(file_name)
