# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Calculate the size of each part and the number of extra nodes
        part_size = length // k  # Size of each part
        extra = length % k  # Number of extra nodes
        
        # Step 3: Split the linked list into k parts
        parts = []
        current = head
        
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if extra > 0 else 0)  # Adjust the size if there are extra nodes
            extra -= 1  # Decrement the extra count
            
            # Traverse the part to find the tail
            for j in range(part_length - 1):
                if current:
                    current = current.next
            
            if current:
                next_node = current.next
                current.next = None  # Disconnect the part from the rest of the list
                current = next_node
                
            parts.append(part_head)
        
        return parts
