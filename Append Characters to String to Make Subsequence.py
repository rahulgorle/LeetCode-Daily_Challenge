class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        t_len = len(t)
        
        # Traverse through string s
        for char in s:
            # If the current character in s matches the current character in t
            if t_index < t_len and char == t[t_index]:
                t_index += 1
        
        # The number of characters left in t after the matched part
        return t_len - t_index
