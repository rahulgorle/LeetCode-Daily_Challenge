class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the nodes at positions a-1, a, b, and b+1
        prev_a = None
        current = list1
        for _ in range(a - 1):
            current = current.next
        prev_a = current
        for _ in range(b - a + 2):
            current = current.next
        next_b = current

        # Connect the node at position a-1 to the head of list2
        prev_a.next = list2

        # Find the last node of list2
        current = list2
        while current.next:
            current = current.next

        # Connect the last node of list2 to the node at position b+1
        current.next = next_b

        return list1
