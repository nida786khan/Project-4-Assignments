import pygame

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Multiplayer Game")

# Load assets
player_img = pygame.Surface((50, 50))
player_img.fill(WHITE)

# Player class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED
    
    def move(self, dx, dy):
        self.x = max(0, min(WIDTH - 50, self.x + dx))
        self.y = max(0, min(HEIGHT - 50, self.y + dy))
    
    def draw(self):
        screen.blit(player_img, (self.x, self.y))

# Game loop
running = True
player1 = Player(WIDTH // 4, HEIGHT // 2)
player2 = Player(3 * WIDTH // 4, HEIGHT // 2)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    player1.move((-PLAYER_SPEED if keys[pygame.K_a] else 0) + (PLAYER_SPEED if keys[pygame.K_d] else 0),
                 (-PLAYER_SPEED if keys[pygame.K_w] else 0) + (PLAYER_SPEED if keys[pygame.K_s] else 0))
    player2.move((-PLAYER_SPEED if keys[pygame.K_LEFT] else 0) + (PLAYER_SPEED if keys[pygame.K_RIGHT] else 0),
                 (-PLAYER_SPEED if keys[pygame.K_UP] else 0) + (PLAYER_SPEED if keys[pygame.K_DOWN] else 0))
    
    player1.draw()
    player2.draw()
    pygame.display.update()

pygame.quit()
