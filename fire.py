import pygame

Swidth= 900
Sheight= 600


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
