import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

board = create_board()

# Function to drop piece
def drop_piece(board, col, piece):
    for row in range(ROW_COUNT - 1, -1, -1):  # Start from bottom row
        if board[row, col] == 0:
            board[row, col] = piece
            return True
    return False

# Function to draw board
def draw_board(board):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(COLUMN_COUNT+1)-0.5, minor=True)
    ax.set_yticks(np.arange(ROW_COUNT+1)-0.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
    
    # Colors
    colors = {0: "white", 1: "red", 2: "yellow"}
    
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            circle = plt.Circle((c, ROW_COUNT - r - 1), 0.4, color=colors[board[r, c]])
            ax.add_patch(circle)
    
    ax.set_xlim(-0.5, COLUMN_COUNT-0.5)
    ax.set_ylim(-0.5, ROW_COUNT-0.5)
    ax.set_aspect('equal')
    return fig

# Streamlit UI
st.title("🔴🟡 Connect Four Game")

player_turn = st.session_state.get("player_turn", 1)
board = st.session_state.get("board", create_board())

col_choice = st.radio("Choose a column to drop your piece:", list(range(COLUMN_COUNT)))
if st.button("Drop Piece"):
    if drop_piece(board, col_choice, player_turn):
        st.session_state.board = board
        st.session_state.player_turn = 3 - player_turn  # Toggle between 1 and 2

st.pyplot(draw_board(board))
