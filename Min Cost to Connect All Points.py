class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] == x:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                parent[root_x] = root_y

        n = len(points)
        edges = []  # Store edges and their distances

        # Calculate distances and create edges
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((distance, i, j))

        # Sort edges by distance in ascending order
        edges.sort()

        parent = list(range(n))  # Initialize a parent array for union-find

        min_cost = 0
        edge_count = 0

        # Kruskal's algorithm
        for edge in edges:
            distance, u, v = edge
            if find(parent, u) != find(parent, v):
                union(parent, u, v)
                min_cost += distance
                edge_count += 1
                if edge_count == n - 1:
                    break

        return min_cost
