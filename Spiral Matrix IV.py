class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Step 1: Initialize the matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Define the spiral boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Traverse the linked list
        curr = head
        
        while top <= bottom and left <= right and curr:
            # Traverse from left to right on the top row
            for col in range(left, right + 1):
                if curr:
                    matrix[top][col] = curr.val
                    curr = curr.next
            top += 1  # Move the top boundary down

            # Traverse from top to bottom on the right column
            for row in range(top, bottom + 1):
                if curr:
                    matrix[row][right] = curr.val
                    curr = curr.next
            right -= 1  # Move the right boundary left

            # Traverse from right to left on the bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if curr:
                        matrix[bottom][col] = curr.val
                        curr = curr.next
                bottom -= 1  # Move the bottom boundary up

            # Traverse from bottom to top on the left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if curr:
                        matrix[row][left] = curr.val
                        curr = curr.next
                left += 1  # Move the left boundary right

        return matrix
