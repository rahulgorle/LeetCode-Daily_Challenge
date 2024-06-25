class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Total sum accumulator
        total = 0
        
        # Reverse in-order traversal function
        def reverse_inorder(node):
            nonlocal total
            if node:
                # Traverse the right subtree
                reverse_inorder(node.right)
                
                # Update the total and node value
                total += node.val
                node.val = total
                
                # Traverse the left subtree
                reverse_inorder(node.left)
        
        # Start the traversal from the root
        reverse_inorder(root)
        return root
