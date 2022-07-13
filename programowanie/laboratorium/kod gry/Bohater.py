import pygame
from Postac import Postac

class Bohater(Postac):
    def __init__(self, nazwa, wyglad):
        super().__init__(wyglad, "lokalizacja", "statystyki", nazwa, "cechy", "dialogi")
        
    def chodz(self, event):
         if event.type == pygame.KEYDOWN:
            super().lokalizacja.aktualizuj(event.key)

         if event.type == pygame.KEYUP:
            super().lokalizacja.aktualizuj(event.key)
        
    def interakcja(self,typ):
        pass

    def wyrzucanie_rzeczy(self,id):
        pass

