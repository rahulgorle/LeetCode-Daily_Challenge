from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                neighbors_sum, count = 0, 0

                # Iterate over the 3x3 neighborhood using a sliding window
                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        neighbors_sum += img[x][y]
                        count += 1

                result[i][j] = neighbors_sum // count

        return result
