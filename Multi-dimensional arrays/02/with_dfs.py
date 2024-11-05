"""
Use dfs to traverse from bottom-right to top-left
"""

def column_traverse(grid, row, col):
    visited = set()  # Keep track of all the visited nodes/cells
    traversed = []
    columns = [[] for _ in range(len(grid[0]))]  # Initialize columns correctly
    
    def dfs(grid, row, col, visited, traversed):
        if not grid:
            return [], []
        rows = len(grid)
        cols = len(grid[0])
        
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited:
            return
        
        visited.add((row, col))
        
        traversed.append(grid[row][col])
        columns[col].append(grid[row][col])
        directions = [(-1, 0), (1, 0), (0, -1)]
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                dfs(grid, new_row, new_col, visited, traversed)
        return traversed, columns[::-1]
    
    return dfs(grid, row, col, visited, traversed)

def main():
    bookshelf = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    traversed, columns = column_traverse(bookshelf, len(bookshelf) - 1, len(bookshelf[0]) - 1)
    print("Traversed:", traversed)
    print("Columns:", columns)

if __name__ == "__main__":
    main()
    # Additional test cases
    bookshelf2 = [
        [1, 2],
        [3, 4]
    ]
    traversed2, columns2 = column_traverse(bookshelf2, len(bookshelf2) - 1, len(bookshelf2[0]) - 1)
    print("Traversed:", traversed2)
    print("Columns:", columns2)

    bookshelf3 = [
        [1]
    ]
    traversed3, columns3 = column_traverse(bookshelf3, len(bookshelf3) - 1, len(bookshelf3[0]) - 1)
    print("Traversed:", traversed3)
    print("Columns:", columns3)

    bookshelf4 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    traversed4, columns4 = column_traverse(bookshelf4, len(bookshelf4) - 1, len(bookshelf4[0]) - 1)
    print("Traversed:", traversed4)
    print("Columns:", columns4)
