import pygame.sprite
import pygame


class Postac(pygame.sprite.Sprite):
    def __init__(self, wyglad, lokalizacja, statystyki, nazwa, cechy, dialog):
        super().__init__()
        self.image = pygame.image.load(wyglad).convert()
        self.rect = self.image.get_rect()
        self._lokalizacja = Lokalizacja(lokalizacja)
        self._statystyki = statystyki
        self._nazwa = nazwa
        self._cechy = cechy
        self._dialog = dialog