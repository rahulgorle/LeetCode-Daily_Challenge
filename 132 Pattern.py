class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # Initialize a stack to store potential candidates for the "32" pattern.
        stack = []
        
        # Initialize the minimum value for "1".
        min_val = float('-inf')
        
        # Traverse the array from right to left.
        for i in range(n - 1, -1, -1):
            # If the current number is less than the minimum value, return True because we've found a "132" pattern.
            if nums[i] < min_val:
                return True
            
            # While there are elements in the stack and the current number is greater than the top element,
            # update the minimum value to the top element and pop the stack.
            while stack and nums[i] > stack[-1]:
                min_val = stack.pop()
            
            # Add the current number to the stack as a potential candidate for the "32" pattern.
            stack.append(nums[i])
        
        # If we reach this point, there is no "132" pattern in the array.
        return False
