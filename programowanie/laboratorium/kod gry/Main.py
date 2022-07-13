import pyautogui
import pygame
from Bohater import Bohater


pygame.init()
clock = pygame.time.Clock()

width, height= pyautogui.size()
screen = pygame.display.set_mode((width-150, height)) 

bohater = Bohater("nazwa", "froggy.png")
all_sprites = pygame.sprite.Group()
all_sprites.add(bohater)

running = True
clock.tick(60)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.flip()
  all_sprites.draw(screen)
 




def menu(wybor):
  if wybor=="1":
      return ""
  elif wybor=="2":
      return ""