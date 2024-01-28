from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # Calculate the cumulative sum for each row
        for i in range(rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i][j - 1]

        # Iterate through all possible pairs of columns
        for start_col in range(cols):
            for end_col in range(start_col, cols):
                prefix_sum = {0: 1}
                current_sum = 0

                # Iterate through each row and calculate the current sum
                for row in range(rows):
                    current_sum += matrix[row][end_col] - (matrix[row][start_col - 1] if start_col > 0 else 0)

                    # Check if there is a subarray with sum equal to target
                    if current_sum - target in prefix_sum:
                        count += prefix_sum[current_sum - target]

                    # Update the prefix sum dictionary
                    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count
