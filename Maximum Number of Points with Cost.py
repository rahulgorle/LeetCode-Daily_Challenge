class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        
        # Initialize dp with the first row's points
        dp = points[0][:]
        
        # Process each row from the second to the last row
        for r in range(1, m):
            new_dp = [0] * n
            
            # Left-to-right pass
            max_left = dp[0]
            for c in range(n):
                max_left = max(max_left, dp[c] + c)
                new_dp[c] = points[r][c] + max_left - c
            
            # Right-to-left pass
            max_right = dp[n-1] - (n-1)
            for c in range(n-2, -1, -1):
                max_right = max(max_right, dp[c] - c)
                new_dp[c] = max(new_dp[c], points[r][c] + max_right + c)
            
            dp = new_dp
        
        # The result is the maximum value in dp after processing all rows
        return max(dp)
