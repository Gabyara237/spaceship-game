import pygame

Swidth= 900
Sheight= 600

Black = (0,0,0)
White = (255,255,255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

class fire( pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.image.load("assets/shots.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y -= 10

        if self.rect.bottom <0:
            self.kill
