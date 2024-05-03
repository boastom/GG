import pygame
import random
import sys
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
purple = (128, 0, 128)
lime = 	(0, 255, 0)
NavyBlue = 	(0, 0, 128)
# Player settings
player_size = 50
player_speed = 5
player_color = NavyBlue

# Projectile settings
proj_size = 5
proj_speed = 7
proj_color = WHITE

# Enemy settings
enemy_size = 55
enemy_speed = 4
enemy_color = lime

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Simple Shooter Game')

clock = pygame.time.Clock()

player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 10

player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
projectiles = []
enemies = []

def create_enemy():
    x = random.randint(0, SCREEN_WIDTH - enemy_size)
    y = random.randint(-enemy_size * 2, -enemy_size)
    enemies.append(pygame.Rect(x, y, enemy_size, enemy_size))

def draw_player(surface, x, y):
    pygame.draw.rect(surface, player_color, (x, y, player_size, player_size))

def draw_enemy(surface, enemy):
    pygame.draw.rect(surface, enemy_color, enemy)

def draw_projectile(surface, proj):
    pygame.draw.rect(surface, proj_color, proj)

# Game loop
running = True
score = 0
font = pygame.font.SysFont(None, 30)

init = True
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
            player_x = SCREEN_WIDTH
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
        if player_x >= SCREEN_WIDTH:
            player_x = 0

    player_rect.x = player_x
    draw_player(screen, player_x, player_y)

    if init is True:
        clock.tick(1000)
        init = False

    if random.randint(1, 100) < 5:
        create_enemy()

    for enemy in enemies:
        enemy.y += enemy_speed
        draw_enemy(screen, enemy)

        if enemy.colliderect(player_rect):
            running = False

        for proj in projectiles:
            if proj.colliderect(enemy):
                enemies.remove(enemy)
                projectiles.remove(proj)
                score += 00000.1

        if enemy.y > SCREEN_HEIGHT:
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
