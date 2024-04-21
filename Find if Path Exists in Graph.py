class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Construct adjacency list from edges
        adjacency_list = [[] for _ in range(n)]
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        # Perform BFS
        visited = set()
        queue = [source]
        front, rear = 0, 0
        while front <= rear:
            current = queue[front]
            front += 1
            if current == destination:
                return True
            visited.add(current)
            for neighbor in adjacency_list[current]:
                if neighbor not in visited:
                    rear += 1
                    queue.append(neighbor)
        
        return False
