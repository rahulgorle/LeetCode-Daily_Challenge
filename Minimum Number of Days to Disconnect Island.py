from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands(grid):
            m, n = len(grid), len(grid[0])
            visited = [[False] * n for _ in range(m)]
            
            def dfs(x, y):
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
            
            island_count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        dfs(i, j)
                        island_count += 1
            
            return island_count
        
        def is_disconnected(grid):
            return count_islands(grid) != 1
        
        if is_disconnected(grid):
            return 0
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected(grid):
                        return 1
                    grid[i][j] = 1
        
        return 2
