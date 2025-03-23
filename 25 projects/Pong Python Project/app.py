import streamlit as st
import pygame
import numpy as np
import time

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 400
PADDLE_SIZE = (10, 80)
BALL_RADIUS = 10
SPEED = 4
PADDLE_SPEED = 20
WIN_SCORE = 5

# Colors
WHITE, BLACK, RED, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255)

# Initialize game state
if "game" not in st.session_state:
    st.session_state.game = {
        "ball": [WIDTH // 2, HEIGHT // 2, SPEED, SPEED],
        "paddle_a": HEIGHT // 2 - PADDLE_SIZE[1] // 2,
        "paddle_b": HEIGHT // 2 - PADDLE_SIZE[1] // 2,
        "score": [0, 0],
        "running": False,
        "winner": None,
    }

game = st.session_state.game

# UI Buttons
st.title("🏓 Pong Game")
cols = st.columns(3)
if cols[0].button("▶ Start Game"): game["running"], game["winner"] = True, None
if cols[1].button("⏹ Stop Game"): game["running"] = False
if cols[2].button("⏯ Resume Game") and not game["winner"]: game["running"] = True
st.markdown("---")

# Paddle Controls
control_cols = st.columns([1, 3, 1])
for i, (player, key_up, key_down) in enumerate([(0, "a_up", "a_down"), (1, "b_up", "b_down")]):
    with control_cols[i * 2]:
        st.write(f"**Player {'A' if i == 0 else 'B'}**")
        if st.button("🔼 Up", key=key_up): game[f"paddle_{'a' if i == 0 else 'b'}"] = max(0, game[f"paddle_{'a' if i == 0 else 'b'}"] - PADDLE_SPEED)
        if st.button("🔽 Down", key=key_down): game[f"paddle_{'a' if i == 0 else 'b'}"] = min(HEIGHT - PADDLE_SIZE[1], game[f"paddle_{'a' if i == 0 else 'b'}"] + PADDLE_SPEED)

# Game Logic
if game["running"] and not game["winner"]:
    game["ball"][0] += game["ball"][2]
    game["ball"][1] += game["ball"][3]

    if game["ball"][1] - BALL_RADIUS < 0 or game["ball"][1] + BALL_RADIUS > HEIGHT:
        game["ball"][3] *= -1

    for i, x in enumerate([0, WIDTH - PADDLE_SIZE[0]]):
        if game["ball"][0] - BALL_RADIUS <= x + PADDLE_SIZE[0] and game[f"paddle_{'a' if i == 0 else 'b'}"] < game["ball"][1] < game[f"paddle_{'a' if i == 0 else 'b'}"] + PADDLE_SIZE[1]:
            game["ball"][2] *= -1

    if game["ball"][0] < 0:
        game["score"][1] += 1
        game["ball"][:2] = [WIDTH // 2, HEIGHT // 2]
    if game["ball"][0] > WIDTH:
        game["score"][0] += 1
        game["ball"][:2] = [WIDTH // 2, HEIGHT // 2]

    for i, player in enumerate(["A", "B"]):
        if game["score"][i] >= WIN_SCORE:
            game["winner"] = f"🎉 Player {player} Wins!"
            game["running"] = False

# Draw Game
screen = pygame.Surface((WIDTH, HEIGHT))
screen.fill(BLACK)
for i, color in enumerate([RED, BLUE]):
    pygame.draw.rect(screen, color, (WIDTH * i - PADDLE_SIZE[0] * i, game[f"paddle_{'a' if i == 0 else 'b'}"], *PADDLE_SIZE))
pygame.draw.circle(screen, WHITE, game["ball"][:2], BALL_RADIUS)

game_img = np.transpose(pygame.surfarray.array3d(screen), (1, 0, 2))
control_cols[1].image(game_img, caption=f"🏆 Score: A ({game['score'][0]}) - B ({game['score'][1]})", use_container_width=True)

if game["winner"]:
    st.markdown(f"<h2 style='text-align: center; color: green;'>{game['winner']}</h2>", unsafe_allow_html=True)

# Refresh
time.sleep(0.1)
st.session_state.game = game
st.rerun()
