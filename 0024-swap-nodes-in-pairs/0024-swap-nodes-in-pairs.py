# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next is not None and prev.next.next is not None:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second
            prev = first

        return dummy.next
