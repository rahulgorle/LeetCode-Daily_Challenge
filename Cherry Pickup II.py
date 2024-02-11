class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Define a 3D DP array to store the maximum cherries collected
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]
        
        # Helper function to recursively compute the maximum cherries collected
        def helper(r, c1, c2):
            # If out of bounds or hitting a thorn, return -infinity
            if r == rows or c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return float('-inf')
            # If already visited, return the value
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
            # If reached the bottom row, return the cherry at the current cell
            if r == rows - 1:
                return grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
            
            # Calculate cherries collected for both robots
            cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
            
            # Calculate the maximum cherries collected recursively
            max_cherries = 0
            for nc1 in range(c1 - 1, c1 + 2):
                for nc2 in range(c2 - 1, c2 + 2):
                    max_cherries = max(max_cherries, helper(r + 1, nc1, nc2))
            
            # Update the dp array with the maximum cherries collected
            dp[r][c1][c2] = cherries + max_cherries
            return dp[r][c1][c2]
        
        # Start the recursion from the top row and the top corners for both robots
        return max(0, helper(0, 0, cols - 1))
