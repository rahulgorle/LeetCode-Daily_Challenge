class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1  # initialize the smallest number that cannot be formed initially
        added = 0    # number of patches added
        
        i = 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                # add missing itself to nums to cover it
                missing += missing
                added += 1
        
        return added
