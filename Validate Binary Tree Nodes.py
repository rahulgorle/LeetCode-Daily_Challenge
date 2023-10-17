class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Create a list to track the parent of each node and a set to track visited nodes.
        parents = [-1] * n
        visited = set()
        root_count = 0  # Count of root candidates.

        for i in range(n):
            left, right = leftChild[i], rightChild[i]

            # Check if the current node has two parents.
            if (left != -1 and parents[left] != -1) or (right != -1 and parents[right] != -1):
                return False

            # Set the parent of the left child and right child.
            if left != -1:
                parents[left] = i
            if right != -1:
                parents[right] = i

            # Check if the current node has been visited.
            if i in visited:
                return False

            visited.add(i)

            if parents[i] == -1:
                root_count += 1

        # Ensure that there is exactly one node without a parent (the root).
        if root_count != 1:
            return False

        # Perform a depth-first search to ensure that the tree is connected.
        stack = [i for i in range(n) if parents[i] == -1]

        while stack:
            node = stack.pop()
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])

        # Ensure that all nodes have been visited.
        return len(visited) == n
