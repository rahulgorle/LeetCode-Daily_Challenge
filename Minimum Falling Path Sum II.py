from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Initialize variables to keep track of the minimum and second minimum values and their indices
        min_val = float('inf')
        min_idx = -1
        sec_min_val = float('inf')
        
        # Iterate through the first row to find the minimum and second minimum values
        for j in range(n):
            val = grid[0][j]
            if val < min_val:
                sec_min_val = min_val
                min_val = val
                min_idx = j
            elif val < sec_min_val:
                sec_min_val = val
        
        # Iterate through the grid starting from the second row
        for i in range(1, n):
            # Initialize variables to keep track of the minimum and second minimum values and their indices for the current row
            cur_min_val = float('inf')
            cur_min_idx = -1
            cur_sec_min_val = float('inf')
            
            # Iterate through each column
            for j in range(n):
                # Update the dp value for the current cell
                if j != min_idx:
                    grid[i][j] += min_val
                else:
                    grid[i][j] += sec_min_val
                
                # Update the minimum and second minimum values and their indices for the current row
                val = grid[i][j]
                if val < cur_min_val:
                    cur_sec_min_val = cur_min_val
                    cur_min_val = val
                    cur_min_idx = j
                elif val < cur_sec_min_val:
                    cur_sec_min_val = val
            
            # Update the minimum and second minimum values and their indices for the next row
            min_val = cur_min_val
            min_idx = cur_min_idx
            sec_min_val = cur_sec_min_val
        
        # Find the minimum value in the last row
        min_sum = min(grid[-1])
        
        return min_sum
