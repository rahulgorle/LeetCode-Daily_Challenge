class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Function to reverse a linked list
        def reverse_linked_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Function to compare two linked lists
        def compare_lists(list1, list2):
            while list1 and list2:
                if list1.val != list2.val:
                    return False
                list1 = list1.next
                list2 = list2.next
            return True
        
        if not head or not head.next:
            return True
        
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Reverse the first half of the linked list
        prev = None
        current = head
        for _ in range(length // 2):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # If the length is odd, move the current pointer to the next node
        if length % 2 == 1:
            current = current.next
        
        # Compare the reversed first half with the second half
        return compare_lists(prev, current)
