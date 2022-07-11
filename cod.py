# podana_wartosc = input("tutaj jest komunikat, ktory jest wyswietlany uzytkownikowi przed podaniem wartosci") # podaj string
# podana_wartosc = str(input("podaj imię\n"))


class atakMieczem:
    def __repr__(self) -> str:
        return "atak mieczem"


class atakpiescia:
    def __repr__(self) -> str:
        return "atak piescią"


class unik:
    def __repr__(self) -> str:
        return "unik"


class blokMiczem:
    def __repr__(self) -> str:
        return "blok mieczem"


class atakNoga:

    def __repr__(self) -> str:
        return "atak noga"


ataki = [atakpiescia(), atakNoga(), atakMieczem(), blokMiczem(), unik()]

hp_b = 100
hp_p = 120

while hp_b >= 0 and hp_p >= 0:
    wybor = int(input("czym chcesz uderzyc albo czym chcesz sie obronic\n" + str(ataki) + "\n"))
    atak = ataki[wybor]
    print(atak)
    if wybor < 3:
        hp_p -= 50

print("koniec gry")

if __name__ == '__main__':
    pass
