from random import randint

los = randint(1,10)
odp = -1
i = 0
print("Zgadnij liczbę z przedziału od 1 do 10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Wylosowana liczba jest mniejsza od twojej")
    elif odp < los:
        print("Wylosowana liczba jest większa od twojej")
print("Braawo, odgadłeś za", i, "razem.")