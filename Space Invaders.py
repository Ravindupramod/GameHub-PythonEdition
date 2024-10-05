import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')  # Replace with a path to a spaceship image if you have one
pygame.display.set_icon(icon)

# Background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 0, 0))

# Player
player_img = pygame.image.load('player.png')  # Replace with your player image
player_x = 370
player_y = 480
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))  # Replace with your enemy image
    enemy_x.append(random.randint(0, WIDTH - 64))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3)
    enemy_y_change.append(40)

# Bullet
bullet_img = pygame.image.load('bullet.png')  # Replace with your bullet image
bullet_x = 0
bullet_y = player_y
bullet_y_change = 5
bullet_state = "ready"  # "ready" means the bullet is not visible; "fire" means it's moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Game Over text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB background color
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player Movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= WIDTH - 64:
        player_x = WIDTH - 64

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= WIDTH - 64:
            enemy_x_change[i] = -3
            enemy_y[i] += enemy_y_change[i]

        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, WIDTH - 64)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet Movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    # Display player and score
    player(player_x, player_y)
    show_score(text_x, text_y)

    # Update the display
    pygame.display.update()
