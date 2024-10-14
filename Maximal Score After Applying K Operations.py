import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums into a max-heap by using negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        
        for _ in range(k):
            # Pop the largest element (negated to retrieve the original value)
            max_value = -heapq.heappop(max_heap)
            score += max_value
            
            # Optimized integer division to compute ceil(max_value / 3)
            new_value = (max_value + 2) // 3
            
            # Push the new value back into the heap as negative
            heapq.heappush(max_heap, -new_value)
        
        return score
