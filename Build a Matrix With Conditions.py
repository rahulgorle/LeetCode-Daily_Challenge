from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topological_sort(k: int, conditions: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            top_order = []
            
            while queue:
                node = queue.popleft()
                top_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(top_order) == k:
                return top_order
            else:
                return []
        
        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {val: i for i, val in enumerate(row_order)}
        col_pos = {val: i for i, val in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for val in range(1, k + 1):
            r, c = row_pos[val], col_pos[val]
            matrix[r][c] = val
        
        return matrix
