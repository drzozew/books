def make_album(artist, song_name, num=''):
    persons = {
        artist: song_name,
    }
    if num != '':
        persons['number'] = num
    return persons


albums = make_album('jony', 'qaws', '5')
albums1 = make_album('sony', 'uga')
albums2 = make_album('50c', 'candy')

print(albums)
print(albums1)
print(albums2)
