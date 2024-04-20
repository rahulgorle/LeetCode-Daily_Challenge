class Solution:
    def findFarmland(self, land):
        m, n = len(land), len(land[0])
        farmlands = []

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    # Find the bottom-right corner of the current farmland group
                    r, c = i, j
                    while r < m and land[r][j] == 1:
                        c = j
                        while c < n and land[r][c] == 1:
                            c += 1
                        r += 1
                    # Add the coordinates of the current farmland group to the result
                    farmlands.append([i, j, r - 1, c - 1])
                    # Mark the farmland cells as visited
                    for x in range(i, r):
                        for y in range(j, c):
                            land[x][y] = 0

        return farmlands
