class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict, deque

        # Step 1: Create the graph using adjacency list
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # Step 2: Perform topological sort using Kahn's algorithm (BFS approach)
        topo_order = []
        queue = deque()
        
        # Initialize the queue with nodes having in-degree 0
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Initialize ancestor sets for each node
        ancestors = [set() for _ in range(n)]
        
        # Step 4: Process nodes in topological order
        for node in topo_order:
            for neighbor in graph[node]:
                # Node is an ancestor of neighbor
                ancestors[neighbor].add(node)
                # All ancestors of node are also ancestors of neighbor
                ancestors[neighbor].update(ancestors[node])
        
        # Convert sets to sorted lists
        result = [sorted(list(ancestors[i])) for i in range(n)]
        
        return result
