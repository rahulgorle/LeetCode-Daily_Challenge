class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # Sort the array
        
        # Initialize pointers
        left, right = 0, len(people) - 1
        boats = 0
        
        # Use two pointers approach
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Move lighter person to next position
            right -= 1  # Move heavier person to next position
            boats += 1  # Increment boats count
        
        return boats
