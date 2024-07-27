class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        n = len(source)
        
        # Initialize the cost matrix with infinity
        inf = float('inf')
        cost_matrix = [[inf] * 26 for _ in range(26)]
        
        # No cost to change a character to itself
        for i in range(26):
            cost_matrix[i][i] = 0
        
        # Build the initial cost matrix from the given transformations
        for i in range(len(original)):
            orig_idx = ord(original[i]) - ord('a')
            chg_idx = ord(changed[i]) - ord('a')
            cost_matrix[orig_idx][chg_idx] = min(cost_matrix[orig_idx][chg_idx], cost[i])
        
        # Apply Floyd-Warshall algorithm to find all-pairs shortest paths
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if cost_matrix[i][j] > cost_matrix[i][k] + cost_matrix[k][j]:
                        cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]
        
        # Calculate the total minimum cost for each character in source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            s_idx = ord(s) - ord('a')
            t_idx = ord(t) - ord('a')
            if cost_matrix[s_idx][t_idx] == inf:
                return -1
            total_cost += cost_matrix[s_idx][t_idx]
        
        return total_cost
