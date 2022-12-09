fname = 'mbox.txt'
fhand = open(fname)
text = 'From '
d = dict()
for line in fhand:
    search = line.startswith(text)   # podaje wartość -1 jeśli nie znaleziono
    splited = line.split()
    if search is False:
        continue
    elif len(splited) < 6:
        continue
    elif len(splited) == 7:
        for i in splited:
            time = splited[5]  # okreslenie adresata w przeszukiwanej linii
            sptime = time.split(":")
            h = sptime[0]
            d[h] = d.get(h, 0) + 1
lst = list()
for k, v in d.items():
    lst.append((k, v))
lst = sorted(lst)
for hour in lst:
    print(hour[0], hour[1])
fhand.close()
