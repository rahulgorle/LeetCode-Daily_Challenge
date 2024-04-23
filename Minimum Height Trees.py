from collections import defaultdict, deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, so its root is the only MHT
        elif n == 2:
            return [0, 1]  # Both nodes are roots of MHT
        
        # Step 1: Construct the graph
        graph = defaultdict(list)
        degrees = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        # Find leaves (nodes with only one edge)
        leaves = deque([i for i in range(n) if degrees[i] == 1])
        
        # Step 2: Remove leaves iteratively until 1 or 2 nodes left
        remaining_nodes = n
        while remaining_nodes > 2:
            num_leaves = len(leaves)
            remaining_nodes -= num_leaves
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        leaves.append(neighbor)
        
        # The remaining nodes in 'leaves' are the roots of MHTs
        return list(leaves)
