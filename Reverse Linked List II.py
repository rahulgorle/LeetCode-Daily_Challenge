class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node before the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # Node before the left position
        
        # Move prev to the node before left position
        for _ in range(left - 1):
            prev = prev.next
        
        # Initialize current and next pointers for reversing
        current = prev.next
        next_node = None
        
        # Reverse the sublist from left to right
        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = next_node
            next_node = current
            current = next_temp
        
        # Connect the reversed sublist back to the original list
        prev.next.next = current
        prev.next = next_node
        
        return dummy.next
