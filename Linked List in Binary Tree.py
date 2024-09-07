class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # Check if the linked list starting from head matches the downward path from the current tree node.
        def dfs(tree_node, list_node):
            if not list_node:  # If the entire linked list is matched, return True
                return True
            if not tree_node:  # If we have reached a leaf node in the tree, return False
                return False
            if tree_node.val != list_node.val:  # If the current values don't match, return False
                return False
            # Proceed to check the left and right children of the current tree node
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)

        # Main function to traverse the tree and look for a subpath starting at any node.
        def traverse(tree_node):
            if not tree_node:  # Base case, empty tree
                return False
            # Check if we can start a subpath from this node or continue traversing the tree
            return dfs(tree_node, head) or traverse(tree_node.left) or traverse(tree_node.right)
        
        return traverse(root)
