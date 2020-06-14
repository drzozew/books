def make_album(artist, song_name, num=''):
    persons = {
        artist: song_name,
    }
    if num != '':
        persons['number'] = num
    return persons


while True:
    artis = input("Podaj artystę: ")
    if artis == 'end':
        break
    else:
        song_name1 = input("Podaj nazwę albumu: ")
        if song_name1 == 'end':
            break
        else:
            print(make_album(artis, song_name1))
