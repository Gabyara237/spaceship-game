import pygame
import random

# Set the screen dimensions
Swidth= 900
Sheight= 600

# Create a class for the enemy sprite
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the enemy image
        self.image = pygame.image.load('assets/enemy.png')
        self.rect = self.image.get_rect() 

        # Initialize the enemy's position within the screen
        self.rect.center = (200,500)
        self.rect.x = random.randrange(Swidth - self.rect.width)
        self.rect.y = random.randrange(300 - self.rect.height)

        # Initialize the enemy's random speed in both x and y directions
        self.speed_x = random.randrange(1,5)
        self.speed_y = random.randrange(1,5)
    

    def update (self):
        
        # Move the enemy based on its speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Adjust speed if hitting screen edges
        if self.rect.left < 0:
            self.speed_x +=1 
        if self.rect.right > Swidth:
            self.speed_x -=1
        if self.rect.bottom > Sheight:
            self.speed_y -=1 
        if self.rect.top < 0 :
            self.speed_y +=1