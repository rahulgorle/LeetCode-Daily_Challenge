class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(root, leaves):
            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)
                dfs(root.left, leaves)
                dfs(root.right, leaves)

        leaves1, leaves2 = [], []
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2
