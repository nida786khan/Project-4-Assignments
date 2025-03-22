import streamlit as st
import numpy as np
import math

st.title("🤖 Tic-Tac-Toe AI")

if "board" not in st.session_state:
    st.session_state.board = np.full((3, 3), " ")
    st.session_state.winner = None
    st.session_state.user_turn = True  # User starts first

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

def minimax(board, is_maximizing):
    scores = {"X": 1, "O": -1, "Tie": 0}

    if check_winner(board, "X"):
        return scores["X"]
    elif check_winner(board, "O"):
        return scores["O"]
    elif " " not in board:
        return scores["Tie"]

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == " ":
                    board[i, j] = "X"
                    score = minimax(board, False)
                    board[i, j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == " ":
                    board[i, j] = "O"
                    score = minimax(board, True)
                    board[i, j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if st.session_state.board[i, j] == " ":
                st.session_state.board[i, j] = "X"
                score = minimax(st.session_state.board, False)
                st.session_state.board[i, j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

cols = st.columns(3)
for i in range(3):
    for j in range(3):
        if cols[j].button(st.session_state.board[i, j], key=f"{i}{j}"):
            if st.session_state.board[i, j] == " " and st.session_state.winner is None:
                st.session_state.board[i, j] = "O"
                if check_winner(st.session_state.board, "O"):
                    st.session_state.winner = "O"
                else:
                    ai_move = best_move()
                    if ai_move != (-1, -1):
                        st.session_state.board[ai_move] = "X"
                        if check_winner(st.session_state.board, "X"):
                            st.session_state.winner = "X"

st.write("### Board")
st.table(st.session_state.board)

if st.session_state.winner:
    st.success(f"🎉 {st.session_state.winner} wins!")
elif " " not in st.session_state.board:
    st.warning("It's a Tie!")

if st.button("Reset Game"):
    st.session_state.board = np.full((3, 3), " ")
    st.session_state.winner = None
