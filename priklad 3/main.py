def obsah() -> int or float:
    try:
        a = float(input("Zadejte velikost strany a: "))
        b = float(input("Zadejte velikost strany b: "))

        obsah = 2 * (a * b)

        print(f"Obsah obdélníku je {obsah}")
        return obsah
    except ValueError:
        print("Toto není číslo")


obsah()
