from typing import Any
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
        self.rect.center = (450,500)
        self.speed_x= 0
        self.speed_y= 0

    def update(self):
        self.speed_x=0
        self.speed_y=0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.speed_x = -10
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.speed_x = 10
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed_y = -10
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed_y = 10

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


        if self.rect.left< 0:
            self.rect.left = 0
        if self.rect.right > Swidth:
            self.rect.right = Swidth
        if self.rect.bottom > Sheight:
            self.rect.bottom = Sheight
        if self.rect.top < 0:
            self.rect.top = 0
        


class start():
    pygame.init()


clock = pygame.time.Clock()
Player = pygame.sprite.Group()
players = player()
Player.add(players)


screen= pygame.display.set_mode((Swidth,Sheight))
pygame.display.set_caption("My Spaceship Game")

background = pygame.transform.scale(pygame.image.load('assets/galaxy-background.jpg').convert(),(900,600))



running =True

while running:
    clock.tick(FPS)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Player.update()
    Player.draw(screen)
    pygame.display.flip()