from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        # Create a set to keep track of visited nodes and initialize the queue.
        visited = set()
        queue = deque()

        # Initialize the queue with all nodes and their corresponding bit masks.
        for i in range(n):
            queue.append((i, 1 << i, 0))

        # Create a target bit mask (all nodes visited) to check when to stop.
        target_mask = (1 << n) - 1

        while queue:
            node, mask, steps = queue.popleft()

            # If the target mask is reached, return the number of steps.
            if mask == target_mask:
                return steps

            for neighbor in graph[node]:
                # Calculate the new bit mask for the neighbor node.
                new_mask = mask | (1 << neighbor)

                # If this state hasn't been visited yet, add it to the queue.
                if (neighbor, new_mask) not in visited:
                    visited.add((neighbor, new_mask))
                    queue.append((neighbor, new_mask, steps + 1))

        return -1  # In case no valid path is found.
