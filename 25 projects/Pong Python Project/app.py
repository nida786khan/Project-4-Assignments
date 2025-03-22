import streamlit as st
import pygame

# Initialize pygame
pygame.init()

# Game Variables
WIDTH, HEIGHT = 600, 400
BALL_SPEED = [4, 4]
PADDLE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Ball and Paddle
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
paddle1 = pygame.Rect(10, HEIGHT // 2 - 30, 10, 60)
paddle2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 30, 10, 60)

# Streamlit UI
st.title("🏓 Pong Game")
if st.button("Start Game"):
    running = True
    while running:
        screen.fill(BLACK)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Ball Movement
        ball.x += BALL_SPEED[0]
        ball.y += BALL_SPEED[1]

        # Ball Collision
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            BALL_SPEED[1] = -BALL_SPEED[1]
        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            BALL_SPEED[0] = -BALL_SPEED[0]

        # Draw Elements
        pygame.draw.rect(screen, WHITE, paddle1)
        pygame.draw.rect(screen, WHITE, paddle2)
        pygame.draw.ellipse(screen, WHITE, ball)

        pygame.display.flip()

    pygame.quit()
