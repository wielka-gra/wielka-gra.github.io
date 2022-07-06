import random


class Polewa_czekoladowa:
    '''
    ważne metody:
        pokaz_przepis,
        status,
        dodaj,
        podgrzej,
        dodaj

    '''
    def __init__(self):
        self._problemy = False
        self._skladniki = ["smietana30%", "czekolada"]

        self._sposob_przygotowania = {
            "dodaj smietana30%": False,
            "podgrzej": 0,
            # "pokrusz czekolade": False,
            "dodaj czekolade": False
        }

    def podgrzej(self):
        self._sposob_przygotowania['podgrzej'] += 3
        if self._sposob_przygotowania["dodaj smietana30%"] == True:
            if self._sposob_przygotowania["podgrzej"] > 83:
                print("smietana sie zwazyla")
                self._problemy = True

    def dodaj(self, skladnik):
        instrukcja = "dodaj " + skladnik
        self._sposob_przygotowania[instrukcja] = True
        print(skladnik + " dodany pomyslnie")
        if skladnik == "czekolada":
            self._sposob_przygotowania["podgrzej"] -= random.random() * 25

    def status(self):
        for instrukcja in self._sposob_przygotowania:
            if self._sposob_przygotowania[instrukcja] == False:
                print("potrawa nie jest gotowa")
                return False
            if self._sposob_przygotowania["podgrzej"] >= 80 and self._problemy == False:
                print("polewa jest gotowa")
                return True

    def pokaz_przepis(self):
        print("lista składnikow: ")
        print(self._skladniki)
        print()
        print("sposob przygotowania: ")
        print(self._sposob_przygotowania.keys())
        print("na koniec wszystko podgrzej do conajmniej 80 stopni, aby czekolada, sie roztopila")
        print("")
