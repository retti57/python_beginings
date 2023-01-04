def read_from_file(to_do):
    file = open("To_do_list.txt", mode="r", encoding="windows-1250")
    for task in file:
        t = task.strip()
        to_do.append(t)
    file.close()
    print(to_do)

def output_list(to_do):
    print(to_do)


def append_to_list(to_do):
    to_do.append(input("Dodaj zadanie: "))


def delete_task(to_do): #  wyjątek , index większy niż długość listy  IndexError
    i = -1
    for task in to_do:
        i += 1
        print(task, "[", i, "]", sep=' ')
    task_index = int(input("wybierz index zadania na liście: "))
    print(f"usunięto: {to_do.pop(task_index)}")


def write_to_file(to_do):
    file = open("To_do_list.txt", mode="w+", encoding="windows-1250")
    for task in to_do:
        file.write(task + '\n')
    file.close()


def save_and_exit(to_do):
    write_to_file(to_do)
    exit()


def main():
    to_do = []
    user_choice = -1
    while user_choice != 6:
        if user_choice == 1:
            output_list(to_do)
        elif user_choice == 2:
            append_to_list(to_do)
        elif user_choice == 3:
            delete_task(to_do)
        elif user_choice == 4:
            write_to_file(to_do)
        elif user_choice == 5:
            save_and_exit(to_do)
        elif user_choice == 0:
            read_from_file(to_do)  #  dodaje do listy ponownie
        elif 6 < user_choice < 0:
            print("wartość spoza zakresu")
        print("0. Wczytaj i wyświetl zadania z pliku")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zapisz do pliku")
        print("5. Wyjście i zapisanie zmian")
        print("6. Wyjście")
        user_choice = int(input("Wybierz liczbe: "))  #  wyjątek gdy inna wartość niż INT ValueError
    return to_do


main()