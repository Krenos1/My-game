import pygame
from pygame.locals import *
# from pygame.sprite import _Group
import button
import random
## 3 aspect important 

##-la fenetre de jeu
##-la loop du jeu
##-et le event handler¸




pygame.init()

# Variable qui constitue la longueur et la largeur de l'écran de jeu
ScreenWidth = 1104
ScreenHeight = 624
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Main Menu")

# Les Frames par secondes
FPS = pygame.time.Clock()
FPS.tick(60)

# Vérification de collision
# object1 = pygame.Rect((20, 50), (50,100))
# object2 = pygame.Rect((10, 10), (100, 100))
# print(object1.collidepoint(50, 75))

# Préchargement des buttons +besoin de convert alpha 9probablement a des fin d'optimisation
ImageStart = pygame.image.load("Images/ButtonStart.png").convert_alpha()

# Créer des instances de buttons
imgScale = 4
ButtonStart = button.Button(304, 125, ImageStart, imgScale)

# Définition des couleurs
TextColor = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Définiton des fonts et de sont font size en paramètre
Font = pygame.font.SysFont("arialblack", 40)

# fonction
def DrawText(text, font, TextColor, x, y):
    img = font.render(text, True, TextColor)
    Screen.blit(img,(x, y))

# Déclaration de variable
GameEXE = True
Running = True
GamePaused = False
MessagePause = "Press SPACE to pause"


Player1 = pygame.Rect((300, 250, 50, 50))

# Lopp qui permet au jeu de conitnuer à run

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Images/ButtonStart.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,ScreenWidth-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.top > 624):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/Johnathan.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < ScreenWidth:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     


P1 = Player()
E1 = Enemy()

# Départ de la loop du jeu
while GameEXE == Running:
    
    
    # Vérifier si le jeu est en pause
    if GamePaused == True:
        ButtonStart.draw(Screen)
    #Affichage du menu
    else:
        # Utilisation de fonction pour écriture de texte + les paramètre en ordre, 
        # message, le fontsize, coleur texte et l'emplacement x et y sur l'axe
        DrawText(MessagePause, Font, TextColor, 160, 250)

    # pygame.draw.rect(Screen, (255,0,0), Player1)
    # Attribution du mouvement de Player1 au touche [W,A,S,D]
    Key = pygame.key.get_pressed()
    ## if Key[pygame.K_a] == True:
    #     Player1.move_ip(-1, 0)
    # elif Key[pygame.K_d] == True:
    #     Player1.move_ip(1, 0)
    # elif Key[pygame.K_w] == True:
    #     Player1.move_ip(0, -1)
    # elif Key[pygame.K_s] == True:
    #     Player1.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                GamePaused = True
                print("Paused")
        if event.type == QUIT:
            Running = False
            pygame.quit()
    P1.update()
    E1.update()
# Permet à l'écran de refresh
    Screen.fill((128,128,91))
    P1.draw(Screen)
    E1.draw(Screen)

    pygame.display.update()
    FPS.tick(60)




