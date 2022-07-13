import random


class atakMieczem:
    def losowy_dmg(self):
        dmg = random.randint(0, 5)
        return dmg

    def __repr__(self) -> str:
        return "atak mieczem"


class atakpiescia:
    def losowy_dmg(self):
        dmg = random.randint(0, 5)
        return dmg

    def __repr__(self) -> str:
        return "atak piescią"


class unik:
    def __repr__(self) -> str:
        return "unik"


class blokMiczem:
    def __repr__(self) -> str:
        return "blok mieczem"


class atakNoga:
    def losowy_dmg(self):
        dmg = random.randint(0, 5)
        return dmg

    def __repr__(self) -> str:
        return "atak noga"


ataki = [atakpiescia(), atakNoga(), atakMieczem(), blokMiczem(), unik()]

hp_b = 50
hp_p = 20


def zadawanie_obrazen(hp, dmg):
    print("obrarzenia", dmg)
    hp = hp - dmg
    print("zdrowie", hp)
    return hp


while hp_b > 0 and hp_p > 0:
    wybor = 5
    while wybor > 4:
        wybor = int(input("czym chcesz uderzyc albo czym chcesz sie obronic\n" + str(ataki) + "\n"))
    atak = ataki[wybor]
    print(atak)
    if wybor < 3:
        print("bohater:")
        dmg = atak.losowy_dmg()
        hp_p = zadawanie_obrazen(hp_p, dmg)
        # teraz misiek nas leje
        szansa_na_uderzenie = random.randint(0, 100)

        #niedzwiedz nas bije
        if szansa_na_uderzenie > 50:
            print("\nPotwor:")
            hp_b = zadawanie_obrazen(hp_b, 10)
    else:
        pass

if hp_b <= 0:
    print("przegrales")
if hp_p <= 0:
    print("wygrales")


if __name__ == '__main__':
    pass
