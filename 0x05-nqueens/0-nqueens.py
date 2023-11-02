#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n):
    """
    Solve the N queens problem using backtracking.
    """
    if col >= n:
        # All queens are placed, print the solution
        for row in board:
            print([row.index(1), row])
        return
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0

def nqueens(n):
    """
    Find and print all solutions to the N queens problem.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
