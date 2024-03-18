class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        for start, end_point in points:
            if start > end:
                arrows += 1
                end = end_point
        
        return arrows
