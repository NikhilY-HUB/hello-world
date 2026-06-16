# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)

        small = small_dummy
        big = big_dummy
        curr = head

        while curr != None:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next
            curr = curr.next

        big.next = None
        small.next = big_dummy.next
        return small_dummy.next

