# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy

        for _ in range(left - 1):
            before_left = before_left.next
        reversed_tail = before_left.next

        prev = None
        curr = before_left.next

        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        before_left.next = prev
        reversed_tail.next = curr

        return dummy.next