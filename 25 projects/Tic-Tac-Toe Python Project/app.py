import streamlit as st
import numpy as np

st.title("❌⭕ Tic-Tac-Toe Game")

# Board initialization
if "board" not in st.session_state:
    st.session_state.board = np.full((3, 3), " ")
    st.session_state.current_player = "X"
    st.session_state.winner = None

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in board.T:
        if all(cell == player for cell in col):
            return True
    if all(board[i, i] == player for i in range(3)) or all(board[i, 2 - i] == player for i in range(3)):
        return True
    return False

# Game UI
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        if cols[j].button(st.session_state.board[i, j], key=f"{i}{j}"):
            if st.session_state.board[i, j] == " " and st.session_state.winner is None:
                st.session_state.board[i, j] = st.session_state.current_player
                if check_winner(st.session_state.board, st.session_state.current_player):
                    st.session_state.winner = st.session_state.current_player
                st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

st.write("### Board")
st.table(st.session_state.board)

if st.session_state.winner:
    st.success(f"🎉 {st.session_state.winner} wins!")
elif " " not in st.session_state.board:
    st.warning("It's a Tie!")

if st.button("Reset Game"):
    st.session_state.board = np.full((3, 3), " ")
    st.session_state.current_player = "X"
    st.session_state.winner = None
