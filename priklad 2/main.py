# Ukladam mesice v proměných listech aby jsem nemusel dělat zbytečně dlouhé if statmenty
jaro = [2, 3, 4]
leto = [5, 6, 7]
podzim = [8, 9, 10]
zima = [11, 12, 1]


def mesice():
    mesic = 6
    if mesic in jaro:
        print("Je jaro")
    elif mesic in leto:
        print("Je léto")
    elif mesic in podzim:
        print("Je podzim")
    elif mesic in zima:
        print("Je zima")
    else:
        print("Špatně zadaný měsíc")


mesice()
