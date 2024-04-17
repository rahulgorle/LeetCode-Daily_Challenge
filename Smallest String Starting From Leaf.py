class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, path):
            if not node:
                return
            path = chr(node.val + ord('a')) + path
            if not node.left and not node.right:  # If it's a leaf
                paths.append(path)
            dfs(node.left, path)
            dfs(node.right, path)

        paths = []
        dfs(root, "")
        return min(paths)
