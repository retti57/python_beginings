def openFile(filename):
    return open(filename, 'r', encoding='UTF-8')


def searchForTimeInLine(fhand):
    for line in fhand:
        search = line.startswith('From ')   # podaje wartość False jeśli nie znaleziono
        splited = line.split()
        if search is False:
            continue
        elif len(splited) < 6:
            continue
        elif len(splited) == 7:
            for i in splited:
                time = splited[5]  # okreslenie czasu wiadomości w przeszukiwanej linii
            return time
""" nie przenosi wszystkich wartości time do funkcji niżej
    pokazuje tylko jedno przejście pętli """

def hourFromTime(searchForTimeInLine):
    t = dict()
    sptime = searchForTimeInLine.split(":")
    h = sptime[0]
    t[h] = t.get(h, 0) + 1
    return t


def sortByHours(t):
    lst = list()
    for k, v in t.items():
        lst.append((k, v))
        return lst


def printingHoursByLine(sortByHours):
    lst = sorted(sortByHours)
    for hour in lst:
        print(hour)


def main():
    fhand = openFile('mbox.txt')
    s = searchForTimeInLine(fhand)
    h = hourFromTime(s)
    print(sortByHours(h))
    fhand.close()


main()
