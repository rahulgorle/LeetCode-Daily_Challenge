class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the basket positions
        position.sort()
        
        # Binary search for the maximum minimum distance
        left, right = 1, position[-1] - position[0]
        
        def canPlaceBalls(d):
            # Place the first ball at the first position
            count, last_position = 1, position[0]
            # Try to place the remaining balls
            for i in range(1, len(position)):
                if position[i] - last_position >= d:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        while left <= right:
            mid = (left + right) // 2
            if canPlaceBalls(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
