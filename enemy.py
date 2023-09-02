import pygame
import random

Swidth= 900
Sheight= 600

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

        self.speed_x = random.randrange(1,10)
        self.speed_y = random.randrange(1,10)
    
    def update (self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y