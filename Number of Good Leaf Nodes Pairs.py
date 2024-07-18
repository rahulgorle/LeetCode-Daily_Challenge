class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_dists = dfs(node.left)
            right_dists = dfs(node.right)
            
            for ld in left_dists:
                for rd in right_dists:
                    if ld + rd <= distance:
                        self.ans += 1
            
            # Return the distances incremented by 1 for the current node
            return [d + 1 for d in left_dists + right_dists if d + 1 <= distance]

        self.ans = 0
        dfs(root)
        return self.ans
