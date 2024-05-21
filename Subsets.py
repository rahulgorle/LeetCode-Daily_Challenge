class Solution:
    def subsets(self, nums):
        def backtrack(start, path):
            # Append the current subset to the result list
            result.append(path[:])
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Exclude nums[i] from the current subset before moving to the next
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
