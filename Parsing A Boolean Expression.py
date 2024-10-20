class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()  # remove '('

                operator = stack.pop()

                if operator == '&':
                    stack.append('t' if all(x == 't' for x in seen) else 'f')
                elif operator == '|':
                    stack.append('t' if any(x == 't' for x in seen) else 'f')
                elif operator == '!':
                    stack.append('f' if 't' in seen else 't')
            elif char != ',':
                stack.append(char)

        return stack[0] == 't'
