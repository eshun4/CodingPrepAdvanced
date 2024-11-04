"""
Now, let's apply what you've learned by focusing on a crucial aspect of the task. 
In this practice, you need to define how we switch directions and move left when we reach the top or bottom of our bookshelf. 
Remember, the books on these shelves are organized in a unique pattern.
"""

def column_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, cols - 1
    direction = -1  # Start going upwards
    output = []

    for _ in range(rows * cols):
        output.append(matrix[row][col])
        # TODO: Implement logic to change direction and move left when hitting the top or bottom of the shelf
        if direction == -1 and row == 0 and col > 0:
            col -= 1
            direction = 1
        elif direction == 1 and row == rows - 1 and col > 0:
            col -= 1
            direction = -1
        else:
            row += direction
    return output

# Example matrix resembling a bookshelf (3 shelves, 4 books each)
bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(column_traverse(bookshelf))