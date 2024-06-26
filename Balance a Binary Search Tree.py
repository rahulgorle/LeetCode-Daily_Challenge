class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Perform an inorder traversal to get the sorted values
        def inorderTraversal(node):
            stack, inorder = [], []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
            return inorder
        
        sorted_values = inorderTraversal(root)
        
        # Step 2: Construct a balanced BST from the sorted values
        def buildBalancedBST(nums, left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = buildBalancedBST(nums, left, mid - 1)
            node.right = buildBalancedBST(nums, mid + 1, right)
            return node
        
        return buildBalancedBST(sorted_values, 0, len(sorted_values) - 1)
