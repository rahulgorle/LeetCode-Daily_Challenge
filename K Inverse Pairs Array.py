class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            prefix_sum = 0

            for j in range(k + 1):
                prefix_sum = (prefix_sum + dp[j]) % MOD

                if j >= i:
                    prefix_sum = (prefix_sum - dp[j - i] + MOD) % MOD

                new_dp[j] = prefix_sum

            dp = new_dp

        return dp[k]
