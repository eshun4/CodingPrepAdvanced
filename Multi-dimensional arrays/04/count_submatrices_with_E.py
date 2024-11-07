"""
Write a Python function to count how many 3x3 submatrices in a given matrix have 'E's in all four corners. Remember, each 3x3 submatrix is like 
a smaller square within the larger matrix. Are you ready to apply what you've learned and show off your skills?
"""


def hasEinAllCorners(board, row, col):
    return (board[row][col] == 'E' and 
            board[row][col+2] == 'E' and 
            board[row+2][col] == 'E' and 
            board[row+2][col+2] == 'E')
            
def countSubmatricesWithE(board):
    # TODO: Initialize a count variable to keep track of how many submatrices meet the criteria
    # TODO: Use a nested loop to go through each element in the matrix that can be the top-left corner of a 3x3 submatrix

        # TODO: Check if the current 3x3 submatrix has 'E's in all four corners
        # If it does, increment the count

    # TODO: Return the count of submatrices that meet the criteria
    count = 0
    for row in range(len(board) - 2):
        for col in range(len(board[0]) - 2):
            if hasEinAllCorners(board, row, col):
                count += 1
    return count
                

    

# TODO: Define a matrix 'board' with some 'E's and 'P's, representing empty and piece positions respectively
board = [
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'E'],
    ['E', 'P', 'E', 'P'],
    ['P', 'E', 'P', 'E']
]
# TODO: Call the function to count the submatrices and print the result
print(countSubmatricesWithE(board))