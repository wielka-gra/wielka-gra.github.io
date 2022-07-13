class Lokalizacja:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    def aktualizuj(self, key, type):
        
        if type == "pygame.KEYDOWN":
            if key == pygame.K_LEFT:
                self.left_pressed = True
            if key == pygame.K_RIGHT:
                self.right_pressed = True
            if key == pygame.K_UP:
                self.up_pressed = True
            if key == pygame.K_DOWN:
                self.down_pressed = True
                
        if type == "pygame.KEYUP":
            if event.key == pygame.K_LEFT:
                self.left_pressed = False
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False
            if event.key == pygame.K_UP:
                self.up_pressed = False
            if event.key == pygame.K_DOWN:
                self.down_pressed = False

