class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxPosition = min(arrLen - 1, steps)
        dp = [0] * (maxPosition + 1)
        dp[0] = 1

        for i in range(1, steps + 1):
            next_dp = [0] * (maxPosition + 1)
            for j in range(maxPosition + 1):
                next_dp[j] = dp[j]
                if j > 0:
                    next_dp[j] = (next_dp[j] + dp[j - 1]) % MOD
                if j < maxPosition:
                    next_dp[j] = (next_dp[j] + dp[j + 1]) % MOD
            dp = next_dp

        return dp[0]
