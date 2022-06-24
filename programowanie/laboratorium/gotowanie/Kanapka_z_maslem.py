import random


class Kanapka_z_maslem:
    '''
    ważne metody:
        pokaz_przepis,
        status,
        ukroj,
        posmaruj,
    '''
    def __init__(self):
        self._problemy = False
        self._skladniki = ["chleb", "maslo"]

        self._sposob_przygotowania = {
            "ukroj kromke": False,
            "posmaruj": 0,
        }

    def ukroj(self):
        self._sposob_przygotowania["ukroj kromke"] = True
        print("Ale równiutko!")

    def posmaruj(self):
        smarowanie = self._sposob_przygotowania["posmaruj"]
        smarowanie+= 1
        
        if smarowanie > 4:
            print("Wiecej masla niz kanapki")

    def status(self):
        if self._sposob_przygotowania["ukroj kromke"] == False:
            print("potrawa nie jest gotowa")
            return False
        if self._sposob_przygotowania["posmaruj"] >= 2:
            print("Smacznego! ")
            return True

    def pokaz_przepis(self):
        print("lista składnikow: ")
        print(self._skladniki)
        print()
        print("sposob przygotowania: ")
        print(self._sposob_przygotowania.keys())
        print("")



        # smarowanie = self._sposob_przygotowania
        # smarowanie["posmaruj"] += 1
        # print(smarowanie)