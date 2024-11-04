"""
In the land of books and libraries, a challenge awaits you, Space Explorer! 
You have a grid that represents a library's bookshelf. 
Your mission is to traverse this bookshelf in a unique pattern, starting from the bottom
right corner and moving in a zig-zag manner, visiting every book. However, 
there appears to be a mistake causing the traversal to behave unexpectedly. 
Can you identify and correct it to ensure the bookshelf is traversed correctly?
"""

library = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [9, 11, 13, 15]
]

# Starting from the bottom right corner of the bookshelf
row = len(library) - 1
col = len(library[0]) - 1
goingUp = True

while col >= 0:
    print(library[row][col], end=" ")
    if goingUp:
        if row == 0:
            goingUp = False
            col -= 1
        else:
            row -= 1
    else:
        if row == len(library) - 1:
            goingUp = True
            col -= 1
        else:
            row += 1