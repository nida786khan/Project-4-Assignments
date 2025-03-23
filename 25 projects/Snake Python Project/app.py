import pygame
import random

# Initialize pygame
pygame.init()

# Game Variables
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)  # Font for text

# Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Function to Reset Game
def reset_game():
    global snake, direction, food, running, speed, level
    snake = [(100, 100)]
    direction = (GRID_SIZE, 0)
    food = (random.randint(0, (WIDTH//GRID_SIZE) - 1) * GRID_SIZE, 
            random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE)
    running = True
    speed = 10 + (level * 2)  # Speed increases with level

# Move Snake
def move_snake():
    global snake, food
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Game Over if Snake hits wall or itself
    if (new_head in snake or 
        new_head[0] < 0 or new_head[1] < 0 or 
        new_head[0] >= WIDTH or new_head[1] >= HEIGHT):
        return False

    if new_head == food:
        food = (random.randint(0, (WIDTH//GRID_SIZE) - 1) * GRID_SIZE, 
                random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE)
    else:
        snake.pop()

    snake.insert(0, new_head)
    return True

# Initialize Game
level = 1
reset_game()
clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Move Snake
    if running:
        if not move_snake():
            running = False  # Game Over
    else:
        # Game Over Screen
        game_over_text = FONT.render(f"Game Over! Level {level}", True, WHITE)
        restart_text = FONT.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)
        screen.blit(game_over_text, (WIDTH//3, HEIGHT//3))
        screen.blit(restart_text, (WIDTH//6, HEIGHT//2))

        pygame.display.flip()

        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart game
                        level += 1  # Increase level
                        reset_game()
                        waiting = False
                    elif event.key == pygame.K_q:  # Quit game
                        pygame.quit()
                        exit()

    # Draw Snake & Food
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

    # Display Level
    level_text = FONT.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)
