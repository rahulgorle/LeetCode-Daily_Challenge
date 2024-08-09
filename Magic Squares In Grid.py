class Solution:
    def numMagicSquaresInside(self, grid):
        def isMagicSquare(grid, r, c):
            # Extract the 3x3 subgrid
            s = {grid[r+i][c+j] for i in range(3) for j in range(3)}
            if s != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            
            if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or  # Row 1
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or  # Row 2
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15 or  # Row 3
                grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or  # Column 1
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or  # Column 2
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15 or  # Column 3
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or  # Diagonal 1
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):  # Diagonal 2
                return False
            
            return True

        rows, cols = len(grid), len(grid[0])
        count = 0
        
        # Traverse the grid and check for each possible 3x3 subgrid
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] == 5:  # Middle element must be 5 in a valid magic square
                    if isMagicSquare(grid, r, c):
                        count += 1
        
        return count
