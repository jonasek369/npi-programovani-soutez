def prvocislo():
    try:
        cislo = float(input("zadejte čislo: "))
        # if cislo <= 0 or cislo == 1:
        if cislo <= 0:
            print(f"{cislo} není prvočíslo")
            exit()
        if not cislo % 1 == 0:
            print(f"{cislo} není prvočíslo")
            exit()
        if not cislo % cislo == 0:
            print(f"{cislo} není prvočíslo")
            exit()

        # zkontroluje čislo jestli je dělitelné s čislem  1 - 9 pomocí % (modularu) ktery vrati zbytkovou
        # hodnotu po dělení když to je 0 tak vím že čislo je tim to dělitelem dělitelné
        for delitel in range(1, 10):
            if delitel == 1 or delitel == cislo:
                continue
            if cislo % delitel == 0:
                print(f"{cislo} není prvočíslo")
                exit()
        print(f"{cislo} je prvočíslo")
    except ValueError:
        print("Toto není číslo")

prvocislo()


def prvocislo():
    if cislo <= 0 or cislo == 1:
        return False
    if not cislo % 1 == 0:
        print(f"{cislo} není prvočíslo")
        exit()
    if not cislo % cislo == 0:
        print(f"{cislo} není prvočíslo")
        exit()

    # zkontroluje čislo jestli je dělitelné s čislem  1 - 9 pomocí % (modularu) ktery vrati zbytkovou
    # hodnotu po dělení když to je 0 tak vím že čislo je tim to dělitelem dělitelné
    for delitel in range(1, 10):
        if delitel == 1 or delitel == cislo:
            continue
        if cislo % delitel == 0:
            print(f"{cislo} není prvočíslo")
            exit()
    print(f"{cislo} je prvočíslo")
