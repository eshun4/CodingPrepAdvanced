"""
1. Create  function that tansposes a matrix. e.g. flips it to another direction
2. Create na recursive method that transpose it n number of times
"""


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    results = [[0] * rows for _ in range(cols)]
    
    # Use  nested for loop to flip it
    for i in range(rows):
        for j in range(cols):
            results[j][i] = matrix[i][j]
    return results


def transpose_matrix_recursive(matrix, n):
    if n == 0:
        return matrix
    
    transposed = transpose_matrix(matrix)
    return transpose_matrix_recursive(transposed, n - 1)


def main():
    matrix = [
        [1, 2, 3], 
        [4, 5, 6],
    ]
    
    print(transpose_matrix(matrix))
    print(transpose_matrix_recursive(matrix, 2))

if __name__ == "__main__":
    main()
            