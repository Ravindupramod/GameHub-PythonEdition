import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Define game variables
gravity = 0.5
bird_movement = 0
bird_rect = pygame.Rect(50, 300, 34, 24)

pipe_height = [200, 300, 400]
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Scoring system
score = 0
high_score = 0

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Load assets
bird_img = pygame.Surface((34, 24))
bird_img.fill(BLUE)

pipe_surface = pygame.Surface((50, 600))
pipe_surface.fill(GREEN)

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

# Font for score display
font = pygame.font.Font(None, 36)

# Function to move the pipes
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > 0]

# Function to generate pipes
def create_pipe():
    random_pipe_height = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(WIDTH + 100, random_pipe_height))
    top_pipe = pipe_surface.get_rect(midbottom=(WIDTH + 100, random_pipe_height - 150))
    return bottom_pipe, top_pipe

# Function to check collisions
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= HEIGHT:
        return False
    return True

# Function to draw pipes
def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

# Function to check if the bird has passed a pipe
def check_score(pipes, score):
    for pipe in pipes:
        if pipe.centerx == bird_rect.centerx:
            score += 1
    return score

# Function to display the score on the screen
def display_score(score, high_score):
    score_surface = font.render(f"Score: {score}", True, BLACK)
    high_score_surface = font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(score_surface, (10, 10))
    screen.blit(high_score_surface, (10, 50))

# Game loop
def game_loop():
    global bird_movement, pipe_list, score, high_score
    clock = pygame.time.Clock()
    running = True
    game_active = True

    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 7
                if event.key == pygame.K_SPACE and not game_active:
                    bird_rect.center = (50, 300)
                    pipe_list.clear()
                    bird_movement = 0
                    score = 0
                    game_active = True
            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())

        if game_active:
            # Bird movement
            bird_movement += gravity
            bird_rect.centery += bird_movement

            # Draw bird
            screen.blit(bird_img, bird_rect)

            # Move pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)

            # Check for collision
            game_active = check_collision(pipe_list)

            # Update and check score
            score = check_score(pipe_list, score)

        else:
            # Game over
            screen.blit(bird_img, bird_rect)
            if score > high_score:
                high_score = score

        # Display score
        display_score(score, high_score)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Run the game
game_loop()
