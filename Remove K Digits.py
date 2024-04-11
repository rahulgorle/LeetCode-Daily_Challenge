from collections import deque

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        non_zero_index = 0
        
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == '0':
            stack.popleft()
        
        return ''.join(stack) if stack else '0'
