from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        
        # Initialize the matrix with zeros
        matrix = [[0] * cols for _ in range(rows)]
        
        # Fill the matrix
        i, j = 0, 0
        while i < rows and j < cols:
            # Determine the value to be placed in the cell
            value = min(rowSum[i], colSum[j])
            matrix[i][j] = value
            
            # Update the rowSum and colSum
            rowSum[i] -= value
            colSum[j] -= value
            
            # Move to the next row or column
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        
        return matrix
