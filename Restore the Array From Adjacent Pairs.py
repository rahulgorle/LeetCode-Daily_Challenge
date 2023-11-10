from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs):
        adjacency_map = defaultdict(list)

        # Build the adjacency map
        for pair in adjacentPairs:
            u, v = pair
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)

        # Find the start point (a point with only one neighbor)
        start_point = None
        for key, values in adjacency_map.items():
            if len(values) == 1:
                start_point = key
                break

        # Reconstruct the original array
        n = len(adjacentPairs) + 1
        result = [0] * n
        result[0] = start_point

        for i in range(1, n):
            neighbors = adjacency_map[result[i - 1]]
            result[i] = neighbors[0] if neighbors[0] != result[i - 2] else neighbors[1]

        return result
