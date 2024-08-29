class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Function to perform DFS to find all connected nodes (stones)
        def dfs(node, visited, graph):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, graph)
        
        graph = defaultdict(list)
        
        # Build the graph
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = set()
        num_components = 0
        
        # Count the number of connected components
        for i in range(len(stones)):
            if i not in visited:
                dfs(i, visited, graph)
                num_components += 1
        
        # The maximum number of stones we can remove is total stones minus number of components
        return len(stones) - num_components
