import random


class Tort:
    '''
    wazne
    '''
    def __init__(self, polewa):
        self.skladniki = ["biszkopt", polewa]

        self.sposob_przygotowania = {
            "udekoruj biszkopt": False
        }

    def dekoruj(self, wzor):
        if self.skladniki[1] is None:
            print("Bez masy nie udekorujemy ciasta...")
            return False

        znaki = ['/', '*', '(', '=', '\\', ')', '-', '_', '#']

        if wzor[1][len(wzor[1]) // 2] != znaki[3]:
            print(2)
            return self.krytyka()

        if wzor[1][len(wzor[1]) // 2 - 1] != znaki[1] or wzor[1][len(wzor[1]) // 2 - 1] != znaki[1]:
            print(3)
            return self.krytyka()

        if wzor[1][2] != znaki[2] or wzor[2][len(wzor[2]) // 2 - 1] != znaki[2]:
            return self.krytyka()

        if wzor[1][-3] != znaki[5] or wzor[2][len(wzor[2]) // 2 + 1] != znaki[5]:
            return self.krytyka()

        if wzor[1][1] != znaki[4] or wzor[1][-2] != znaki[0]:
            return self.krytyka()

        if wzor[3][len(wzor[3]) // 2 - 1] != znaki[0] or wzor[3][len(wzor[3]) // 2 + 1] != znaki[4]:
            return self.krytyka()

        if wzor[3][3] != znaki[-2] or wzor[3][-4] != znaki[-2]:
            return self.krytyka()

        self.sposob_przygotowania["udekoruj biszkopt"] = True
        print("Lepiej nie mozna bylo udekorowac!")

    def krytyka(self):
        print("Wzor nie spelnia standartow, ")
        self.skladniki[1] = None
        return False

    def status(self):
        if self.sposob_przygotowania["udekoruj biszkopt"] == True:
            print("Tort jest gotowy!")
            return True
        else:
            print("Tort nie jest gotowy")
            return False

    def pokaz_przepis(self):
        print("lista składnikow: ")
        print(self.skladniki)
        print("sposob przygotowania: ")
        print(self.sposob_przygotowania.keys())
        print("")
