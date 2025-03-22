import streamlit as st
import numpy as np

# Sudoku Solver using Backtracking
def is_valid(board, row, col, num):
    """Check if num can be placed at board[row][col]"""
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solve Sudoku using backtracking"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Streamlit UI
st.title("🔢 Sudoku Solver")

# Input Sudoku Grid
default_grid = np.zeros((9, 9), dtype=int)
grid = []
for i in range(9):
    row = []
    cols = st.columns(9)
    for j in range(9):
        row.append(cols[j].number_input("", min_value=0, max_value=9, value=int(default_grid[i][j]), key=f"{i}{j}"))
    grid.append(row)

grid = np.array(grid)

# Solve Button
if st.button("Solve Sudoku"):
    if solve_sudoku(grid):
        st.success("✅ Sudoku Solved Successfully!")
    else:
        st.error("❌ No Solution Found!")

# Display Solved Grid
st.write("### 🏆 Solved Sudoku Grid:")
st.write(grid)
