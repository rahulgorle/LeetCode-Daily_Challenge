class Solution:
    def replaceValueInTree(self, root):
        # List to store the sum of node values at each depth
        self.depth_sum = []

        # First DFS to calculate the sum of node values at each depth
        def dfs1(node, d):
            if not node:
                return  # Base case: if the node is null, return

            # If the current depth is greater than or equal to the list size,
            # add a new element with the current node's value
            if d >= len(self.depth_sum):
                self.depth_sum.append(node.val)
            # Otherwise, add the current node's value to the existing sum at this depth
            else:
                self.depth_sum[d] += node.val

            # Recursively call dfs1 for left and right children, incrementing the depth
            dfs1(node.left, d + 1)
            dfs1(node.right, d + 1)

        # Second DFS to replace node values
        def dfs2(node, val, d):
            if not node:
                return  # Base case: if the node is null, return

            # Replace the current node's value with the passed 'val'
            node.val = val

            # Calculate the sum of cousin nodes' values
            # If there's a next depth, get its sum, otherwise use 0
            c = self.depth_sum[d + 1] if d + 1 < len(self.depth_sum) else 0
            # Subtract the values of the current node's children (if they exist)
            c -= (node.left.val if node.left else 0)
            c -= (node.right.val if node.right else 0)

            # Recursively call dfs2 for left and right children
            # Pass the calculated cousin sum 'c' and increment the depth
            if node.left:
                dfs2(node.left, c, d + 1)
            if node.right:
                dfs2(node.right, c, d + 1)

        # First DFS to calculate depth sums
        dfs1(root, 0)
        # Second DFS to replace values, starting with 0 for the root
        dfs2(root, 0, 0)
        # Return the modified root
        return root
