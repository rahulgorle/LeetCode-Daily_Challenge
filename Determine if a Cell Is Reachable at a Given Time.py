class Solution:
    def isReachableAtTime(self, startX, startY, targetX, targetY, time):
        if startX == targetX and startY == targetY:
            if time == 1:
                return False
        
        x_diff = abs(startX - targetX)
        y_diff = abs(startY - targetY)
        
        max_diff = max(x_diff, y_diff)
        
        if max_diff <= time:
            return True
        
        return False
