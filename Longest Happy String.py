class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [['a', a], ['b', b], ['c', c]]
        
        def add_char(i):
            result.append(counts[i][0])
            counts[i][1] -= 1

        while True:
            # Sort only if counts are different, reducing redundant operations
            counts.sort(key=lambda x: -x[1])
            
            if counts[0][1] == 0:
                break  # All characters exhausted
            
            # Add the most frequent character if possible
            if len(result) >= 2 and result[-1] == result[-2] == counts[0][0]:
                # If the last two characters are the same, try to add the second most frequent
                if counts[1][1] == 0:
                    break  # No valid characters left to add
                add_char(1)
            else:
                add_char(0)

        return ''.join(result)
