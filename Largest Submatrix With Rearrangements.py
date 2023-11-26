from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        # Calculate heights of consecutive 1s ending at each column
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        # Calculate the maximum area without explicit sorting
        max_area = 0
        for i in range(m):
            row = matrix[i]
            row.sort()
            for j in range(n):
                max_area = max(max_area, row[j] * (n - j))

        return max_area
