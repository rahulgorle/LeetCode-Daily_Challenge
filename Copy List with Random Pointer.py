# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create a mapping from original nodes to their corresponding new nodes
        mapping = {}

        # First pass: Create new nodes and copy values while building the mapping
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        # Second pass: Connect next and random pointers using the mapping
        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next

        # Return the head of the copied linked list
        return mapping[head]
