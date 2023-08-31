class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_jumps = [0] * (n + 1)  # Stores the maximum jump we can make from each index
        for i in range(len(ranges)):
            left, right = max(0, i - ranges[i]), min(n, i + ranges[i])
            max_jumps[left] = max(max_jumps[left], right - left)
        
        curr_end, next_end = 0, 0
        taps = 0
        
        i = 0
        while curr_end < n:
            while i <= curr_end:
                next_end = max(next_end, i + max_jumps[i])
                i += 1
            if curr_end == next_end:
                return -1
            curr_end = next_end
            taps += 1
        
        return taps
