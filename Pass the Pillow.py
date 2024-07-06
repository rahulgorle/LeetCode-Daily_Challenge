class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Calculate the effective time within a single cycle
        effective_time = time % (2 * (n - 1))
        
        # Determine the position based on the effective time
        if effective_time < n:
            # Pillow is moving forward
            return 1 + effective_time
        else:
            # Pillow is moving backward
            return 2 * n - 1 - effective_time
