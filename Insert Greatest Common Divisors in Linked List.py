import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        current = head
        
        # Traverse through the list until the second last node
        while current and current.next:
            # Find GCD of current and next node values
            gcd_val = math.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(gcd_val)
            
            # Insert the new node between current and current.next
            new_node.next = current.next
            current.next = new_node
            
            # Move to the next original node (skip the newly inserted node)
            current = new_node.next
        
        return head
