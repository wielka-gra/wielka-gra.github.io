class Lokalizacja:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    def aktualizuj(self):
        if event.key == pygame.K_LEFT:
            self.left_pressed = True
        if event.key == pygame.K_RIGHT:
            self.right_pressed = True
        if event.key == pygame.K_UP:
            self.up_pressed = True
        if event.key == pygame.K_DOWN:
            self.down_pressed = True

