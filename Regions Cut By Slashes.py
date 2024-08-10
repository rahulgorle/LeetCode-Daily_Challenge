class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Each square is divided into 4 triangles, so we have 4*n*n regions
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                if grid[i][j] == '/':
                    union(base + 0, base + 3)  # connect top-left to bottom-right
                    union(base + 1, base + 2)  # connect top-right to bottom-left
                elif grid[i][j] == '\\':
                    union(base + 0, base + 1)  # connect top-left to top-right
                    union(base + 2, base + 3)  # connect bottom-left to bottom-right
                else:
                    union(base + 0, base + 1)
                    union(base + 1, base + 2)
                    union(base + 2, base + 3)
                
                # Union the adjacent triangles from different cells
                if i > 0:  # connect with top cell
                    union(base + 0, base - 4 * n + 2)
                if j > 0:  # connect with left cell
                    union(base + 3, base - 4 + 1)
        
        # Count the number of distinct regions
        return sum(find(x) == x for x in range(4 * n * n))
