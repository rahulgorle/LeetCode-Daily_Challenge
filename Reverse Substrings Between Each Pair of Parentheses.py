class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                # Collect characters until the matching '('
                segment = []
                while stack and stack[-1] != '(':
                    segment.append(stack.pop())
                stack.pop()  # Remove the '('
                stack.extend(segment)  # Add the reversed segment back
            else:
                stack.append(char)
        return ''.join(stack)
