import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Min-heap to store the smallest element and its list index and element index
        min_heap = []
        max_value = float('-inf')  # Track the maximum value in the current range
        
        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])
        
        # Initialize the smallest range as [min, max]
        result_range = [float('-inf'), float('inf')]
        
        while min_heap:
            # Get the smallest element from the heap
            min_value, list_idx, element_idx = heapq.heappop(min_heap)
            
            # Update the result range if the current range is smaller
            if max_value - min_value < result_range[1] - result_range[0]:
                result_range = [min_value, max_value]
            
            # If this list has more elements, push the next element into the heap
            if element_idx + 1 < len(nums[list_idx]):
                next_value = nums[list_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_value, list_idx, element_idx + 1))
                # Update the max value if necessary
                max_value = max(max_value, next_value)
            else:
                # If any list is exhausted, we can't include one element from each list anymore
                break
        
        return result_range
