"""
Columnr ZigZag Traversals in a Matrix

-> Bottom - right corner starting.
Here's the task: you've been given a 2D matrix consisting of individual cells, each holding a unique integer value. Your goal is to create a function that will traverse this matrix, starting at the bottom right cell. From there, you'll travel up to the top of the same column, then move left to the next column, and then continue downwards from the top of this new column. After reaching the bottom of the column, you again move left and start moving upwards. This unique traverse pattern will be performed until all the cells have been visited.

Consider this small 

3×4 matrix as an example:

Python

[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


Solution Building: Step 1
The first step towards a solution is understanding the dimensions of the matrix with which we're working. We can do this using Python's built-in len() function. Let's set up our function and identify the matrix size:


def column_traverse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    
Solution Building: Step 2
Now that we're aware of the matrix dimensions, we should establish the starting point (bottom-right) and the direction of travel (upwards initially). Additionally, we'll need a list to keep track of the cells we've visited in order:

def column_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    direction = 'up'
    row, col = rows - 1, cols - 1
    output = []  

Solution Building: Step 3
It's time to go exploring! We'll now implement a while loop to traverse the matrix. This loop will continue until we 
have covered all the cells in the matrix. As we "visit" each cell, we'll add the value in the cell to our list.

def column_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    direction = 'up'
    row, col = rows - 1, cols - 1
    output = []
    
    while len(output) < rows * cols:
        output.append(matrix[row][col])
        
        if direction == 'up':
            if row - 1 < 0:
                direction = 'down'
                col -= 1
            else:
                row -= 1
        else:
            if row + 1 == rows:
                direction = 'up'
                col -= 1
            else:
                row += 1

    return output 
    
raverse Using Decreasing Range
Let's explore one more way of traversal. We can leverage the utility of Python's range() function to traverse a 2D matrix in reverse order. This function, known for its flexibility, can also create a sequence that decrements.

To achieve this, we use range() with three arguments - start, stop, and step. By setting step to -1, we generate a decreasing sequence.

Consider our familiar 

3×4 matrix:


[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


Using a decrementing range(), the reverse traverse pattern would produce this list: [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1].

Here's how we can implement this reverse traversal:

def reverse_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    output = []

    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            output.append(matrix[row][col])
            
    return output


In this function, we start the range() for row from rows - 1 and run it till -1 (which is excluded), decrementing at each step. Similarly, our nested range() for col starts from cols - 1 and goes till -1. 
This allows us to start from the bottom-right corner and traverse leftwards, then upwards, covering the entire matrix in reverse order.
"""