from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        n = len(formula)
        i = 0
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[i_start:i] or 1)
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplicity
            else:
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                elem = formula[i_start:i]
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                stack[-1][elem] += count
        
        final_counts = stack[0]
        sorted_elements = sorted(final_counts.keys())
        result = []
        
        for elem in sorted_elements:
            result.append(elem)
            if final_counts[elem] > 1:
                result.append(str(final_counts[elem]))
        
        return ''.join(result)
