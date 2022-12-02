try:
    fhand = open('ang2pol.txt', mode = 'a', encoding = 'UTF-8')  # metoda 'a' - dodaje na koniec do pliku
    while True:
        sth = input('Czy chcesz coś dodać?: ')
        if sth == 'nie' or sth == 'n' or sth == 'n' or sth == 'no':
            print('Nic nie dodajesz.')
            break
        elif sth == 'tak' or sth == 't' or sth == 'y' or sth == 'yes':
            ang = input('Podaj angielskie słówko: ')
            pol = input('Podaj polskie tłumaczenie: ')
            fhand.write(f"{ang}, {pol}, ")
            continue
        else:
            print('Niewłaściwe polecenie!\n')
            print('Podaj "tak" lub "yes" jeśli chcesz coś dodać.\nAlbo "nie", "not", "no" jeśli nie.')
            continue
    print('Wykonuje poza pętlą while')
finally:
    print("zamykam bo finally")
    fhand.close()

