import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []  # priority queue to store the differences between heights
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(pq, diff)  # push positive height differences to the priority queue
                if len(pq) > ladders:  # if we have more height differences than available ladders
                    bricks -= heapq.heappop(pq)  # use bricks instead of a ladder
                    if bricks < 0:  # if we run out of bricks, we can't go further
                        return i
        return len(heights) - 1  # if we reach here, we can go to the last building
