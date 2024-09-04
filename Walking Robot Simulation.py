class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert list of obstacles into a set for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions in order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0  # Start facing North
        x, y = 0, 0  # Starting position
        
        max_distance_sq = 0  # Track the maximum distance squared
        
        for command in commands:
            if command == -2:  # Turn left
                current_direction = (current_direction - 1) % 4
            elif command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
            else:  # Move forward
                dx, dy = directions[current_direction]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
        
        return max_distance_sq
