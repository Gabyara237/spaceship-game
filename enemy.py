import pygame
import random

Swidth= 900
Sheight= 600

Black = (0,0,0)
White = (255,255,255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect() 
        self.rect.center = (200,500)
        self.rect.x = random.randrange(Swidth - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)

        self.speed_x = random.randrange(1,5)
        self.speed_y = random.randrange(1,5)
    
    def update (self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0:
            self.speed_x +=1 
        if self.rect.right > Swidth:
            self.speed_x -=1
        if self.rect.bottom > Sheight:
            self.speed_y -=1 
        if self.rect.top < 0 :
            self.speed_y +=1