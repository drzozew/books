def count_words(file_name, word):
    with open(file_name) as f:
        content = f.read()
        x = content.lower().count(word)
        print(f"Zwrot {word} znajduje się w pliku {file_name} {x} razy")


count_words('ksiazka.txt', 'dom')
count_words('ksiazka.txt', 'błażej')
count_words('ksiazka.txt', 'berlin')
count_words('ksiazka.txt', 'tak')
