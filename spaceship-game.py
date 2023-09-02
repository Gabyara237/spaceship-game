import pygame
from pygame.sprite import Group

Swidth= 900
Sheight= 600
FPS= 60

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('assets/spaceships-player.png')
        self.rect = self.image.get_rect()
        self.rect.center=(450,500)


class start():
    pygame.init()


clock = pygame.time.Clock()
Player = pygame.sprite.Group()
players = player()
Player.add(players)


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
    Player.draw(screen)
    pygame.display.flip()