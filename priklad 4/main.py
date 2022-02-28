import random


def vytvorit_novy_hashtable() -> dict:
    # vytovorím 2 proměné s listem cisel pismen atd.
    # potom letters_shuffled nahodně promíchám a vytvorim dict
    # do ktereho dam pismeno na indexu z letters a letters_shuffled
    letters = list("qwertzuiopasdfghjklyxcvbnm+ěščřžýáíé=´0123456789QWERTZUIOPASDFGHJKLYXCVBNMĚŠČŘŽÝÁÍÉł ")
    print(letters)

    letters_shuffled = list("qwertzuiopasdfghjklyxcvbnm+ěščřžýáíé=´0123456789QWERTZUIOPASDFGHJKLYXCVBNMĚŠČŘŽÝÁÍÉł ")

    for x in range(4):
        # random.shuffle náhodně promíchá dany objekt
        random.shuffle(letters_shuffled)

    return {letters[x]: letters_shuffled[x] for x in range(len(letters))}


# předvytvoření hashtable na zakodovani zprávy da se vytvořit s funkcí vytvorit_novy_hashtable()
hashtable = {'q': 'P', 'w': 'Ě', 'e': 'u', 'r': 'o', 't': 'y', 'z': 'Q', 'u': '0', 'i': 'ł', 'o': 'Í', 'p': 'U',
             'a': 'g', 's': 'T', 'd': 'i', 'f': 'F', 'g': 'O', 'h': 'z', 'j': 'f', 'k': ' ', 'l': 'š', 'y': 'E',
             'x': 'Ř', 'c': '4', 'v': 'R', 'b': 'p', 'n': 'H', 'm': 'm', '+': 'h', 'ě': 'á', 'š': 'Ý', 'č': '3',
             'ř': 'é', 'ž': 'r', 'ý': 'x', 'á': 'a', 'í': 'q', 'é': 'b', '=': 'ě', '´': 'd', '0': '7', '1': 'e',
             '2': 'A', '3': 'w', '4': 'Á', '5': 'Ž', '6': 'í', '7': 's', '8': '´', '9': '5', 'Q': 'Z', 'W': '1',
             'E': 'N', 'R': 'C', 'T': 'M', 'Z': 'W', 'U': 'Š', 'I': 'č', 'O': 'I', 'P': '8', 'A': 'Y', 'S': 'ý',
             'D': 'V', 'F': 'G', 'G': 'n', 'H': 'J', 'J': 'ž', 'K': 'É', 'L': 'S', 'Y': 'l', 'X': '2', 'C': '+',
             'V': 'k', 'B': '=', 'N': 'D', 'M': '6', 'Ě': 't', 'Š': 'j', 'Č': 'ř', 'Ř': 'B', 'Ž': '9', 'Ý': 'v',
             'Á': 'c', 'Í': 'K', 'É': 'L', 'ł': 'X', ' ': 'Č'}


def zakodovat(veta) -> str:
    if veta is None or veta == "":
        veta = input("Zadejte větu: ")
    # každé písmeno věty bude vyhledané pod proměný hashtalbe takže např. "w" se zmeni na "Ě"
    zakodovana = "".join((hashtable[pismeno] for pismeno in veta))
    print(f"zakodovaná zpráva: {zakodovana}")
    return zakodovana


def dekodovat(kodovana_veta) -> str:
    if kodovana_veta is None or kodovana_veta == "":
        kodovana_veta = input("Zadejte kodovanou větu: ")
    keys = list(hashtable.keys())
    values = list(hashtable.values())
    # ziskam index každého pismena v kodovane vetě a potom ho vyhledam v proměné keys např. "g" se zmeni na "a"
    dekdovana = "".join([keys[values.index(pismeno)] for pismeno in kodovana_veta])
    print(f"dekodovana zpráva: {dekdovana}")
    return dekdovana


dekodovat(zakodovat(""))
