class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D array to store the number of unique paths for each column
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                # Update dp[j] with the sum of dp[j] (from the previous row) and dp[j-1] (from the current row)
                dp[j] += dp[j - 1]

        return dp[n - 1]
