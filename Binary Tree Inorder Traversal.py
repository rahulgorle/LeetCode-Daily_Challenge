# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the current node
            current = stack.pop()
            result.append(current.val)

            # Move to the right subtree
            current = current.right

        return result
