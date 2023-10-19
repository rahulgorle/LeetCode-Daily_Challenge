class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Helper function to find the next valid character index in a string
        def find_next_valid_index(string, index):
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    return index
                index -= 1
            return index
        
        i = len(s) - 1  # Pointer for string s
        j = len(t) - 1  # Pointer for string t
        
        while i >= 0 or j >= 0:
            i = find_next_valid_index(s, i)
            j = find_next_valid_index(t, j)
            
            if i < 0 and j < 0:  # Both strings are exhausted
                return True
            if i < 0 or j < 0 or s[i] != t[j]:  # Mismatch found
                return False
            
            i -= 1
            j -= 1
        
        return True
