class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraversal(node):
            nonlocal prev_val, max_freq, current_freq, modes

            if node is None:
                return

            inOrderTraversal(node.left)

            if node.val == prev_val:
                current_freq += 1
            else:
                current_freq = 1

            if current_freq == max_freq:
                modes.append(node.val)
            elif current_freq > max_freq:
                max_freq = current_freq
                modes = [node.val]

            prev_val = node.val

            inOrderTraversal(node.right)

        if not root:
            return []

        prev_val = None
        max_freq = 0
        current_freq = 0
        modes = []

        inOrderTraversal(root)

        return modes
