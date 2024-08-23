from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Parse the expression and extract fractions
        fractions = []
        i = 0
        while i < len(expression):
            start = i
            if expression[i] in "+-":
                i += 1
            while i < len(expression) and expression[i] != '+' and expression[i] != '-':
                i += 1
            fractions.append(Fraction(expression[start:i]))
        
        # Sum up all the fractions
        result = sum(fractions)
        
        # Convert the result to the required format
        return f"{result.numerator}/{result.denominator}"
