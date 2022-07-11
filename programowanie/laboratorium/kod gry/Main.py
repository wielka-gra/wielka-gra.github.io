import pygame
import Postac
import Bohater
running = True
bohater = Bohater("nazwa")
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False







def menu(wybor):
  match wybor:
    case "1":
      return ""
    case "":
      return ""
    case "2":
      return ""