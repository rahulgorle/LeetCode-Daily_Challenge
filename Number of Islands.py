class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(grid, i, j):
            stack = [(i, j)]
            while stack:
                row, col = stack.pop()
                if 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] == '1':
                    grid[row][col] = '0'  # Mark as visited
                    stack.extend([(row+1, col), (row-1, col), (row, col+1), (row, col-1)])

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)
        
        return num_islands
