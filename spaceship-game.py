from typing import Any
import pygame
from pygame.sprite import Group
from enemy import enemy
from fire import fire

Swidth= 900
Sheight= 600
game_over = False


White = (255,255,255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

FPS= 60

Consoles = pygame.font.match_font('consolas')
Times = pygame.font.match_font('times')
Arial = pygame.font.match_font('arial')
Courier = pygame.font.match_font('courier')

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
        shot= fire(self.rect.centerx -45, self.rect.centery +20 )
        Shots.add(shot)
    def shots2(self):
        shot= fire(self.rect.centerx +45, self.rect.centery +20)
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

lives= 5
score=0
def text(screen,fonts, text,color,dimensions, x,y):
    type_letter = pygame.font.Font(fonts,dimensions)
    surface = type_letter.render(text,True,color)
    rectangle = surface.get_rect()
    rectangle.center = (x,y)
    screen.blit(surface,rectangle)

restart_button= pygame.Rect(Swidth // 2 -90,Sheight // 2 + 50, 180, 50 )
button_font= pygame.font.Font(Times,30)
restart_text =  button_font.render("New game", True, Green)

running =True

while running:
    clock.tick(FPS)
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        text(screen,Times,"Score: " + str(score).zfill(4),White,30, 780,50)
        text(screen,Times,"Lives: " + str(lives),White,30, 100,50)

        Player.update()
        Enemies.update()
        Shots.update()

        ship_collision = pygame.sprite.groupcollide(Player,Enemies, False, False)
        shot_collision = pygame.sprite.groupcollide(Shots,Enemies, True, True)

        if ship_collision:
            for enemy_hit in ship_collision[players]:
              enemy_hit.kill()
            lives -= 1

        if lives <=0:
          game_over= True
        
        if score < 0:
            score = 0
        
        if shot_collision:
            score +=30
       # players.kill()


        if not Enemies:
            for x in range(10):
                enemies = enemy()
                Enemies.add(enemies)



        Player.draw(screen)
        Enemies.draw(screen)
        Shots.draw(screen)
    else:
        text(screen,Times,"Game Over!", Red, 50, Swidth//2,Sheight//2)

        pygame.draw.rect(screen, White, restart_button)
        screen.blit(restart_text, (Swidth // 2 - 70, Sheight // 2 + 60))

        
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and restart_button.collidepoint(mouse_pos):
            
            game_over = False
            lives = 5  
            score = 0  


    pygame.display.flip()