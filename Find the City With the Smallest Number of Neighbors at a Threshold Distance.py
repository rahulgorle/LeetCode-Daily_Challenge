import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create an adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Function to perform Dijkstra's algorithm
        def dijkstra(start: int) -> List[int]:
            distances = [float('inf')] * n
            distances[start] = 0
            min_heap = [(0, start)]  # (distance, node)
            
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                
                if current_dist > distances[u]:
                    continue
                
                for v, weight in graph[u]:
                    distance = current_dist + weight
                    if distance < distances[v]:
                        distances[v] = distance
                        heapq.heappush(min_heap, (distance, v))
            
            return distances
        
        # Determine the number of reachable cities for each city
        min_reachable = float('inf')
        best_city = -1
        
        for i in range(n):
            distances = dijkstra(i)
            reachable_count = sum(dist <= distanceThreshold for dist in distances)
            
            if reachable_count < min_reachable or (reachable_count == min_reachable and i > best_city):
                min_reachable = reachable_count
                best_city = i
        
        return best_city
