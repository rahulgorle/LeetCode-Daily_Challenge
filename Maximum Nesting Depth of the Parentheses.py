class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            if char == ')':
                depth -= 1
        
        return max_depth
