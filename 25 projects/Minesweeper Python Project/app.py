import streamlit as st
import random
import numpy as np

# Game settings
GRID_SIZE = 5
MINES_COUNT = 3

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    st.session_state.mines = set(random.sample(range(GRID_SIZE * GRID_SIZE), MINES_COUNT))
    st.session_state.revealed = set()
    st.session_state.game_over = False

# Function to count nearby mines
def count_mines(r, c):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum((r + dr) * GRID_SIZE + (c + dc) in st.session_state.mines 
               for dr, dc in directions if 0 <= r + dr < GRID_SIZE and 0 <= c + dc < GRID_SIZE)

# Reveal cell function
def reveal_cell(r, c):
    if (r * GRID_SIZE + c) in st.session_state.mines:
        st.session_state.game_over = True
    elif (r, c) not in st.session_state.revealed:
        st.session_state.revealed.add((r, c))
        count = count_mines(r, c)
        if count == 0:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                    reveal_cell(nr, nc)

# Streamlit UI
st.title("💣 Minesweeper")

if st.session_state.game_over:
    st.error("💥 BOOM! You hit a mine! Game Over.")
elif len(st.session_state.revealed) == (GRID_SIZE * GRID_SIZE) - MINES_COUNT:
    st.success("🎉 Congratulations! You won!")

# Create grid buttons
for r in range(GRID_SIZE):
    cols = []
    for c in range(GRID_SIZE):
        if (r, c) in st.session_state.revealed:
            count = count_mines(r, c)
            cols.append(st.button(f"{count}" if count > 0 else "⬜", key=f"{r}{c}", disabled=True))
        else:
            if st.button("🟦", key=f"{r}{c}"):
                reveal_cell(r, c)
    st.write(cols)
