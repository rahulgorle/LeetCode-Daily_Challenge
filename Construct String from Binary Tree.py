# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def helper(node, result):
            if not node:
                return

            result.write(str(node.val))

            if node.left or node.right:
                result.write("(")
                helper(node.left, result)
                result.write(")")

            if node.right:
                result.write("(")
                helper(node.right, result)
                result.write(")")

        result_stream = io.StringIO()
        helper(root, result_stream)
        return result_stream.getvalue()
        
