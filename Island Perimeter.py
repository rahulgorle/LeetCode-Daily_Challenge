from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i < rows - 1 and grid[i + 1][j] == 1:  # Check bottom
                        perimeter -= 2
                    if j < cols - 1 and grid[i][j + 1] == 1:  # Check right
                        perimeter -= 2
        
        return perimeter
