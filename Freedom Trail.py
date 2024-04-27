class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}  # Memoization table to store minimum steps
        
        # Helper function to find the minimum steps to spell the rest of the key
        def dp(index_ring, index_key):
            if index_key == len(key):
                return 0  # Base case: all characters in key have been spelled
            if (index_ring, index_key) in memo:
                return memo[(index_ring, index_key)]  # Return memoized result
            
            # Find the current character's position in the ring
            char = key[index_key]
            min_steps = float('inf')  # Initialize with positive infinity
            
            # Iterate over all possible positions of the ring
            for i in range(len(ring)):
                if ring[i] == char:
                    # Calculate steps to rotate to this position
                    clockwise_steps = (i - index_ring) % len(ring)
                    anticlockwise_steps = (index_ring - i) % len(ring)
                    steps = min(clockwise_steps, anticlockwise_steps) + 1
                    
                    # Recursively find the minimum steps for the remaining key characters
                    next_steps = dp(i, index_key + 1)
                    
                    # Update the minimum steps
                    min_steps = min(min_steps, steps + next_steps)
            
            # Memoize the result
            memo[(index_ring, index_key)] = min_steps
            return min_steps
        
        # Start from the initial alignment of the ring (index 0)
        return dp(0, 0)
