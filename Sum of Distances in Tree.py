class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        res = [0] * n

        def dfs(node, parent):
            nonlocal res
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs_propagate(node, parent):
            nonlocal res
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs_propagate(child, node)

        dfs(0, -1)
        dfs_propagate(0, -1)

        return res
