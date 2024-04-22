from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        
        queue = deque(["0000"])
        visited = set(["0000"])
        moves = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current == target:
                    return moves
                
                for i in range(4):
                    for move in [-1, 1]:
                        next_state = current[:i] + str((int(current[i]) + move) % 10) + current[i+1:]
                        if next_state not in deadends_set and next_state not in visited:
                            queue.append(next_state)
                            visited.add(next_state)
            moves += 1
        
        return -1
