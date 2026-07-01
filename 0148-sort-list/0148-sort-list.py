# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        right_head = slow.next
        slow.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)
        dummy = ListNode(0)
        tail = dummy

        l1, l2 = left_sorted, right_sorted

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next
        tail.next = l1 if l1 is not None else l2
        return dummy.next