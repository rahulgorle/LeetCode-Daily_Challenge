class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        step = 1  # Start with 1 step in one direction
        r, c = rStart, cStart
        result.append([r, c])  # Start from the initial position
        
        if rows * cols == 1:
            return result
        
        while len(result) < rows * cols:
            for i in range(4):  # Each loop handles 4 directions (right, down, left, up)
                dr, dc = directions[i]
                for _ in range(step):  # Walk the number of steps in the current direction
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    if len(result) == rows * cols:
                        return result
                # Increment step after walking in right and down direction (i.e., after i = 1)
                if i == 1 or i == 3:
                    step += 1
        
        return result
