class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Use memoization to store intermediate results
        memo = {}

        def compute(expr):
            # If the expression is already computed, return the result
            if expr in memo:
                return memo[expr]

            # Result list to store the computed results
            result = []

            # Iterate through the expression to find operators
            for i, char in enumerate(expr):
                if char in '+-*':
                    # Recursively compute left and right subexpressions
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    # Combine the results of left and right based on the operator
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                result.append(left + right)
                            elif char == '-':
                                result.append(left - right)
                            elif char == '*':
                                result.append(left * right)

            # Base case: if the expression contains no operators, it's a number
            if not result:
                result.append(int(expr))

            # Store the computed result in the memoization dictionary
            memo[expr] = result
            return result

        # Compute the result for the entire expression
        return compute(expression)
