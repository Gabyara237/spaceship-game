import pygame

Swidth= 900
Sheight= 600

class start():
    pygame.init()

screen= pygame.display.set_mode((Swidth,Sheight))

#

running =True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()