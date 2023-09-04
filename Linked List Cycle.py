class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False  # There can't be a cycle with less than 2 nodes
        
        tortoise = head
        hare = head
        
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                return True  # The pointers have met, indicating a cycle
        
        return False  # No cycle found
