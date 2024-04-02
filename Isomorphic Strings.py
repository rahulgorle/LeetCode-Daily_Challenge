class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}  # Mapping from characters in s to characters in t
        
        for char_s, char_t in zip(s, t):
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                if char_t in mapping.values():  # Check if char_t is already mapped to another character in s
                    return False
                mapping[char_s] = char_t
        
        return True
