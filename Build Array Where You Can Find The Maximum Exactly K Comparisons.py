MOD = 10**9 + 7

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        dp_cur = [[0 for _ in range(k+1)] for _ in range(m+1)]
        dp_prev = [[0 for _ in range(k+1)] for _ in range(m+1)]
        
        # Initialize dp for base cases
        for j in range(1, m+1):
            dp_cur[j][1] = 1
        
        for i in range(2, n+1):
            dp_cur, dp_prev = dp_prev, dp_cur  # Swap current and previous arrays
            for j in range(1, m+1):
                for cost in range(1, k+1):
                    dp_cur[j][cost] = j * dp_prev[j][cost] % MOD  # Increase the maximum element
                    for prev in range(1, j):
                        dp_cur[j][cost] = (dp_cur[j][cost] + dp_prev[prev][cost-1]) % MOD  # Increase the search_cost
        
        result = sum(dp_cur[j][k] for j in range(1, m+1)) % MOD
        return result
