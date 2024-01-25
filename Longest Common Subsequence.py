class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Use two 1D arrays to store the lengths of common subsequences
        dp1 = [0] * (n + 1)
        dp2 = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp2[j] = dp1[j - 1] + 1
                else:
                    dp2[j] = max(dp1[j], dp2[j - 1])

            # Swap the arrays for the next iteration
            dp1, dp2 = dp2, dp1

        # The length of the longest common subsequence is stored in the last element of dp1
        return dp1[n]
