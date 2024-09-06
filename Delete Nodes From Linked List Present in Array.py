# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookups
        num_set = set(nums)
        
        # Initialize a dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the linked list
        while current.next:
            if current.next.val in num_set:
                # Skip the node with value in num_set
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the modified linked list starting from the original head
        return dummy.next
