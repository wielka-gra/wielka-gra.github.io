import random


class Nalesniki():
    '''
    wazne metody:
        pokaz_przepis,
        status,
        wymieszaj,
        wbij_jajko,
        napraw,
        dodaj,
    '''

    def __init__(self):
        self._problemy = {"skorupki": 0}
        self._skladniki = ["maka", "mleko", "woda", "olej", "jajko"]

        self._sposob_przygotowania = {
            "dodaj maka": False,
            "dodaj mleko": False,
            "dodaj woda": False,
            "dodaj olej": False,
            "wbij jajko": False,
            "wymieszaj": False,
            "usmaz": 0,
        }

    @property
    def skladniki(self):
        return self._skladniki

    def wymieszaj(self):
        for instrukcja in self._sposob_przygotowania:
            if instrukcja == "wymieszaj":
                break
            if self._sposob_przygotowania[instrukcja] == False:
                return
        self._sposob_przygotowania["wymieszaj"] = True
        print("potrawa zostala wymieszana")

    def wbij_jajko(self):
        self._sposob_przygotowania["wbij jajko"] = True
        print("wbito jajko")

        if random.random() < 0.7:
            self._problemy["skorupki"] += 1
            print("wpadla skorupka. Aby sie jej pozbyc skorzystaj z 'napraw()'")
            return False
        return True

    def napraw(self):
        if random.random() > 0.8:
            self._problemy["skorupki"] -= 1
            print("udalo sie wyjac skorupke!")
            return True
        print("skorupka wciaz tkwi w ciescie. sprobuj ponownie ja wylowic")
        return False

    def dodaj(self, skladnik):
        instrukcja = "dodaj " + skladnik
        self._sposob_przygotowania[instrukcja] = True
        print(skladnik + " dodany pomyslnie")

    def usmaz(self):
        for instrukcja in self._sposob_przygotowania:
            if instrukcja == "usmaz":
                break
            if self._sposob_przygotowania[instrukcja] == False:
                print("cos poszlo nie tak...")
                print("sprobuj ponownie :)")
                return

        if self._sposob_przygotowania["usmaz"] < 12:
            self._sposob_przygotowania["usmaz"] += 1
            print(self._sposob_przygotowania["usmaz"], "nalesnik usmazony")
        else:
            print('brak ciasta')

    def status(self):
        for instrukcja in self._sposob_przygotowania:
            if self._sposob_przygotowania[instrukcja] == False:
                print("potrawa nie jest gotowa")
                return False
        if self._sposob_przygotowania["usmaz"] == 10:
            if self._problemy["skorupki"] == 0:
                print("potrawa jest gotowa! :) ")
                return True
            else:
                print("teoretycznie jadalne, ale cos chrupie")
                return True
        else:
            print("zostalo ciasto do usmazenia")
            return False

    def pokaz_przepis(self):
        print("lista składnikow: ")
        print(self._skladniki)
        print()
        print("sposob przygotowania: ")
        print(self._sposob_przygotowania.keys())
        print("")
