class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to count steps between curr and curr+1 (within limit n)
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10  # Move down the tree by multiplying by 10
                last = last * 10 + 9  # Extend range to cover all numbers at this level
            return steps

        curr = 1
        k -= 1  # We're treating '1' as the first number, so decrement k

        # Keep moving until we find the k-th smallest number
        while k > 0:
            steps = count_steps(curr, n)  # Count numbers in subtree rooted at 'curr'
            if steps <= k:
                # If there are fewer numbers than k, move to next sibling
                curr += 1
                k -= steps  # Decrement k by the number of skipped numbers
            else:
                # If k is within this subtree, go deeper into this subtree
                curr *= 10  # Go to the next level in the tree
                k -= 1  # Decrement k since we're moving to a child node

        return curr
