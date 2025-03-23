import streamlit as st
import numpy as np
import random

def create_board(size, mines):
    board = np.zeros((size, size), dtype=int)
    mine_positions = random.sample(range(size * size), mines)
    
    for pos in mine_positions:
        row, col = divmod(pos, size)
        board[row][col] = -1
    
    for row in range(size):
        for col in range(size):
            if board[row][col] == -1:
                continue
            count = sum(
                board[r][c] == -1
                for r in range(max(0, row - 1), min(size, row + 2))
                for c in range(max(0, col - 1), min(size, col + 2))
            )
            board[row][col] = count
    return board

def display_board(board, revealed, flagged):
    size = len(board)
    for row in range(size):
        cols = []
        for col in range(size):
            if flagged[row][col]:
                cols.append("🚩")
            elif not revealed[row][col]:
                cols.append("⬜")
            elif board[row][col] == -1:
                cols.append("💣")
            else:
                cols.append(str(board[row][col]) if board[row][col] > 0 else " ")
        st.write(" ".join(cols))

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return
    
    revealed[row][col] = True
    
    if board[row][col] == 0:
        for r in range(max(0, row - 1), min(len(board), row + 2)):
            for c in range(max(0, col - 1), min(len(board), col + 2)):
                if not revealed[r][c]:
                    reveal(board, revealed, r, c)

def main():
    st.title("💣 Minesweeper Game")
    size = st.sidebar.slider("Grid Size", 5, 10, 9)
    mines = st.sidebar.slider("Number of Mines", 1, size * size // 2, 10)
    
    if "board" not in st.session_state:
        st.session_state.board = create_board(size, mines)
        st.session_state.revealed = np.zeros((size, size), dtype=bool)
        st.session_state.flagged = np.zeros((size, size), dtype=bool)
    
    board = st.session_state.board
    revealed = st.session_state.revealed
    flagged = st.session_state.flagged
    
    row = st.number_input("Row (0-indexed)", min_value=0, max_value=size-1, step=1)
    col = st.number_input("Column (0-indexed)", min_value=0, max_value=size-1, step=1)
    
    if st.button("Reveal Cell"):
        if board[row][col] == -1:
            st.error("💥 Game Over! You hit a mine.")
            st.session_state.revealed = np.ones((size, size), dtype=bool)
        else:
            reveal(board, revealed, row, col)
    
    if st.button("Flag Cell"):
        flagged[row][col] = not flagged[row][col]
    
    display_board(board, revealed, flagged)
    
    if np.all((board != -1) | revealed):
        st.success("🎉 Congratulations! You won the game!")

if __name__ == "__main__":
    main()
