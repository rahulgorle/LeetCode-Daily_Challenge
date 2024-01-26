class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        dp = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

        def helper(row, col, moves):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            if moves == 0:
                return 0
            if dp[row][col][moves] != -1:
                return dp[row][col][moves]

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            total_paths = 0

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                total_paths = (total_paths + helper(new_row, new_col, moves - 1)) % MOD

            dp[row][col][moves] = total_paths
            return total_paths

        return helper(startRow, startColumn, maxMove) % MOD
