from audioop import cross
import random
from re import T
from string import hexdigits
import pygame, sys

class Zaba(pygame.sprite.Sprite):
    def __init__(self,picture_path,x,y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.animalSound = pygame.mixer.Sound("mutant_frog-1.ogg")

        self.x = int(x)
        self.y = int(y)
        self.velX = 0
        self.velY = 0

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.speed = 4

    def sound(self):
            self.animalSound.play()
    def update(self):
        self.velX = 0
        self.velY = 0

        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed 

        self.x += self.velX
        self.y += self.velY
        
        self.rect = pygame.Rect(self.x, self.y, 3, 3) #zasieg

class Skladnik(pygame.sprite.Sprite):
    def __init__(self,picture_path, poz_x,poz_y):
        super().__init__()
        self.image = pygame.image.load(picture_path).convert_alpha() #ustawienie obrazka 
        self.rect = self.image.get_rect()
        self.rect.center = [poz_x,poz_y] #ustawienie na pozycji w oknie

class Salatka():
    '''
    wazne metody:
        pokaz_przepis,
        status,
        zbierz_skladniki
    '''
    def __init__(self):
        self._skladniki = ["egg_fried.png", "french_fries.png","blueberries.png","cauliflower.png","avocado_half.png","bell_pepper_red.png"]

        self._sposob_przygotowania = {
            "zbierz skladniki": False,
            "zrob sałatke":False
        }

    @property
    def skladniki(self):
        return self._skladniki

    def status(self):
        pass

    def pokaz_przepis(self):
        print("lista składnikow: ")
        print(self._skladniki)
        print()
        print("sposob przygotowania: ")
        print(self._sposob_przygotowania.keys())
        print("")

    def zbierz_skladniki(self): 
        #general setup
        TITLE = "Żabi łów"
        pygame.display.set_caption(TITLE)
        pygame.init()
        clock = pygame.time.Clock()

        # game screen
        screen_width = 300
        screen_height = 250
        screen = pygame.display.set_mode((screen_width,screen_height)) #ustawienie wielkosci ekranu
        background = pygame.image.load("clouds.png") #ustawienie tła
        pygame.mouse.set_visible(False) #ustawienie widoczności myszki

        #Zaba
        zaba = Zaba("froggy.png",screen_width/2, screen_height/2)
        zaba_group = pygame.sprite.Group()
        zaba_group.add(zaba)

        #Skladnik
        skladnik_group = pygame.sprite.Group()

        # początkowe umiejscowienie jednego składnika na tle
        rand = random.randrange(0,len(self._skladniki)) #wylosowana pozycja składnika ze skladnik_list
        new_skladnik = Skladnik(self._skladniki[rand],random.randrange(0,screen_width),random.randrange(0,screen_height)) #losujemy przyszłą pozycję składnika
        skladnik_group.add(new_skladnik) 
        self._skladniki.pop(rand) #usuwamy z listy pozostałych do zebrania składników

        while len(self._skladniki) > 0:
            for event in pygame.event.get(): #event - jakies klikniecie
                if event.type == pygame.QUIT: #jesli kliknieto "X"
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN: #jesli przycisnieto klawisz
                    if event.key == pygame.K_LEFT:
                        zaba.left_pressed = True
                    if event.key == pygame.K_RIGHT:
                        zaba.right_pressed = True
                    if event.key == pygame.K_UP:
                        zaba.up_pressed = True
                    if event.key == pygame.K_DOWN:
                        zaba.down_pressed = True

                if event.type == pygame.KEYUP:  #jesli puszczono klawisz
                    if event.key == pygame.K_LEFT:
                        zaba.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        zaba.right_pressed = False
                    if event.key == pygame.K_UP:
                        zaba.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        zaba.down_pressed = False

                collide = pygame.sprite.spritecollide(zaba,skladnik_group,True) #jesli żaba najedzie na składnik, to składnik znika, jednoczesnie funkcja zwraca true/false
                if collide: #jesli collide == true
                    zaba.sound()

                    #generacja kolejnego składnika do sałatki
                    if len(self._skladniki) > 0:
                        rand = random.randrange(0,len(self._skladniki))
                        new_skladnik = Skladnik(self._skladniki[rand],random.randrange(0,screen_width),random.randrange(0,screen_height)) #umieszenie składnika w oknie
                        skladnik_group.add(new_skladnik)
                        self._skladniki.pop(rand) #pomiejszanie listy pozostałych skladników
            
            pygame.display.flip() # rysowanie rzeczy na tle
            screen.blit(background,(0,0)) # rysowanie tla
            skladnik_group.draw(screen) # umieszczenie wszystkich skladnikow ze skladnik_group w oknie gry
            zaba_group.draw(screen) # umieszczenie żaby
            zaba_group.update() # zmiana pozycji żaby na ekranie
            clock.tick(60) # max czestotliwosc odswiezania ekranu

        pygame.time.wait(900)
        pygame.quit()
        sys.exit()


