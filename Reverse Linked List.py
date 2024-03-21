class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        
        while head:
            head.next, prev_node, head = prev_node, head, head.next
            
        return prev_node
