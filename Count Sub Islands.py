class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True
            if grid1[i][j] == 0:
                return False
            
            grid2[i][j] = 0  # Mark as visited
            
            top = dfs(i - 1, j)
            bottom = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            
            return top and bottom and left and right
        
        sub_islands_count = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_islands_count += 1
        
        return sub_islands_count
