class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Initialize the Tribonacci sequence with initial values
        tribonacci_sequence = [0, 1, 1]
        
        # Calculate the Tribonacci sequence up to n
        for i in range(3, n + 1):
            tribonacci_sequence.append(tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3])
        
        return tribonacci_sequence[n]
