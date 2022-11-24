print('Wprowadź liczbę. Zakończ słowem "gotowe"')
a = list()
while True:
    try:
        inp = input()
        b = inp.strip()
        if b == "gotowe":
            break
        elif b == "":
            continue
        else:
            bint = int(b)
            add = a.append(bint)
    except ValueError:
        print("Błędna wartość")
for i in a:
    c = max(a)
    d = min(a)
print(f"Największa:{c}")
print(f"Najmniejsza:{d}")
