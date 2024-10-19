   # Import the pygame library and initialise the game engine
import pygame
import random
import sys

projectiles = []
enemies = []

def create_enemy(width, enemy_size):
    x = random.randint(0, width - enemy_size)
    y = random.randint(-enemy_size * 2, -enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

def draw_player(surface, x, y):
    pygame.draw.rect(surface, player_color, (x, y, player_size, player_size))

def draw_enemy(surface, enemy):
    pygame.draw.rect(surface, enemy_color, enemy)

def draw_projectile(surface, proj):
    pygame.draw.rect(surface, proj_color, proj)


# Colors
BLACK = (0, 0, 0); WHITE = (255, 255, 255); RED = (255, 0, 0)
BLUE = (0, 0, 255); PURPLE = (128, 0, 128); LIME = 	(0, 255, 0)
NAVYBLUE = 	(0, 0, 128)

# Player settings
player_size = 50
player_speed = 5
player_color = NAVYBLUE

# Projectile settings
proj_size = 5
proj_speed = 7
proj_color = WHITE

# Enemy settings
enemy_size = 60
enemy_speed = 10
enemy_color = LIME

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
# Get screen width and height
width, height = screen.get_size()
# Give the screen a title
pygame.display.set_caption('DropBlock')
# Set clock
clock = pygame.time.Clock()

player_x = width // 2 - player_size // 2
player_y = height - player_size - 10 # Why  - 10?

player_rect = pygame.Rect(player_x, player_y, player_size, player_size)


# Game loop
running = True
score = 0
font = pygame.font.SysFont(None, 30)

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
        if player_x <= 0:
            player_x = width
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        if player_x >= width:
            player_x = 0
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed
        if player_y <= 0:
            player_y = height - player_size - 10

    player_rect.x = player_x
    draw_player(screen, player_x, player_y)

    if random.randint(1, 100) < 3:
        create_enemy(width, enemy_size)

    for enemy in enemies:
        enemy.y += enemy_speed
        draw_enemy(screen, enemy)

        if enemy.colliderect(player_rect):
            running = False

        for proj in projectiles:
            if proj.colliderect(enemy):
                enemies.remove(enemy)
                projectiles.remove(proj)
                score += 000000.1

        if enemy.y > height:
            enemies.remove(enemy)

    for proj in projectiles:
        proj.y -= proj_speed
        draw_projectile(screen, proj)

        if proj.y < 0:
            projectiles.remove(proj)

    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    
    clock.tick(60)
    score = score  + 1

pygame.quit()