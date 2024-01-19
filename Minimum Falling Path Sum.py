from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)

        for row in range(1, n):
            for col in range(n):
                left = matrix[row - 1][col - 1] if col - 1 >= 0 else float('inf')
                up = matrix[row - 1][col]
                right = matrix[row - 1][col + 1] if col + 1 < n else float('inf')

                matrix[row][col] += min(left, up, right)

        return min(matrix[-1])
