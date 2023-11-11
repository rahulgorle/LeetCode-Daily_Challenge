from typing import List
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = {i: [] for i in range(n)}
        for edge in edges:
            self.graph[edge[0]].append((edge[1], edge[2]))
        
    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]  # Priority queue with (cost, node)
        visited = set()

        while pq:
            cost, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == node2:
                return cost

            for neighbor, edge_cost in self.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + edge_cost, neighbor))

        return -1
