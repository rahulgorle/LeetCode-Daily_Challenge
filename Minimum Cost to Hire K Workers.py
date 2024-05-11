import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Calculate the wage to quality ratio for each worker and sort them
        workers = sorted((w / q, q) for w, q in zip(wage, quality))
        
        min_cost = float('inf')
        quality_heap = []  # Heap to store negative quality
        
        sum_quality = 0
        
        for ratio, q in workers:
            heapq.heappush(quality_heap, -q)
            sum_quality += q
            
            if len(quality_heap) > k:
                sum_quality += heapq.heappop(quality_heap)
            
            if len(quality_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)
        
        return min_cost
