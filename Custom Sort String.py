class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count the frequency of characters in string s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Construct the result string according to the order
        result = ""
        for char in order:
            if char in char_count:
                result += char * char_count[char]
                # Remove the character from the count dictionary after adding to the result
                del char_count[char]
        
        # Append the remaining characters in s to the result
        for char, count in char_count.items():
            result += char * count
        
        return result
