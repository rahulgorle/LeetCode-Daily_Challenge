from typing import Optional

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, count):
            if not node:
                return 0
            
            count[node.val] += 1
            if not node.left and not node.right:
                result = 1 if sum(val_count % 2 == 1 for val_count in count) <= 1 else 0
            else:
                result = dfs(node.left, count) + dfs(node.right, count)

            # Backtrack: restore the count to its original state
            count[node.val] -= 1
            return result
        
        return dfs(root, [0] * 10)
