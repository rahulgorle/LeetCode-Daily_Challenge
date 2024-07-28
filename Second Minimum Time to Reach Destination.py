from collections import deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Step 1: Create the graph as an adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Initialize the distances for first and second minimum paths
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        
        # Step 3: Use a deque to manage BFS traversal
        queue = deque([(1, 1)])
        
        while queue:
            node, freq = queue.popleft()
            current_time = dist1[node] if freq == 1 else dist2[node]
            
            # Calculate the wait time if the traffic signal is red
            if (current_time // change) % 2:
                current_time = change * (current_time // change + 1) + time
            else:
                current_time += time
            
            # Traverse the neighbors
            for neighbor in graph[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = current_time
                    queue.append((neighbor, 1))
                elif dist2[neighbor] == -1 and dist1[neighbor] != current_time:
                    if neighbor == n:
                        return current_time
                    dist2[neighbor] = current_time
                    queue.append((neighbor, 2))
        
        return 0
