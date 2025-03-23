import pygame
import random

# Game Constants
WIDTH, HEIGHT = 300, 600
BLOCK = 30
ROWS, COLS = HEIGHT // BLOCK, WIDTH // BLOCK

# Colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
COLORS = [(0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (128, 0, 128)]

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 0], [1, 1, 1]]
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

def new_tetromino():
    return {"shape": random.choice(SHAPES), "color": random.choice(COLORS), "x": COLS // 2, "y": 0}

def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen, WHITE, (x * BLOCK, y * BLOCK, BLOCK, BLOCK), 1)

def draw_tetromino(tet):
    for y, row in enumerate(tet["shape"]):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, tet["color"], ((tet["x"] + x) * BLOCK, (tet["y"] + y) * BLOCK, BLOCK, BLOCK))

def move_tetromino(tet, dx, dy):
    tet["x"] += dx
    tet["y"] += dy

def game_loop():
    tetromino = new_tetromino()
    running = True
    
    while running:
        screen.fill(BLACK)
        draw_grid()
        draw_tetromino(tetromino)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tetromino(tetromino, -1, 0)
                if event.key == pygame.K_RIGHT:
                    move_tetromino(tetromino, 1, 0)
                if event.key == pygame.K_DOWN:
                    move_tetromino(tetromino, 0, 1)
        
        pygame.display.flip()
        clock.tick(10)
    
    pygame.quit()

game_loop()
