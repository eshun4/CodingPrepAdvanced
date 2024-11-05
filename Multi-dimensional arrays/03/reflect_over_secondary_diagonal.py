"""
Can you fill in the code to reflect the given matrix over its secondary diagonal?

Note that the secondary diagonal of the matrix is the line starting from the upper-right corner 
and ending in the bottom-left corner of the matrix. In the following matrix, we fill the elements
in the secondary diagonal with 1s:

Python
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0

As an example, in a 4x4 matrix, reflecting the matrix over its secondary diagonal means that the elements
matrix[0][0] and matrix[3][3] should be swapped, matrix[0][1] and matrix[2][3] 
should be swapped, etc. Elements in the secondary diagonal stay at the same place.

"""


def reflectOverSecondaryDiagonal(matrix):
    size = len(matrix)
    new_matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        # TODO: Complete the code to obtain the reflected square matrix in new_matrix.
        for j in range(size -1, -1, -1):
            new_matrix[size-j-1][size-i-1] = matrix[i][j]
    return new_matrix

# Example square matrix to reflect over the secondary diagonal
square_matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

# Call the function and print the transformed matrix
transformed_matrix = reflectOverSecondaryDiagonal(square_matrix)
# TODO: Call the function on square_matrix and store the result in transformed_matrix.
print(transformed_matrix)
# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]