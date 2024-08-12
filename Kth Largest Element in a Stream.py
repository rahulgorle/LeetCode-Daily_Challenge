import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Heapify the nums list in O(n) time
        
        # Maintain the heap size to k by popping the smallest elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value to the heap
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            # Push the new value and pop the smallest value in one operation
            heapq.heappushpop(self.min_heap, val)
        
        # The smallest value in the heap (root) is the kth largest element
        return self.min_heap[0]
