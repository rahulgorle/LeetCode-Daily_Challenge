class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Reorders the linked list in-place.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow points to the middle node (or the first node of the second half)
        second_half = slow.next
        slow.next = None  # Disconnect the first half from the second half
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        current = second_half
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second_half = prev  # New head of the reversed second half
        
        # Step 3: Merge the first half with the reversed second half
        first_half = head
        while first_half and second_half:
            temp1 = first_half.next
            temp2 = second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2
