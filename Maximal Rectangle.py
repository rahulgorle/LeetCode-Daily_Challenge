from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)  # Add an extra element for boundary checking
        max_area = 0
        
        for row in matrix:
            # Update heights for each row
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            
            # Calculate the largest area using the updated heights
            stack = [-1]  # Initialize stack with a sentinel value
            for j in range(cols + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
        
        return max_area
