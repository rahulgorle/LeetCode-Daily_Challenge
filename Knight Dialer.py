class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        # Initialize dp array to store the number of ways to reach each number for each step
        dp = [1] * 10

        for _ in range(n - 1):
            # Create a new dp array for the current step
            new_dp = [0] * 10

            for i in range(10):
                for neighbor in moves[i]:
                    new_dp[neighbor] = (new_dp[neighbor] + dp[i]) % MOD

            dp = new_dp

        return sum(dp) % MOD
