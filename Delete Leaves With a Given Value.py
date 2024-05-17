class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        # Define a recursive helper function
        def remove_leaves(node):
            if not node:
                return None
            
            # Recursively remove from left and right children
            node.left = remove_leaves(node.left)
            node.right = remove_leaves(node.right)
            
            # Check if current node is a leaf and has the target value
            if not node.left and not node.right and node.val == target:
                return None  # Remove the leaf node
            
            return node
        
        # Call the helper function starting from the root
        return remove_leaves(root)
