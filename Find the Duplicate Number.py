class Solution:
    def findDuplicate(self, nums):
        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # Return the duplicate number
        return slow
