class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix_sum = 0
        prefix_sum_map = {}
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum_map[0] = dummy
        
        while head:
            prefix_sum += head.val
            if prefix_sum in prefix_sum_map:
                # Remove nodes between the prefix_sum that equals 0
                temp = prefix_sum_map[prefix_sum].next
                temp_sum = prefix_sum + temp.val
                while temp_sum != prefix_sum:
                    del prefix_sum_map[temp_sum]
                    temp = temp.next
                    temp_sum += temp.val
                prefix_sum_map[prefix_sum].next = head.next
            else:
                prefix_sum_map[prefix_sum] = head
            head = head.next
        
        return dummy.next
