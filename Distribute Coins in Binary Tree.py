class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            # Accumulate the number of moves required
            self.moves += abs(left_balance) + abs(right_balance)
            
            # Return the balance of coins at this node
            return node.val + left_balance + right_balance - 1
        
        dfs(root)
        return self.moves
