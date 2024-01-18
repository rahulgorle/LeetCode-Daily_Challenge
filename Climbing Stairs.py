class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * (n + 1)

        # Base cases
        dp[1] = 1
        dp[2] = 2

        # Calculate the number of ways for each step starting from the third step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # The result is stored in the last element of the dp array
        return dp[n]
