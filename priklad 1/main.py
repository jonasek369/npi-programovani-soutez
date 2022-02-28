# uvedena hodnota přes kterou program nepujde
fibonacci_max = 1000


def fibonacci() -> None:
    a = 1
    b = 1
    # proměná listu kterou potom uložim do souboru
    fibb_list = []
    while b < fibonacci_max:
        print(a)
        fibb_list.append(a)
        a = a + b
        print(b)
        fibb_list.append(b)
        b = a + b

    # ukladani do souboru
    try:
        with open("fibonacci.txt", "w") as file:
            file.write(str(fibb_list))
        print("Soubor fibonacci.txt se uložil úspěšně")
    except:
        print("Nepodařilo se uložit soubor fibonacci.txt")

fibonacci()
