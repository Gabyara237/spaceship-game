import pygame

Swidth= 900
Sheight= 600
FPS= 60

clock=pygame.time.Clock()

class start():
    pygame.init()


screen= pygame.display.set_mode((Swidth,Sheight))
pygame.display.set_caption("My Spaceship Game")
#
background = pygame.transform.scale(pygame.image.load('assets/galaxy-background.jpg').convert(),(900,600))

running =True

while running:
    clock.tick(FPS)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()