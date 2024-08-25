class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, output = [], []
        last_visited_node = None
        current = root
        
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                # If right child exists and traversing node from left child, then move to right child
                if peek_node.right and last_visited_node != peek_node.right:
                    current = peek_node.right
                else:
                    output.append(peek_node.val)
                    last_visited_node = stack.pop()
        
        return output
