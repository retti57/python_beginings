word = input('Podaj napis: ')
count = 0
search = input('Podaj literę której szukamy: ')
for letter in word:
    if search == letter:
        count += 1

print('Szukana fraza', search, 'występuje ', count, 'razy')
