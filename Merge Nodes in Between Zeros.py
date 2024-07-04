class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head  # Initialize the 'left' pointer to the head
        right = head.next  # Initialize the 'right' pointer to the node after head

        current_sum = 0  # Initialize the sum of values between zeroes
        while right:
            if right.val == 0:
                left = left.next  # Move the 'left' pointer to the next node
                left.val = current_sum  # Assign the accumulated sum to the 'left' node
                current_sum = 0  # Reset the current sum
            else:
                current_sum += right.val  # Add the value of the 'right' node to the current sum
            right = right.next  # Move the 'right' pointer to the next node
        
        left.next = None  # Set the next node of the last merged node to None
        return head.next  # Return the merged list, skipping the initial zero
