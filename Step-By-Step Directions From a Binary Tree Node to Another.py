class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        def findLCA(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        def findPath(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True
            if node.left and findPath(node.left, value, path):
                path.append('L')
                return True
            if node.right and findPath(node.right, value, path):
                path.append('R')
                return True
            return False

        lca = findLCA(root, startValue, destValue)
        path_to_start = []
        path_to_dest = []
        findPath(lca, startValue, path_to_start)
        findPath(lca, destValue, path_to_dest)
        
        # Reverse paths to get the correct order from lca to nodes
        path_to_start = path_to_start[::-1]
        path_to_dest = path_to_dest[::-1]
        
        # All moves from start to LCA will be 'U'
        result = ['U'] * len(path_to_start)
        result += path_to_dest
        return ''.join(result)
