import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_effort = [[float('inf')] * cols for _ in range(rows)]

        min_effort[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, row, col)

        while heap:
            effort, row, col = heapq.heappop(heap)

            if row == rows - 1 and col == cols - 1:
                return effort

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                ):
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))

                    if new_effort < min_effort[new_row][new_col]:
                        min_effort[new_row][new_col] = new_effort
                        heapq.heappush(heap, (new_effort, new_row, new_col))

        return -1  # In case there is no valid path
