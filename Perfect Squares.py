class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for square in squares:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]
