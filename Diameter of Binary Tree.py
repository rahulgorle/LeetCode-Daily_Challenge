class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Helper function to calculate height of the tree
        def height(node):
            nonlocal diameter
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            # Diameter at this node is the sum of heights of its left and right subtrees
            diameter = max(diameter, left_height + right_height)
            # Return the height of the current subtree
            return 1 + max(left_height, right_height)

        diameter = 0
        height(root)
        return diameter
