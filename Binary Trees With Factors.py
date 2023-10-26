class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        dp = [1] * n  # Initialize all elements to 1 because a single node is also a binary tree.

        # Create a dictionary for quick lookup of array elements.
        arr_set = set(arr)

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in arr_set:
                    dp[i] = (dp[i] + dp[j] * dp[arr.index(arr[i] // arr[j])]) % MOD

        return sum(dp) % MOD
