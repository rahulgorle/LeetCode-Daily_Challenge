from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        
        # Combine the input data into a list of tuples and sort by position
        robots = sorted(zip(positions, healths, directions), key=lambda x: x[0])
        
        stack = []
        
        for pos, health, dir in robots:
            if dir == 'R':
                stack.append((pos, health, dir))
            else:
                while stack and stack[-1][2] == 'R':
                    top_pos, top_health, top_dir = stack.pop()
                    if top_health > health:
                        stack.append((top_pos, top_health - 1, top_dir))
                        health = 0
                        break
                    elif top_health < health:
                        health -= 1
                    else:
                        health = 0
                        break
                
                if health > 0:
                    stack.append((pos, health, dir))
        
        # Create a dictionary to store the surviving healths by position for quick lookup
        surviving_health_by_pos = {pos: health for pos, health, dir in stack}
        
        # Extract the healths of surviving robots in the original order of input
        surviving_healths = []
        for pos in positions:
            if pos in surviving_health_by_pos:
                surviving_healths.append(surviving_health_by_pos[pos])
        
        return surviving_healths
