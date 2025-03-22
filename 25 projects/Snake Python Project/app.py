import streamlit as st
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

# Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Snake & Food
snake = [(100, 100)]
direction = (GRID_SIZE, 0)
food = (random.randint(0, (WIDTH//GRID_SIZE) - 1) * GRID_SIZE, 
        random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE)

def move_snake():
    global snake, food
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if new_head == food:
        food = (random.randint(0, (WIDTH//GRID_SIZE) - 1) * GRID_SIZE, 
                random.randint(0, (HEIGHT//GRID_SIZE) - 1) * GRID_SIZE)
    else:
        snake.pop()
    snake.insert(0, new_head)

# Streamlit UI
st.title("🐍 Snake Game")
if st.button("Start Game"):
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_snake()

        # Draw Snake & Food
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
