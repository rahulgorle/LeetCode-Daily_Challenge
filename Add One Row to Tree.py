class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        queue = [root]
        current_level = 1
        
        while queue:
            if current_level == depth - 1:
                for node in queue:
                    if node.left:
                        new_left = TreeNode(val)
                        new_left.left = node.left
                        node.left = new_left
                    else:
                        node.left = TreeNode(val)
                    
                    if node.right:
                        new_right = TreeNode(val)
                        new_right.right = node.right
                        node.right = new_right
                    else:
                        node.right = TreeNode(val)
                break
            
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            queue = next_level
            current_level += 1
        
        return root
