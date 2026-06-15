# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head and not head.next:
            return True

        slow = head
        fast = head 

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first_half = head
        second_half = prev

        while second_half != None:
            if first_half.val != second_half.val:
                return False

            first_half = first_half.next
            second_half = second_half.next
        return True