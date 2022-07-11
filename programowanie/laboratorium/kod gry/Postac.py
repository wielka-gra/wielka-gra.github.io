import pygame.sprite


class Postac(pygame.sprite.Sprite):
    def __init__(self, wyglad, lokalizacja, statystyki, nazwa, cechy, dialog):
        self._wyglad = wyglad
        self._lokalizacja = lokalizacja
        self._statystyki = statystyki
        self._nazwa = nazwa
        self._cechy = cechy
        self._dialog = dialog