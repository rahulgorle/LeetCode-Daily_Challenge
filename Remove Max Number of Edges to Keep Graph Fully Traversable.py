class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent_a = list(range(n + 1))
        parent_b = list(range(n + 1))
        rank_a = [0] * (n + 1)
        rank_b = [0] * (n + 1)
        
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False
        
        edges_needed = 0
        
        # Add type 3 edges to both union finds
        for t, u, v in edges:
            if t == 3:
                if union(parent_a, rank_a, u, v):
                    union(parent_b, rank_b, u, v)
                    edges_needed += 1
        
        # Add type 1 edges to Alice's union find
        for t, u, v in edges:
            if t == 1:
                if union(parent_a, rank_a, u, v):
                    edges_needed += 1
        
        # Add type 2 edges to Bob's union find
        for t, u, v in edges:
            if t == 2:
                if union(parent_b, rank_b, u, v):
                    edges_needed += 1
        
        # Check if both Alice and Bob can traverse the whole graph
        root_a = find(parent_a, 1)
        root_b = find(parent_b, 1)
        
        for i in range(2, n + 1):
            if find(parent_a, i) != root_a or find(parent_b, i) != root_b:
                return -1
        
        return len(edges) - edges_needed
