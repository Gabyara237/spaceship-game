import pygame

# Set screen dimensions
Swidth= 900
Sheight= 600

# Define the fire class for projectile sprites
class fire( pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        # Load the projectile image
        self.image = pygame.image.load("assets/shots.png")
        self.rect = self.image.get_rect()
        
        # Set the initial position of the projectile
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):

        # Move the projectile upward
        self.rect.y -= 10

        #  Remove the projectile if it goes off the top of the screen 
        if self.rect.bottom <0:
            self.kill
