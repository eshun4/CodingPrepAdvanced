"""
Your task involves writing a function that simulates a unique traversal across a library's bookshelves,
moving through the collection in a zigzag pattern.
Remember to start from the bottom right and zigzag up and down each column. To the code editor!
"""


def bookshelfTraversal(bookshelves):
    rows, cols = len(bookshelves), len(bookshelves[0])
    traversal_path = []
    
    for col in range(cols - 1, -1, -1):
        if col % 2 == 0:  # Even-indexed columns (from the right), traverse from top to bottom
            for row in range(rows):
                traversal_path.append(bookshelves[row][col])
        else:  # Odd-indexed columns, traverse from bottom to top
            for row in range(rows - 1, -1, -1):
                traversal_path.append(bookshelves[row][col])
    
    return traversal_path

# Create a 2x4 'bookshelves' variable with unique numbers representing books
bookshelves = [
    [101, 102, 103, 104],
    [201, 202, 203, 204]
]

# Print the traversal path of the books
print(bookshelfTraversal(bookshelves))
