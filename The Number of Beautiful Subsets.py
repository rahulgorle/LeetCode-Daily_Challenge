class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(index, current_set):
            nonlocal count
            if index == len(nums):
                if current_set:
                    count += 1
                return
            
            # Skip the current element
            backtrack(index + 1, current_set)
            
            # Include the current element if it keeps the subset beautiful
            can_include = True
            for num in current_set:
                if abs(num - nums[index]) == k:
                    can_include = False
                    break
            
            if can_include:
                current_set.append(nums[index])
                backtrack(index + 1, current_set)
                current_set.pop()

        count = 0
        nums.sort()  # Optional: to handle elements in a sorted order
        backtrack(0, [])
        return count
