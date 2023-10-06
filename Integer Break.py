class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        # Calculate the number of 3's that can be obtained
        num_threes = n // 3
        
        # Handle the case when n is exactly divisible by 3
        if n % 3 == 0:
            return 3 ** num_threes
        
        # Handle the case when n leaves a remainder of 1 when divided by 3
        if n % 3 == 1:
            return 3 ** (num_threes - 1) * 4
        
        # Handle the case when n leaves a remainder of 2 when divided by 3
        if n % 3 == 2:
            return 3 ** num_threes * 2
