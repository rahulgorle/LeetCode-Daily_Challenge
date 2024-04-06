class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert string to list for efficient manipulation
        s = list(s)
        stack = []

        # First pass: mark invalid closing parentheses and their corresponding opening parentheses
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''  # Mark invalid closing parentheses for removal

        # Second pass: mark unmatched opening parentheses
        for i in stack:
            s[i] = ''  # Mark unmatched opening parentheses for removal

        # Join the list and return the result
        return ''.join(s)
