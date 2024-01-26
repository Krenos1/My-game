import pygame
from sys import exit 

#Fonction qui permet d'afficher le score du joueur 
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = testFont.render(f'{current_time}',False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

#Permet le début de ma loop qui permet le fonctionnement du jeu 
game = True
#GameAcitve permet de savoir si le jeu est en pause ou non 
gameActive = True 

start_time = 0
testFont = pygame.font.Font("TestSprites/Pixeltype.ttf", 50)
testSurface = pygame.Surface((100,200))
# testSurface.fill('Red')
skySurface = pygame.image.load('TestSprites/Sky.png').convert()
groundSurface = pygame.image.load('TestSprites/ground.png').convert()

#Transforme font en surface
# scoreSurf = testFont.render("My game", False, (64,64,64))
# scoreRect = scoreSurf.get_rect(center = (400, 50))

snailSurface = pygame.image.load("TestSprites/snail1.png").convert_alpha()
snailRect = snailSurface.get_rect(midbottom = (600,300))

playerSurf = pygame.image.load('TestSprites/player_walk_1.png').convert_alpha()
playerRect = playerSurf.get_rect(midbottom = (80,300))

#control de la gravité
playerGravity = 0


while game == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        ## Mouse collision dans la event loop
        # if event.type == pygame.MOUSEMOTION:
        #     if playerRect.collidepoint((event.pos)):
                # print('trouvé')
        # keyboard input in the event loop
        # if event.type == pygame.KEYDOWN:
        if gameActive == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerRect.bottom >= 300:
                    playerGravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerRect.collidepoint(event.pos):
                    playerGravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True  
                snailRect.left = 800
                start_time = pygame.time.get_ticks()
    
    if gameActive == True:    
        screen.blit(skySurface,(0,0))
        screen.blit(groundSurface,(0,300))
        display_score()

        # pygame.draw.rect(screen, '#c0e8ec', score_rect)


        # pygame.draw.line(screen,'Gold',(0,0),(800,400), 10)
        # screen.blit(score_surf,score_rect)
        
        ##vitesse du snail
        # snail_x_pos -= 3
        # if snail_x_pos < -100:
        #     snail_x_pos = 800

        snailRect.left -= 4
        if snailRect.right <= 0:
            snailRect.left = 800

        screen.blit(snailSurface, snailRect)
        # playerRect.left += 1

        # player
        playerGravity += 1
        playerRect.y += playerGravity
        if playerRect.bottom >= 300:
            playerRect.bottom = 300
        screen.blit(playerSurf, playerRect)
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        # if playerRect.colliderect(snailRect):
        #     print("trouvé")
        
        # mousePos = pygame.mouse.get_pos()
        # if playerRect.collidepoint((mousePos)):
        #     print(pygame.mouse.get_pressed())

        # collision
        if snailRect.colliderect(playerRect):
            gameActive = False
    
    else:
        screen.fill('Green')

    pygame.display.update()
    #Rafraichissement de l'ecran par seconde
    clock.tick(60)