"""
here's a magical spell (also known as "code") that allows you to inspect the chessboard for wise moves.
Can you figure out the incantation (or code) that helps identify possible locations 
for a new piece, ensuring it has room to move in the next turn? 
Focus on checking the conditions for a spot to be deemed valid.

"""


def evaluate_move(board, row, col):
    # TODO: Check if a move to the given cell is possible; write a condition to check if the cell is empty.
    # Also, check if at least one neighboring cell is empty (not diagonally).
    rows, cols = len(board),len(board[0])
    if board[row][col] == "E":
        return ((row > 0 and board[row - 1][col] == "E") or 
        (row < rows - 1 and board[row + 1][col] == "E") or 
        (col > 0 and board[row][col - 1] == "E") or 
        (col < cols - 1 and board[row][col + 1] == "E"))
    return False
    
    
    
    

# Assuming a constant 2D array representing a board
board = [
    ['P', 'E', 'E', 'P'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'P'],
    ['P', 'E', 'P', 'E']
]

# TODO: Write a list comprehension to find all valid move positions.
valid_positions = [(row, col) for row in range(len(board)) for col in range(len(board[0])) if evaluate_move(board, row, col)]
print(valid_positions)