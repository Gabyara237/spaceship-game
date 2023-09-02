from typing import Any
import pygame
from pygame.sprite import Group
from enemy import enemy
from fire import fire

Swidth= 900
Sheight= 600
FPS= 60


class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('assets/spaceships-player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (450,550)
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
        if keys[pygame.K_SPACE]:
            self.shots()
            self.shots2()

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Swidth:
            self.rect.right = Swidth
        if self.rect.bottom > Sheight:
            self.rect.bottom = Sheight
        if self.rect.top < 0:
            self.rect.top = 0
    
    def shots(self):
        shot= fire(self.rect.centerx -40, self.rect.centery +15 )
        Shots.add(shot)
    def shots2(self):
        shot= fire(self.rect.centerx +40, self.rect.centery +15)
        Shots.add(shot)

        


class start():
    pygame.init()


clock = pygame.time.Clock()

# Sprites

Player = pygame.sprite.Group()
Shots = pygame.sprite.Group()
Enemies = pygame.sprite.Group()

# Add Sprites
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
    Enemies.update()
    Shots.update()

    
    if not Enemies:
        for x in range(6):
            enemies = enemy()
            Enemies.add(enemies)



    Player.draw(screen)
    Enemies.draw(screen)
    Shots.draw(screen)

    pygame.display.flip()