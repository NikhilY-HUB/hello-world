# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
            
        curr = head
        # Localize the next node check to minimize dot-lookup overhead
        nxt = curr.next
        
        while nxt:
            if curr.val == nxt.val:
                # Skip the duplicate
                curr.next = nxt.next
            else:
                # Move curr forward
                curr = nxt
            # Advance our lookup pointer
            nxt = curr.next
            
        return head