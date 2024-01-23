from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(mask, s):
            for char in s:
                char_mask = 1 << (ord(char) - ord('a'))
                if mask & char_mask:
                    return False
                mask |= char_mask
            return True

        def backtrack(index, mask, length):
            nonlocal max_length
            max_length = max(max_length, length)

            for i in range(index, len(arr)):
                if is_unique(mask, arr[i]):
                    new_mask = mask
                    for char in arr[i]:
                        new_mask |= 1 << (ord(char) - ord('a'))
                    backtrack(i + 1, new_mask, length + len(arr[i]))

        max_length = 0
        backtrack(0, 0, 0)
        return max_length
