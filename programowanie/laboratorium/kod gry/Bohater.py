import pygame

import Postac

class Bohater(Postac):
    def __init__(self, nazwa):
        super().__init__("wyglad.jpg", "lokalizacja", "statystyki", nazwa, "cechy")

    def chodz(self, event):
        if event.type == pygame.KEYDOWN:
            super().lokalizacja.aktualizuj(event.key)

        if event.type == pygame.KEYUP:
            super().lokalizacja.aktualizuj(event.key)

    def interakcja(self,typ):
        pass

    def wyrzucanie_rzeczy(self,id):
        pass

