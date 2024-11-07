"""
Adjust our function so that it identifies potential positions for a new piece, based solely on its ability 
to move left or right. We're simplifying our search to horizontal moves only, 
aligning with our focus on multidimensional arrays. Modify the code accordingly and observe the difference.
"""

# Function to check if a neighboring position is empty ('E')
def is_empty_neighbor(board, x, y):
    rows, cols = len(board), len(board[0])

    # Check that (x, y) is within board boundaries
    if 0 <= x < rows and 0 <= y < cols:
        return board[x][y] == 'E'
    return False

def main():
    board = [
        ['P', 'E', 'E', 'P'],
        ['E', 'P', 'E', 'P'],
        ['P', 'E', 'P', 'P'],
        ['P', 'E', 'P', 'E']
    ]
    result = []
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            # Check for empty spot with an empty neighbor on four directions
            if board[i][j] == 'E' and (
                is_empty_neighbor(board, i, j - 1) or
                is_empty_neighbor(board, i, j + 1)
            ):
                result.append((i, j))
    print(result)

if __name__ == "__main__":
    main()