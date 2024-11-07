"""
More specifically, your task is to find the positions of empty cells that neighbor 
to at least one other empty cell. In the given matrix, 'E' represents an empty cell, and 'P' represents a cell with a piece. For a specific cell, 
its neighboring cells are the cells directly above, below, to the left, and to the right.
"""

# Sample 'chessboard' with 'E' for empty and 'P' for a piece
board = [
    ['P', 'E', 'E', 'P'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'P'],
    ['P', 'E', 'P', 'E']
]

# Find and print positions where a piece can move in its first turn
def print_movable_positions(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            # The logical bug is in the condition that checks for the empty neighbors
            if board[i][j] == 'E':
                if (i > 0 and board[i-1][j] == 'E') or (i < len(board)-1 and board[i+1][j] == 'E') or (j > 0 and board[i][j-1] == 'E') or(j < len(board[i])-1 and board[i][j+1] == 'E'):
                    print((i, j))

print_movable_positions(board)