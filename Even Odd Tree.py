from typing import Optional
from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        queue = deque([(root, 0)])  # Initialize queue with root and its level
        
        while queue:
            level_size = len(queue)
            prev_val = None  # To keep track of previous value for ordering
            
            for _ in range(level_size):
                node, level = queue.popleft()
                
                # Check if the level index is even or odd
                if level % 2 == 0:  # Even indexed level
                    if node.val % 2 == 0 or (prev_val is not None and prev_val >= node.val):
                        return False
                else:  # Odd indexed level
                    if node.val % 2 != 0 or (prev_val is not None and prev_val <= node.val):
                        return False
                
                prev_val = node.val
                
                # Add children to the queue with their corresponding levels
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
                    
        return True
