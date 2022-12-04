
def openFile(filename: str):
    return open(filename, mode='r+', encoding='UTF-8')  # metoda 'a' - dodaje na koniec do pliku


def readDataFromFileToDictionary(file):
    temporaryDict = dict()
    for line in file:
        ln = line.split(',')
        temporaryDict[ln[0]] = ln[1]
    return temporaryDict


def readNewWords(localDict):
    newWords = dict()
    sth = input('Czy chcesz coś dodać?: ')
    approvedChoice = ['tak', 't', 'y', 'yes']
    while sth in approvedChoice:
        ang = input('Podaj angielskie słówko: ')
        pol = input('Podaj polskie tłumaczenie: ')
        addNewWordIfNotExist(ang,pol, localDict, newWords)
        sth = input('Czy chcesz coś dodać?: ')
    return newWords


def addNewWordIfNotExist(ang,pol,localDict,newWords):
    if ang not in localDict:
        newWords[ang] = pol


def saveNewWordsInFile(file, words):
    for word in words:
        file.write(f"{word},{words[word]}\n")


def main():
    file = openFile("ang2pol.txt")
    localDict = readDataFromFileToDictionary(file)
    nnew = readNewWords(localDict)
    saveNewWordsInFile(file, nnew)
    file.close()


main()
