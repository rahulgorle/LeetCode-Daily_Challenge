class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        char_indices = {}

        for i, char in enumerate(s):
            if char not in char_indices:
                char_indices[char] = [i, i]
            else:
                char_indices[char][1] = i

        for char in char_indices:
            start, end = char_indices[char]
            unique_chars_in_between = set(s[start+1:end])
            result += len(unique_chars_in_between)

        return result
