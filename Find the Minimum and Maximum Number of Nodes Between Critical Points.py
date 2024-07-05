class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_cp = -1
        last_cp = -1
        min_distance = float('inf')
        prev_position = -1
        position = 1

        prev = head
        curr = head.next
        next = curr.next

        while next:
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                if first_cp == -1:
                    first_cp = position
                else:
                    min_distance = min(min_distance, position - prev_position)
                
                last_cp = position
                prev_position = position
            
            prev = curr
            curr = next
            next = next.next
            position += 1

        if first_cp == last_cp:
            return [-1, -1]

        return [min_distance, last_cp - first_cp]
