import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30
GAME_WIDTH, GAME_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Define the shapes of the tetrominoes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]

# Function to create a new piece
def new_piece():
    shape = random.choice(SHAPES)
    color = random.choice([RED, GREEN, BLUE, CYAN])
    return shape, color

# Function to draw the grid
def draw_grid():
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Function to draw a piece on the screen
def draw_piece(piece, x_offset, y_offset, color):
    shape, _ = piece
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color, ((x + x_offset) * BLOCK_SIZE, (y + y_offset) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Function to check if the piece is within bounds and not colliding
def valid_position(piece, x_offset, y_offset, grid):
    shape, _ = piece
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + x_offset < 0 or x + x_offset >= GAME_WIDTH or y + y_offset >= GAME_HEIGHT:
                    return False
                if grid[y + y_offset][x + x_offset]:
                    return False
    return True

# Function to lock the piece into the grid
def lock_piece(piece, x_offset, y_offset, grid):
    shape, color = piece
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + y_offset][x + x_offset] = color

# Function to clear completed lines
def clear_lines(grid):
    lines_cleared = 0
    for y in range(GAME_HEIGHT - 1, -1, -1):
        if all(grid[y]):
            lines_cleared += 1
            del grid[y]
            grid.insert(0, [None] * GAME_WIDTH)
    return lines_cleared

# Main game loop
def game_loop():
    grid = [[None] * GAME_WIDTH for _ in range(GAME_HEIGHT)]
    clock = pygame.time.Clock()
    game_over = False
    piece = new_piece()
    x_offset = GAME_WIDTH // 2 - len(piece[0]) // 2
    y_offset = 0
    speed = 500
    lines_cleared = 0

    while not game_over:
        screen.fill(BLACK)
        draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Move piece left, right, or down based on key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and valid_position(piece, x_offset - 1, y_offset, grid):
            x_offset -= 1
        if keys[pygame.K_RIGHT] and valid_position(piece, x_offset + 1, y_offset, grid):
            x_offset += 1
        if keys[pygame.K_DOWN] and valid_position(piece, x_offset, y_offset + 1, grid):
            y_offset += 1

        # Move piece down automatically
        if pygame.time.get_ticks() % speed == 0:
            if valid_position(piece, x_offset, y_offset + 1, grid):
                y_offset += 1
            else:
                lock_piece(piece, x_offset, y_offset, grid)
                lines_cleared += clear_lines(grid)
                piece = new_piece()
                x_offset = GAME_WIDTH // 2 - len(piece[0]) // 2
                y_offset = 0
                if not valid_position(piece, x_offset, y_offset, grid):
                    game_over = True

        draw_piece(piece, x_offset, y_offset, piece[1])
        pygame.display.flip()
        clock.tick(60)

# Start the game
game_loop()
pygame.quit()


    
