import pygame
from pygame.sprite import Group
from enemy import enemy
from fire import fire

# Screen dimensions
Swidth= 900
Sheight= 600
game_over = False

# Colors
White = (255,255,255)
Red = (255, 0, 0)
Green = (0, 255, 0)

# Frames per second
FPS= 60

# Load images 
heart_image = pygame.image.load('assets/heart.png')
impact_image = pygame.image.load('assets/impact.png')

# Predefined font
Times = pygame.font.match_font('times')

# Welcome screen class
class WelcomeScreen():
    def __init__(self):
        self.background = pygame.image.load('assets/welcome.png')
        self.title_font = pygame.font.Font(Times, 50)
        self.text_font = pygame.font.Font(Times, 30)
        self.start_text = self.text_font.render("Press ENTER to start", True, White)
        self.show_screen = True
    
    # Draw the welcome screen
    def update(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.start_text, (Swidth // 2 - self.start_text.get_width() // 2, 525))

# Player class
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

        # Setting keys for player's movement
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
            shot_sound.play()

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Limit the player's position on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Swidth:
            self.rect.right = Swidth
        if self.rect.bottom > Sheight:
            self.rect.bottom = Sheight
        if self.rect.top < 0:
            self.rect.top = 0
    
    
    def shots(self):
        # Create a left shot
        shot = fire(self.rect.centerx -45, self.rect.centery +20 )
        Shots.add(shot)
    
    def shots2(self):
        # Create a right shot
        shot = fire(self.rect.centerx +45, self.rect.centery +20)
        Shots.add(shot)


# Game initialization
class start():
    pygame.init()

# Load sounds and music
shot_sound = pygame.mixer.Sound('assets/shot-sound.wav')
shot_sound.set_volume(0.1)
point_sound = pygame.mixer.Sound('assets/point-sound.wav')
background_sound = pygame.mixer.Sound('assets/background-sound.mp3')
game_over_sound = pygame.mixer.Sound('assets/game-over-sound.wav')
game_over_sound.set_volume(0.2)
pygame.mixer.music.set_volume(0.2)

# Play background music
background_sound.play()
clock = pygame.time.Clock()

# Sprites groups

Player = pygame.sprite.Group()
Shots = pygame.sprite.Group()
Enemies = pygame.sprite.Group()

# Add Sprites
players = player()
Player.add(players)

# Screen configuration
screen= pygame.display.set_mode((Swidth,Sheight))
pygame.display.set_caption("My Spaceship Game")

# Load background image
background = pygame.transform.scale(pygame.image.load('assets/galaxy-background.jpg').convert(),(900,600))

# Lives and score
lives= 5
heart_images = [heart_image.copy() for _ in range(lives)]

score=0

# Function to display text on the screen 
def text(screen,fonts, text,color,dimensions, x,y):
    type_letter = pygame.font.Font(fonts,dimensions)
    surface = type_letter.render(text,True,color)
    rectangle = surface.get_rect()
    rectangle.center = (x,y)
    screen.blit(surface,rectangle)

# Restart button 
restart_button= pygame.Rect(Swidth // 2 -90,Sheight // 2 + 50, 180, 50 )
button_font= pygame.font.Font(Times,30)
restart_text =  button_font.render("New game", True, Green)

# Initialize game variables
running =True
welcome_screen = WelcomeScreen()
game_started = False
collision_happened = False 

# Main game loop
while running:
    clock.tick(FPS)
    screen.blit(background,(0,0))

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        if game_started:
           
           # Display the score on the screen 
            text(screen,Times,"Score: " + str(score).zfill(4),White,30, 780,50)
       
            # Update player position, enemies and shots
            Player.update()
            Enemies.update()
            Shots.update()

            # Check for collisions between the player and enemies
            ship_collision = pygame.sprite.groupcollide(Player,Enemies, False, False)
            
            # Check for collisions between shots and enemies
            shot_collision = pygame.sprite.groupcollide(Shots,Enemies, True, True)

            if ship_collision:
                for enemy_hit in ship_collision[players]:
                    if not collision_happened:  
                        
                        # Remove enemy and decrease lives
                        collision_x, collision_y = enemy_hit.rect.center
                        enemy_hit.kill()
                        lives -= 1

                        # Remove a heart from the screen if there are any left
                        if len(heart_images) > 0:
                            heart_images.pop()

                        # Display collision effect
                        screen.blit(impact_image, (collision_x - impact_image.get_width() // 2, collision_y - impact_image.get_height() // 2))
                        collision_happened = True  

           
            collision_happened = False

            if lives <=0:
                game_over= True
        
            if score < 0:
                score = 0
        
            if shot_collision:
                score +=30
                point_sound.play()

                if not collision_happened:  
                        for shot, enemies_hit in shot_collision.items():
                            for enemy_hit in enemies_hit:
                              if not collision_happened:  
                                
                                # Display collision effect for shots 
                                collision_x, collision_y = enemy_hit.rect.center
                                screen.blit(impact_image, (collision_x - impact_image.get_width() // 2, collision_y - impact_image.get_height() // 2))
                                collision_happened = True 
            collision_happened = False

            if not Enemies:
                for x in range(10):
                    enemies = enemy()
                    Enemies.add(enemies)

            # Draw player, enemies, and shots on screen 
            Player.draw(screen)
            Enemies.draw(screen)
            Shots.draw(screen)
        else:

            # Display the welcome screen and wait for user input to start
            welcome_screen.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_started = True

    else:
        background_sound.stop()
        game_over_sound.play()

        # Display "Game Over" text on screen
        text(screen,Times,"Game Over!", Red, 50, Swidth//2,Sheight//2)

        # Draw the restart button 
        pygame.draw.rect(screen, White, restart_button)
        screen.blit(restart_text, (Swidth // 2 - 70, Sheight // 2 + 60))

        # Check if the user clicked the restart button 
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and restart_button.collidepoint(mouse_pos):
            game_over_sound.stop()
            background_sound.play()
            game_over = False
            lives = 5  
            score = 0  
            heart_images = [heart_image.copy() for _ in range(lives)]
            for x in range(5):
                    enemies = enemy()
                    Enemies.add(enemies)

    # Display player lives as hearts 
    for i, heart in enumerate(heart_images):
        screen.blit(heart, (20 + i * (heart.get_width() + 10), 20))

    # Update the screen 
    pygame.display.flip() 